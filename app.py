from flask import Flask 
app = Flask(__name__)
import random
import pandas as pandas
import os

@app.route('/')
def hello_world():
	return 'Hello, world!'