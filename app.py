from flask import Flask 
app = Flask(__name__)
import random
import pandas as pd
import os

@app.route('/')
def hello_world():
	return 'Hello, world!'

if __name__ == "__main__":
	 # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)