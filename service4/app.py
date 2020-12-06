from flask import Flask, request, Response
import requests 

app = Flask(__name__)

@app.route('/post_prize/', methods=["POST"])
def post_prize():
    numbers= request.data.decode("utf-8")
    numberslist=numbers.split(",")
    
    randint=int(numberslist[0])
    randfloat=float(numberslist[1])

    returnnumber=randint*randfloat
    
    returnstring=str(returnnumber)
    
    if randint == 0:
        returnstring+= ",missed"
    elif randint == 0:
        returnstring+= ",hit"
    else:
        returnstring+= ",crit"
    return Response(returnstring, mimetype='text/plain')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)
