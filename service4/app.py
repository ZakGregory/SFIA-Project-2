from flask import Flask, request, Response
import requests 

app = Flask(__name__)

@app.route('/post_attack/', methods=["POST"])
def post_attack():
    numbers= request.data.decode("utf-8")
    numberslist=numbers.split(",")
    
    randint=int(numberslist[0])
    randfloat=float(numberslist[1])

    if randint == 0:
        returnstring= "MISSED"
    elif randint == 2 and randfloat > 5:
        returnstring= "CRIT"
    else:
        returnstring= "HIT"
    return Response(returnstring, mimetype='text/plain')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)
