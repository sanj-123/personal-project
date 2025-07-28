from flask import Flask, request, jsonify
from flask_cors import CORS
from math import gcd 

app = Flask(__name__) 
CORS(app) 

def isPrime(n):
    if (n < 0):
        return False 
    if (n == 0 or n == 1):
        return False
    if (n == 2):
        return True
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True 

def isFibonacci(n):
    if (n < 0):
        return False 
    if (n == 0 or n == 1):
        return True 
    first = 1
    second = 1 
    sum = 0
    while (sum < n):
        sum = first + second 
        first = second
        second = sum 
    if (sum == n):
        return True 
    return False 

@app.route('/check_prime', methods=['POST'])
def check_prime():
    data = request.get_json()
    number = int(data.get("number")) 
    result = isPrime(number) 
    return jsonify({"isPrime": result})

@app.route('/factorial', methods=['POST'])
def factorial():
    data = request.get_json() 
    n = int(data.get('number', 0)) 
    if n < 0:
        return jsonify({"result": "undefined for negative numbers"})
    if n == 0 or n == 1:
        return jsonify({"result": str(1)})
    result = 1
    for i in range(2, n + 1):
        result *= i 
    return jsonify({"result": str(result)}) 

@app.route('/fibonacci', methods=['POST'])
def check_fibonacci():
    data = request.get_json()
    number = int(data.get("number"))
    result = isFibonacci(number)
    return jsonify({"isFibonacci": result})

@app.route('/properties', methods=['POST'])
def check_property():
    data = request.get_json() 
    number = int(data.get("number"))
    if (number <= 0):
        return jsonify({"result": "neither - only positive numbers are valid"})
    sum = 0
    for i in range(1, number):
        if (number % i == 0):
            sum += i
    if (sum == number):
        return jsonify({"result": "perfect"})
    if (sum < number):
        return jsonify({"result": "deficient"})
    return jsonify({"result": "abundant"})

@app.route('/lcm', methods=['POST'])
def lcm():
    data = request.get_json() 
    a = int(data.get("number1"))
    b = int(data.get("number2")) 
    if (a < 0 or b < 0):
        return jsonify({"result": "not defined for negative numbers"})
    if (a == 0 or b == 0):
        return jsonify({"result": str(0)})
    if (a >= b and a % b == 0):
        return jsonify({"result": str(a)}) 
    if (b >= a and b % a == 0):
        return jsonify({"result": str(b)}) 
    result = abs(a * b) // gcd(a, b)
    return jsonify({"result": str(result)})



if __name__ == '__main__':
    app.run(debug=True) 