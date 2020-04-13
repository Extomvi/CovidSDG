from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
   return jsonify({
       'author': 'Vivek Singh Bhadauria',
       'author_url': 'http://viveksb007.wordpress.com/',
       'base_url': 'zeolearn.com/',
       'endpoints': {
           'Returns URLS of images': '/magazines/photos/{number of photos}',
       }
   })

@app.route('/check', methods=['GET', 'POST', 'PUT', 'DELETE'])
def check():
   if request.method == 'GET':
       return "REQUEST TYPE: GET"

   elif request.method == 'POST':
       return "REQUEST TYPE: POST"

   elif request.method == 'PUT':
       return "REQUEST TYPE: PUT"

   elif request.method == 'DELETE':
       return "REQUEST TYPE: DELETE"

@app.route('/response', methods=['GET'])
def api_response():
   data = {
       'data': 'test data',
       'id': 1
   }
   js = json.dumps(data)
   resp = Response(js, status=200, mimetype='application/json')
   return resp


@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
   app.run(debug=True)