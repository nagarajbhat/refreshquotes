from flask import Flask, render_template
import random
import pandas as pd
import os
from logic import randomquote


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
	data = pd.read_csv('data/quotes.csv')
	author,quote = randomquote(data)
	return render_template('index.html',
		author = author,
		quote = quote)


if __name__ == "__main__":
	 # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)