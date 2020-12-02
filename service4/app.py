from flask import Flask, request, Response
import requests 

@app.route('/post_prize/', methods=["POST"])
def post_prize():
    numbers= request.data.decode("utf-8")
    numberslist=numbers.split(",")
    
    randint=int(numberslist[0])
    randfloat=float(numberslist[1])

    returnnuber=randint*randfloat

    return Response(returnnuber, mimetype='text/plain')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)
