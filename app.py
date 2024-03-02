from flask import Flask
import os
from threading import Thread


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!
    
    
    def app():
	t = Thread(target=run)
	t.start()