from flask import Flask, request, jsonify, Response
import requests 

from application import app

@app.route('/')
@app.route('/home')
def home():
    '''
    APIs
    ''' 
    
    return 
