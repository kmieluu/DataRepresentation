#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

dogs = [
    {
        "breed":"Puddle",
        "age":2,
        "IKC Registered":"Yes",
        "price":400
    },
    {
        "breed":"Vizsla",
        "age":0.5,
        "IKC Registered":"Yes",
        "price":800
    },
    {
        "breed":"German Shepherd",
        "age":"2 months",
        "IKC Registered":"Yes",
        "price":2500
    }
]

@app.route('/dogs', methods=['GET'])
def get_dogs():
    return jsonify( {'dogs':dogs})
#curl -i http://localhost:5000/dogs


@app.route('/dogs/<string:breed>', methods =['GET'])
def get_dog(breed):
    foundDogs = list(filter(lambda t : t['breed'] == breed , dogs))
    if len(foundDogs) == 0:
        return jsonify( { 'dog' : '' }),204
    return jsonify( { 'dog' : foundDogs[0] })