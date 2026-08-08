import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer

df = pd.read_csv('IMDB-Movie-Data.csv')  # Load your dataset

print(df.head(5))  # Display the first few rows of the dataset   



