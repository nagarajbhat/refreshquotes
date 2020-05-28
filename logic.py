import pandas as pd
import random

# this is for quotes.csv ->	
data = pd.read_csv('data/quotes.csv')
def randomquote(data):
	pos = random.randint(0,len(data['Author'])-1)
	author = data['Author'][pos]
	quote = data['Quote'][pos]
	return author,quote

"""
#this is for inspquotes.csv ->

data = pd.read_csv('data/inspquotes.csv',names=['quote','author','genre'])

def randomquote(data):
	pos = random.randint(0,len(data['Author'])-1)
	author = data['Author'][pos]
	quote = data['Quote'][pos]
	genre = data['GENRE'][pos]
	return author,quote,genre

print(randomquote(data))
"""
