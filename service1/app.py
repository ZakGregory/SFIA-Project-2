from application import app
import requests 

@app.route('/')
@app.route('/home')
def home():
    randint = requests.get('http://service2:5001/get_integer/').text
    randfloat = requests.get('http://service3:5002/get_float/').text

    poststring = randint+","+randfloat

    prize = requests.post('http://service4:5003/post_prize/', poststring).text
    printstring= randint + randfloat + prize
    return printstring

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
