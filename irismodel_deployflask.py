# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:09:33 2022

@author: sree
"""

from flask import Flask,request
import pickle
import numpy as np


app = Flask(__name__)

model_pk = pickle.load(open("flower-v1.pkl","rb"))

@app.route('/api_predict', methods=["GET","POST"])
def api_predict():
    if request.method == "GET":
        return "Please send POST request"
    elif request.method == "POST":
        data = request.get_json()
        
        sepal_length = data["sepal_length"]
        sepal_width = data["sepal_width"]
        petal_length = data["petal_length"]
        petal_width = data["petal_width"]
        
        inp=np.array([[sepal_length,sepal_width,sepal_width,petal_width]])
        
        prediction = model_pk.predict(inp)
        
        return str(prediction)
    
app.run()

import requests

url = "http://127.0.0.1:5000/api_predict"

data = {
        "sepal_length" : 2,
        "sepal_width" : 3,
        "petal_length" : 4,
        "petal_width" : 5
        }

r = requests.post(url, json=data)
print(r)

print(r.text)