from classifier import Classifier

class TestClassifier():
    def __init__(self):
        self.inp_file = ["../data/unabomber.txt", "../data/phenomology_of_spirit.txt"]

    def test_lexical_features(self):
        """
        Test the lexical features of the corpus 
        """

        word_frequencies = []
        for corpus in self.inp_file:
            classify = Classifier(corpus, file=True)

            print(classify.word_frequency()[:30])
            
            word_freq = [ [word[1] for word in classify.word_frequency()[:50] ] , [word[0] for word in classify.word_frequency()[:50] ]]

            word_frequencies.append(word_freq)

            average_word_len, average_sent_len = classify.average_word_length(), classify.average_sentence_length()
            
            print("Average word length:", average_word_len)
            print("Average sentences length:", average_sent_len)

            #print(classify.average_word_length(ret_data=True))
            classify.plot(classify.average_word_length(ret_data=True), legend=["Word length frequency"], type_="histogram", x_label='most used words', y_label='number of occurencies', location='upper right')
    
        
        #classify.plot(word_frequencies, 'plot', legend=['UNABOMBER', 'Hegel'], x_label='most used words', y_label='number of occurencies', location='upper right')


if __name__ == '__main__':
    c = TestClassifier()
    c.test_lexical_features()