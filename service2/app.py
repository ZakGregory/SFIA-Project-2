from flask import Flask, request, Response
import requests 
import random

@app.route('/get_numbers/', methods=["GET"])
def get_numbers():
    randomint= random.randint(0,2)
    return Response(randomint, mimetype='text/plain')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
