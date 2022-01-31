import argparse
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from features import LexicalFeatures

class Classifier(LexicalFeatures):
    def __init__(self, corpus, file=True):
        self.output = ""
        self.features = [method for method in dir(LexicalFeatures) if not method.startswith('__')] 
        
        if file:
            self.filename = corpus
            self.corpus = Path(corpus).read_text()
        else:
            self.corpus = corpus
    
    def __repr__(self):
        return f"<Classifier Object> : {[i for i in self.features]}"
    
    def plot(self, features, type_, legend, **labels):
        line_style = ['solid', 'dotted', 'dashed', 'dashdot']

        isNested_feature = any(isinstance(i, list) for i in features)

        if isNested_feature:
            for index, feature in enumerate(features):
                if type_ == "plot":
                    plt.plot(feature, linestyle = line_style[index], label=legend[index])
                elif type_ == "historgram":
                    sns.displot(feature, kde = False, bins = 70, color = 'blue')
                    return
        else:
            if type_ == "plot":
                plt.plot(features)
            elif type_ == "historgram":
                sns.displot(features, kde = False, bins = 70, color = 'blue')
        
        if 'x_label' in labels.keys() or 'y_label' in labels.keys():
            plt.xlabel(labels['x_label'])
            plt.ylabel(labels['y_label'])

        plt.legend(loc=labels['location'])
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
        word_frequencies = []
        for corpus in inp_file:
            classify = Classifier(corpus, file=True)

            print(classify.word_frequency()[:30])

            word_frequencies.append([word[1] for word in classify.word_frequency()[:50]])
            
            print("Average word length:", classify.average_word_length())
            print("Average sentences length:", classify.average_sentence_length())
            print(classify.average_word_length(ret_data=True))
            #classify.plot(classify.average_word_length(ret_data=True), legend=["Word length frequency"], type_="histogram")
    
        
        classify.plot(word_frequencies, 'plot', legend=['UNABOMBER', 'Hegel'], x_label='most used words', y_label='number of occurencies', location='upper right')

            #with open(file, "r+") as f:
            #    corpus.append(f.read())
    else:
            classify = Classifier(inp_file, file=True)

            print(classify.word_frequency()[:30])
            
            print("Average word length:", classify.average_word_length())
            print("Average sentences length:", classify.average_sentence_length())

            classify.plot([word[1] for word in classify.word_frequency()], legend=['UNABOMBER'])

    #classify = Classifier(corpus)

    #print("Feautures:", classify)

    #print(classify.word_frequency())
    
    #print("Average word length:", classify.average_word_length())
    #print("Average sentences length:", classify.average_sentence_length())

    #classify.word_frequency()


if __name__ == "__main__":
    main()