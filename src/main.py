from camel_tools.tokenizers.word import simple_word_tokenize
from camel_tools.disambig.mle import MLEDisambiguator
from camel_tools.tokenizers.morphological import MorphologicalTokenizer
import pandas as pd
from nltk import ISRIStemmer
import warnings
from pyarabic import araby
from stop_words import ArabicStopWords
import re

# Suppress warnings
warnings.filterwarnings("ignore")

# Initialize MLEDisambiguator
mle = MLEDisambiguator.pretrained('calima-msa-r13')

# Initialize MorphologicalTokenizer
tokenizer = MorphologicalTokenizer(mle, scheme='d3tok', split=True)

def tokenize(sentence):
    # Tokenize the sentence
    sentence = simple_word_tokenize(sentence)
    tokens = tokenizer.tokenize(sentence)

    # Filter out tokens containing '+'
    tokens = [token for token in tokens if '+' not in token]

    return tokens

def remove_stop_words(tokens):
    stop_words = ArabicStopWords()
    filtered = [token for token in tokens if token not in stop_words.get_stop_words()]
    return filtered

def print_stop_words(tokens):
    stop_words = ArabicStopWords()
    filtered = [token for token in tokens if token in stop_words.get_stop_words()]
    return filtered

def stemming(filtered_tokens):
    stemmer = ISRIStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    return stemmed_tokens

def normalize(token):
    token = re.sub("[إأآا]", "ا", token)
    token = re.sub("ى", "ي", token)
    token = re.sub("ة", "ه", token)
    token = re.sub("[\W\d]", "", token)
    token = araby.strip_diacritics(token)
    token = araby.strip_tatweel(token)
    return token

file_path = 'Your_File_Name.txt'
cols = ['Text']
sample = pd.DataFrame(columns=cols)

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            line_parts = line.strip().split('\t')
            text = line_parts[0]
            new_row = pd.DataFrame({'Text': text}, index=[0])
            sample = pd.concat([sample, new_row], ignore_index=True)
        except:
            pass

# Data preprocessing
for row in range(len(sample)):
    # Tokenization
    sample['Text'][row] = tokenize(sample['Text'][row])

    # Normalization
    sample['Text'][row] = [normalize(token) for token in sample['Text'][row]]

    # Removing Stop Words
    sample['Text'][row] = remove_stop_words(sample['Text'][row])

    # Stemming
    sample['Text'][row] = stemming(sample['Text'][row])

    # Removing null values
    sample['Text'][row] = [text for text in sample['Text'][row] if text != '']
    if not sample['Text'][row]:  # check if the list is empty
        sample.drop(row, inplace=True)

# Save the cleaned data to a txt file
sample.to_csv('output.txt', index=False)
