from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # data from javascript
    data = request.get_json()
    category = data.get('category')
    unit1 = data.get('unit1') 
    unit2 = data.get('unit2')
    num1 = float(data.get('val', 0))

    answer = 0 

    if category == "w":
        if unit1 == "cg" and unit2 == "mg": 
            answer = num1 * 10 
        elif unit1 == "cg" and unit2 == "g": 
            answer = num1 / 100 
        elif unit1 == "cg" and unit2 == "kg":
            answer = num1 / 10000 
        elif unit1 == "g" and unit2 == "mg": 
            answer = num1 * 1000 
        elif unit1 == "g" and unit2 == "cg": 
            answer = num1 * 100 
        elif unit1 == "g" and unit2 == "kg": 
            answer = num1 / 1000
        elif unit1 == "mg" and unit2 == "cg": 
            answer = num1 / 10
        elif unit1 == "mg" and unit2 == "g": 
            answer = num1 / 1000
        elif unit1 == "mg" and unit2 == "kg": 
            answer = num1 / 1000000
        elif unit1 == "kg" and unit2 == "g": 
            answer = num1 * 1000
        elif unit1 == "kg" and unit2 == "cg": 
            answer = num1 * 100000
        elif unit1 == "kg" and unit2 == "mg": 
            answer = num1 * 1000000
        elif unit1 == unit2: 
            answer = num1

    elif category == "l":
        if unit1 == "cm" and unit2 == "mm": 
            answer = num1 * 10 
        elif unit1 == "cm" and unit2 == "m": 
            answer = num1 / 100 
        elif unit1 == "cm" and unit2 == "km": 
            answer = num1 / 10000 
        elif unit1 == "m" and unit2 == "mm": 
            answer = num1 * 1000 
        elif unit1 == "m" and unit2 == "cm": 
            answer = num1 * 100 
        elif unit1 == "m" and unit2 == "km": 
            answer = num1 / 1000
        elif unit1 == "mm" and unit2 == "cm":
            answer = num1 / 10
        elif unit1 == "mm" and unit2 == "m": 
            answer = num1 / 1000
        elif unit1 == "mm" and unit2 == "km": 
            answer = num1 / 1000000
        elif unit1 == "km" and unit2 == "m": 
            answer = num1 * 1000
        elif unit1 == "km" and unit2 == "cm": 
            answer = num1 * 100000
        elif unit1 == "km" and unit2 == "mm": 
            answer = num1 * 1000000
        elif unit1 == unit2: 
            answer = num1

    # send back to js
    return jsonify({ 'result': answer })

if __name__ == '__main__' :
    app.run( host='0.0.0.0', port=5000, debug=True)