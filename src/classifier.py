import utils
import argparse

import matplotlib.pyplot as plt
import nltk

from nltk.tokenize import sent_tokenize, word_tokenize

class Classifier:
    def __init__(self, corpus):
        self.corpus = corpus
        self.output = ""
        self.features = ""
    
    def __repr__(self):
        return f"<Classifier Object> : {[i for i in self.features]}"
    
    def word_frequency(self):
        count_words = {}
        for index, word in enumerate(self.corpus):
            if word not in count_words:
                count_words[word] = 1
            else:
                count_words[word] += 1

        return utils.removeStopwords(count_words)
    
    def average_word_length(self):
        #word_list = utils.removeStopwords(self.corpus)
        word_list = word_tokenize(self.corpus)

        # Calculate the mean
        return sum([len(word) for word in word_list]) // len(word_list)
    
    def average_sentence_length(self):
        """
        Number of words n sentence on average
        """
        sentences = sent_tokenize(self.corpus) 
        return sum([len(sentence.split()) for sentence in sentences]) // len(sentences)

def main():
    inp_file = "data/sample_corpus.txt"
    parser = argparse.ArgumentParser(description='Process file url')

    parser.add_argument('--path', help='enter the path to the corpus')

    args = vars(parser.parse_args())

    if args["path"]:
        inp_file = args["path"]

    args = parser.parse_args()

    with open(inp_file, "r+") as f:
        corpus = f.read()

    classify = Classifier(corpus)
    #print(classify.word_frequency())
    print("Average word length:", classify.average_word_length())
    print("Average sentences length:", classify.average_sentence_length())

if __name__ == "__main__":
    main()