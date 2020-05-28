from flask import Flask 
app = Flask(__name__)
import random
import pandas as pd
import os

@app.route('/')
def hello_world():
	return 'Hello, world!'