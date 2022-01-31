import string

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from textstat.textstat import textstatistics,legacy_round

class LexicalFeatures:
    def __init__(self):
        pass

    def word_frequency(self):
        count_words = {}
        filtered_words = [word.lower() for word in word_tokenize(self.corpus) if word.lower() not in stopwords.words('english') and word.lower() not in string.punctuation and word.lower() not in ['""', "''", '``']]

        for index, word in enumerate(filtered_words):
            if word not in count_words:
                count_words[word] = 1
            else:
                count_words[word] += 1
        
        return sorted(count_words.items(), key=lambda x: x[1], reverse=True)
    
    def most_common_stopwords(self):
        count_words = {}
        # Words without punctuation
        filtered_words = [word.lower() for word in word_tokenize(self.corpus) if word.lower() not in string.punctuation]
        for word in filtered_words:
            if word not in count_words:
                count_words[word] = 1
            else:
                count_words[word] += 1

        return sorted(count_words.items(), key=lambda x: x[1], reverse=True)
    
    def average_word_length(self, ret_data=False):
        #word_list = utils.removeStopwords(self.corpus)
        word_list = word_tokenize(self.corpus)

        if ret_data:
            return [len(word) for word in word_list]

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

    def find_shortest_corpus(self):
        for word in self.corpus:
            pass
