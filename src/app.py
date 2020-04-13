from flask import Flask, request, jsonify
from flask_restful import Resource, Api 
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

@app.route('/<function>', methods=['GET'])
def hello(function):
    return "Hello! This is a {}.".format(function) 
'''
@app.route('/', methods=['GET'])
class severeImpact:
    def __init__(self):
        pass
#        self.reportedCases = reportedCases
        
    def currentlyInfected(self,days,weeks,months):
        reportedCases = int(input("Reported cases: "))
        currentlyInfected = reportedCases*50
        infectionByRequestTime = currentlyInfected*512
        infectionByRequestTime = int(infectionByRequestTime)
        print("Input number of days to see the projected no of cases...")
        months = int(input("How many months: "))
        days = int(input("How many days: "))
        weeks = int(input("How many weeks: "))
        if months != 1:
            days = months*30 + days + weeks*7
            weeks = months*4 + weeks
            if weeks >= 1:
                days = weeks*7 + days
        elif months == 1:
            days = months*30 + weeks*7 +days
        infectionByRequestTime = currentlyInfected* 512 #28days
        days = days//3
        pwr = 2**days
        infectionByRequestTime= currentlyInfected*pwr

        return "Currently Infected is {} cases.".format(currentlyInfected), "and the rate of cases by the inputed period of {} days would be: {} cases".format(days,infectionByRequestTime)
'''

if __name__ == "__main__":
#    impact()
#    severeImpact.currentlyInfected(1,1,1,1)
    app.run(debug=True)