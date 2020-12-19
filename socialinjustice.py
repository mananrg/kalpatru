import spacy
from googlenewsapi import news
nlp =spacy.load('en_core_web_md')

data=news()

text_list=['Trolled','Abused','Employability' ,'Education','Health','Travel','Leisure','Gender','Racism']
