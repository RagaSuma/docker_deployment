# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:46:57 2022

@author: sree
"""


from flask import Flask, request

app = Flask(__name__)

@app.route('/hello_world')
def hello():
    return "Hello World"

app.run()

@app.route('/add',methods=["GET"])
def add_Get():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(a+b)

app.run()

@app.route('/add',methods=["POST"])
def add_POST():
    data = request.get_json()
    a = data['a']
    b = data['b']
    return str(int(a)+int(b))

app.run()