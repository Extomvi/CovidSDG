from flask import Flask, request, jsonify
#from estimator import impact
from trial import severeImpact

import json

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/<name>")
def hello(name):
    return "Hello! This is a {}.".format(name) 

@app.route('/response', methods=['GET'])
def api_response():
   
   data = {
       region: {
           name: "Africa",
           avgAge: 19.7,
           avgDailyIncomeInUSD: 5,
           avgDailyIncomePopulation: 0.71
        },
       periodType: "days",
       timeToElapse: 58,
       reportedCases: 674,
       population: 66622705,
       totalHospitalBeds: 1380614
    }
   js = json.dumps(data)
   resp = severeImpact(js)
   return resp

if __name__ == "__main__":
#    impact()
    severeImpact()
    app.run(debug=True)