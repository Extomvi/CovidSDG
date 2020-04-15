from flask import Flask, request, jsonify
from flask_restful import Resource, Api 
from estimator import estimator
import json


app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route('/', methods=['GET'])
def hello():
    return "<h1>Welcome to my covid19-estimator application</h1>"

new = estimator({   
              'region': {       
                'name': "Africa",       
                'avgAge': 19.7,       
                'avgDailyIncomeInUSD': 5,       
                'avgDailyIncomePopulation': 0.71     
                },   
              'periodType': "days",   
              'timeToElapse': 58,   
              'reportedCases': 373,   
              'population': 66622705,   
              'totalHospitalBeds': 1380614 
              })

if __name__ == "__main__":
    estimator(new)
    app.run(debug=True)