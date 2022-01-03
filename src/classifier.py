import argparse
import string
import matplotlib.pyplot as plt

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from textstat.textstat import textstatistics,legacy_round


class Classifier():
    def __init__(self, corpus):
        self.corpus = corpus
        self.output = ""
        self.features = [method for method in dir(Classifier) if not method.startswith('__')] 
    
    def __repr__(self):
        return f"<Classifier Object> : {[i for i in self.features]}"
    
    def word_frequency(self):
        count_words = {}
        filtered_words = [word.lower() for word in word_tokenize(self.corpus) if word.lower() not in stopwords.words('english') and not word in string.punctuation]

        for index, word in enumerate(filtered_words):
            if word not in count_words:
                count_words[word] = 1
            else:
                count_words[word] += 1
        
        return sorted(count_words.items(), key=lambda x: x[1], reverse=True)
    
    def most_common_stopwords(self):
        count_words = {}
        # Words without punctuation
        filtered_words = [word.lower() for word in word_tokenize(self.corpus) if word.lower() not word in string.punctuation]

        for word in filtered_words:
            if word not in count_words:
                count_words[word] = 1
            else:
                count_words[word] += 1

        return sorted(count_words.items(), key=lambda x: x[1], reverse=True)
    
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
    
    def character_space(self):
        return len(self.corpus)
    
    def syllables_count(self, word):
        return textstatistics().syllable_count(word)
    
    def complexity_words(self, document):
        pass


    def difficult_words(self, text):
    
        words = []
        sentences = sent_tokenize(self.corpus)
        for sentence in sentences:
            words += [str(token) for token in sentence]
    
        # difficult words are those with syllables >= 2
        # easy_word_set is provide by Textstat as
        # a list of common words
        diff_words_set = set()
        
        for word in words:
            syllable_count = self.syllables_count(word)
            if word not in stopwords.words('english') and syllable_count >= 2:
                diff_words_set.add(word)
    
        return len(diff_words_set)

    def poly_syllable_count(self, text):
        count = 0
        words = []
        sentences = sent_tokenize(text)
        for sentence in sentences:
            words += [token for token in sentence]
        
    
        for word in words:
            syllable_count = self.syllables_count(word)
            if syllable_count >= 3:
                count += 1
        return count
    
    def gunnin_for_readability_index(self):
        return 0.4 * (len(word_tokenize(self.corpus)) / len(sent_tokenize(self.corpus)) + 100 * (len(self.complexity_words(self.corpus)) // len(word_tokenize(self.corpus))))
    
    def plot(self, **features):
        for feature in features:
            plt.plot(feature)
        
        plt.show()

def main():
    inp_file = "../data/sample_corpus.txt"
    multiple_files = False

    parser = argparse.ArgumentParser(description='Process file url')
    parser.add_argument('--path', help='enter the path to the corpus')
    args = vars(parser.parse_args())

    if args["path"]:
        inp_file = args["path"]
        if ";" in inp_file:
            inp_file = inp_file.split(';')
            multiple_files = True

    args = parser.parse_args()

    if multiple_files:
        corpus = []
        for file in inp_file:
            with open(file, "r+") as f:
                corpus.append(f.read())
    else:
        with open(inp_file, "r+") as f:
            corpus = f.read()

    #classify = Classifier(corpus)

    #print("Feautures:", classify)

    #print(classify.word_frequency())
    
    #print("Average word length:", classify.average_word_length())
    #print("Average sentences length:", classify.average_sentence_length())

    #classify.word_frequency()


if __name__ == "__main__":
    main()