import pandas as pd
import random

# this is for quotes.csv ->	
data = pd.read_csv('data/quotes.csv')

# this function returns a random author,quote from the csv
def randomquote(data):
	pos = random.randint(0,len(data['Author'])-1)
	author = data['Author'][pos]
	quote = data['Quote'][pos]
	return author,quote

"""

#this is for inspquotes.csv ->

#data = pd.read_csv('data/n_quotes_all.csv',names=['AUTHOR','QUOTE','GENRE'],sep=';')
data = pd.read_csv('data/inspquotes.csv',sep=';')
print(data.head()
def randomquote(data):
	#pos = random.randint(0,len(data['AUTHOR'])-1)
	pos=1
	author = data['AUTHOR'][pos]
	quote = data['QUOTE'][pos]
	genre = data['GENRE'][pos]
	return author,quote
"""
#print(randomquote(data))
#print(data.isnull().sum())