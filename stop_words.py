from nltk.tokenize import word_tokenize
from pyarabic import araby

class ArabicStopWords:
    def get_stop_words(self):
        sample = open('stop_words.txt', 'r', encoding='utf-8')
        sample_Words = str(sample.read())
        stopwords = araby.tokenize(sample_Words)
        return stopwords
