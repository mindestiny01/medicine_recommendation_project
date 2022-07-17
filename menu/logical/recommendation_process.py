## Pre Processing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import linear_kernel
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from tqdm import tqdm

## Classification 
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

import re
import streamlit as st
import numpy as np
import pandas as pd
import spacy
# from menu.logical.db import get_save_data, get_user_review, get_symtomps, get_user_name

DATASET = 'indonesian_medicine_dataset.csv'

def recommendation(record_symtomps: list):
    return record_symtomps[0]

def pre_processing_data():
    dt = pd.read_csv(DATASET); dt = dt.loc[:, ~dt.columns.str.contains('^Unnamed')]
    print(dt.dtypes)

    stopwords = StopWordRemoverFactory().get_stop_words()



pre_processing_data()