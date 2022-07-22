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

# Imported Analysis tools
import spacy
import re
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

DATASET = 'menu/logical/data/preprocessing_finish.csv'
# Updated info dataset 

def main_recommendation():
    pass

if __name__ == '__main__':
    main_recommendation()