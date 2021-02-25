#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

dogs = [
    {
        "breed":"Puddle",
        "age":2,
        "IKC Registered":"No",
        "price":200
    },
    {
        "breed":"Vizsla",
        "age":0.5,
        "IKC Registered":"Yes",
        "price":2000
    },
    {
        "breed":"German Shepherd",
        "age":"2 months",
        "IKC Registered":"No",
        "price":700
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
#curl -i http://localhost:5000/dogs/test

@app.route('/dogs', methods=['POST'])
def create_dog():
    if not request.json:
        abort(400)
    if not 'dog' in request.json:
        abort(400)
    dog={
        "breed":  request.json['breed'],
        "age": request.json['age'],
        "IKC registeded":request.json['model'],
        "price":request.json['price']
    }
    dogs.append(dog)
    return jsonify( {'dog':dog }),201
# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"reg":"12 D 1234","make":"Fiat","model":"Punto","price":3000}' http://localhost:5000/cars
# for windows use this one
# curl -i -H "Content-Type:application/json" -X POST -d "{\"reg\":\"12 D 1234\",\"make\":\"Fiat\",\"model\":\"Punto\",\"price\":3000}" http://localhost:5000/cars
@app.route('/dogs/<string:breed>', methods =['PUT'])
def update_dog(breed):
    foundDogs=list(filter(lambda t : t['breed'] ==breed, dogs))
    if len(foundDogs) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'age' in request.json and type(request.json['age']) != str:
        abort(400)
    if 'IKC registered' in request.json and type(request.json['IKC registered']) is not str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not int:
        abort(400)
    foundDogs[0]['age']  = request.json.get('age', foundDogs[0]['age'])
    foundDogs[0]['IKC registered'] =request.json.get('IKC registered', foundDogs[0]['IKC registered'])
    foundDogs[0]['price'] =request.json.get('price', foundDogs[0]['price'])
    return jsonify( {'dog':foundDogs[0]})
#curl -i -H "Content-Type:application/json" -X PUT -d '{"make":"Fiesta"}' http://localhost:5000/cars/181%20G%201234
# for windows use this one
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"Fiesta\"}" http://localhost:5000/cars/181%20G%201234

@app.route('/dogs/<string:breed>', methods =['DELETE'])
def delete_dog(breed):
    foundDogs = list(filter (lambda t : t['breed'] == breed, dogs))
    if len(foundDogs) == 0:
        abort(404)
    dogs.remove(foundDogs[0])
    return  jsonify( { 'result':True })

@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)