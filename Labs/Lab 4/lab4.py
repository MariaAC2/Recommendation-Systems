# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import preprocessing
import math
import io
import sklearn
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("nike_data_2022_09.csv", encoding="utf-8")
df = df.head(10)

text_data = df["description"].dropna().astype(str)
cleaned_text = text_data.apply(lambda x: re.sub(r"<[^>]+>", "", x))

tfidf = TfidfVectorizer(stop_words="english")
response = tfidf.fit_transform(cleaned_text)
tfidf.get_feature_names_out()

print(cosine_similarity(response))