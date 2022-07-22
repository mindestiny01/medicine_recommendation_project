from data.symtomps import symtomps
from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pandas as pd
import numpy as np
import re

######### CASE FOLDING
def get_lower(dataframe):
    dataframe = str(dataframe).lower()
    return dataframe

######### REMOVE PUNCTUATION
def get_remove_punctuation(dataframe):

    # compile all the symbols and numbers
    clean_from_symbols = re.compile('[/(){}\[\]?\|@,.;]'); 
    clean_from_alnum = re.compile('[^0-9a-z]')

    # sub the compiled symbols and return to be empty string
    # sub the compiled alphanumerical and return to be whitespace  
    dataframe = clean_from_symbols.sub('', dataframe)
    dataframe = clean_from_alnum.sub(' ', dataframe)

    return dataframe

########## REMOVE DOUBLE OR MORE WHITESPACES
def get_remove_whitespaces_url(dataframe):

    # casting to string
    corrected = str(dataframe)

    ## white spaces
    corrected = re.sub(r"//t",r"\t", corrected)
    corrected = re.sub(r"( )\1+",r"\1", corrected)
    corrected = re.sub(r"(\n)\1+",r"\1", corrected)
    corrected = re.sub(r"(\r)\1+",r"\1", corrected)
    corrected = re.sub(r"(\t)\1+",r"\1", corrected)

    ## Unimportant Link
    corrected = re.sub('http://\S+|https://\S+', '', corrected)
    corrected = re.sub('http[s]?://\S+', '', corrected)
    corrected = re.sub(r"http\S+", "", corrected)
    dataframe = corrected.strip(" ")
    return dataframe

######### FILTERING / STOPWORDS
def get_stopwords(dataframe):

    # using Sastrawi Library for the removing stopwords
    factory = StopWordRemoverFactory()
    stopwords = factory.create_stop_word_remover()
    dataframe = stopwords.remove(dataframe)
    return dataframe

########## STEMMING WITH SASTRAWI
def get_stemming(dataframe):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    dataframe = stemmer.stem(dataframe)
    return dataframe

########## TOKENIZING
def get_tokenizing(dataframe):

    # use nltk for tokenizing
    dataframe = word_tokenize(dataframe)
    
    # Deleting the last index
    del dataframe[-1]

    return dataframe

if __name__ == '__main__':

    # Import the dataset
    dt = pd.read_csv('data/indonesian_medicine_dataset.csv'); dt.loc[:, ~dt.columns.str.contains('^Unnamed')]
    
    # Applyin the function one by one as a new columns
    dt['lower_dataframe'] = dt['Overview'].apply(get_lower)
    dt['no_punctuation_text'] = dt['lower_dataframe'].apply(get_remove_punctuation)
    dt['remove_whitespaces'] = dt['no_punctuation_text'].apply(get_remove_whitespaces_url)
    dt['stopwords'] = dt['remove_whitespaces'].apply(get_stopwords)

    # Get match topics from the bunch of medication keywords and return a new column as match_info
    match = r"\b({})\b".format("|".join(x for x in symtomps))
    dt['match_info'] = dt['stopwords'].str.extract(match).fillna('not match')
    
    # Create a dictionary for the new dataset
    new_dataset = {
        'Name' : dt['Name'],
        'Symtomps': dt['match_info']
    }

    # Save the dataset
    save = pd.DataFrame(new_dataset)
    save.to_csv('data/final_result.csv')
    print('OK!')