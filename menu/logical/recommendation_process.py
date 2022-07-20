'''
    Pre Processing Dataset
    
    1. Importing the dataset
    2. Case Folding
    3. Remove Punctuation
    4. Deleting double or more whitespaces
    5. Stopwords Removal
    6. Lemmatization or Stemming
    7. Tokenizing

    Processing / Recommendation

'''

## PRE PROCESSING
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from tqdm import tqdm
import nltk

## PROCESSING / RECOMMENDATION
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import linear_kernel


from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Updated Database from users
from menu.logical.db import get_user_name, get_symtomps, get_save_data, get_user_review

# Imported Analysis tools
import spacy
import re
import streamlit as st
import numpy as np
import pandas as pd

DATASET = './data/indonesian_medicine_dataset.csv'

def overview_case_folding(overview_info):

    # Process the Overview column to change the case to lower
    overview_info = overview_info.lower()
    return overview_info

def remove_data_punctuation(overview_info):

    # Applying regex to removing any symbols
    clean_spcl = re.compile('[/(){}\[\]\|@,;]')
    clean_symbol = re.compile('[^0-9a-z]')

    overview_info = clean_spcl.sub('', overview_info)
    overview_info = clean_symbol.sub(' ', overview_info)
    return overview_info

def get_delete_whitespace(overview_info):

    # Deleting double or more whitespaces
    corrected = str(overview_info)
    corrected = re.sub(r"//t",r"\t", corrected)
    corrected = re.sub(r"( )\1+",r"\1", corrected)
    corrected = re.sub(r"(\n)\1+",r"\1", corrected)
    corrected = re.sub(r"(\r)\1+",r"\1", corrected)
    corrected = re.sub(r"(\t)\1+",r"\1", corrected)
    return corrected.strip(" ")

def get_lemma_stem(overview_info):
    
    # Porter Stemming Algorithms
    overview_info = ' '.join(PorterStemmer.stem(word) for word in overview_info.split() if word in overview_info)
    
    # Lancester Stemming Algorithms
    overview_info = ' '.join(LancasterStemmer.stem(word) for word in overview_info.split() if word in overview_info)

    # Lemmatization
    overview_info = ' '.join(WordNetLemmatizer.lemmatize(word) for word in overview_info.split() if word in overview_info)
    return overview_info



def removal_stopwords(overview_info):

    # Set the stopwords with indomesian language
    get_stopwords = set(stopwords.words("indonesian"))
    overview_info = ' '.join(word for word in overview_info.split() if word not in get_stopwords)


    # You can added some additional stopwords
    add = pd.DataFrame(overview_info)
    overview_info = add.replace(to_replace =['whether','yes','also','thanks','take','whatever',
                    'making','makes','taking','takes','ok','oh','etc',
                                        "yep"],  
                            value ="", regex= True)     
    overview_info

    return overview_info

def get_tokenize(overview_info):

    # divided the all text/sentences to be a list of words
    overview_info = word_tokenize(overview_info)
    return overview_info

def optimalization_token(overview_info):

    # Optimalize the tokenizing by implementing nltk library
    lemma = pd.DataFrame(overview_info)
    token = nltk.tokenize.WhitespaceTokenizer().tokenize(lemma['desc_clean_lemma'][108])

def step_of_recommendation(record_symtomps: list, overview_info):
    
    # Implementing the content based recommendation based on symtomps
    pass

def main_recommendation(record_symtomps: list):

    # return the top of recommendation
    return record_symtomps[0]

def get_visualization():

    # creating some of important visualization info for recommmendation
    pass

def count_vectorizer_example():

    #Example of Processing the Text
    count_vectorizer= CountVectorizer(encoding='latin-1', ngram_range=(1,1), 
                                  tokenizer=None, analyzer='word',
                                  stop_words= None)
    countvec= count_vectorizer.fit_transform(df['desc_cleanfix']).toarray()
    return countvec

def pre_processing_data():

    # Importing the dataset and removing some unimportant column
    dt = pd.read_csv(DATASET); dt = dt.loc[:, ~dt.columns.str.contains('^Unnamed')]
    dt['pre_processing'] = dt['Overview']
    
    overview_case_folding(dt['pre_processing'])

if __name__ == '__main__':
    pre_processing_data()