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

# Updated Database from users
from menu.logical.db import get_user_name, get_symtomps, get_save_data, get_user_review

# Imported Analysis tools
import spacy
import re
import streamlit as st
import numpy as np
import pandas as pd

DATASET = './data/indonesian_medicine_dataset.csv'

def pre_processing_data():
    dt = pd.read_csv(DATASET); dt = dt.loc[:, ~dt.columns.str.contains('^Unnamed')]
    print(dt.dtypes)

def get_tokenize():
    pass
    stopwords = StopWordRemoverFactory().get_stop_words()

def optimalization_token():
    pass

def step_of_recommendation():
    pass

def main_recommendation(record_symtomps: list):
    return record_symtomps[0]

if __name__ == '__main__':
    pre_processing_data()