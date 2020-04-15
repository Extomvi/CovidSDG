import json
import pprint
#function for estimation
def estimator(data):
  
  reportedCases = int(data['reportedCases']) 
  
  if (data['periodType'] == 'weeks'):
    requestedTime = int(data['timeToElapse']) * 7
  elif (data['periodType'] == 'months'):
    requestedTime = int(data['timeToElapse']) * 30
  else:
    requestedTime = int(data['timeToElapse'])
  
  #IMPACT
  impact = { 'currentlyInfected' : int(reportedCases * 10)}
  
  impact.update({'infectionsByRequestedTime' : int(impact['currentlyInfected'] *
                                 (2 ** int(requestedTime/3)))})
  
  impact.update({'severeCasesByRequestedTime' : int(0.15 * 
                                 impact['infectionsByRequestedTime'])})

  impact.update({'hospitalBedsByRequestedTime' : int((0.35 * 
                                 (data['totalHospitalBeds']))- 
                                 impact['severeCasesByRequestedTime'])})

  impact.update({'casesForICUByRequestedTime' : int(0.05 * 
                             impact['infectionsByRequestedTime'])})
  
  impact.update({'casesForVentilatorsByRequestedTime' : int(0.02 * 
                             impact['infectionsByRequestedTime'])})

  impact.update({'dollarsInFlight' : int((impact['infectionsByRequestedTime']) *
                             (data['region']['avgDailyIncomePopulation']) * 
                             (data['region']['avgDailyIncomeInUSD']) / requestedTime)})
  
  
  #SEVERE IMPACT
  severeImpact = { 'currentlyInfected' : int(reportedCases * 50)}
  
  severeImpact.update({ 'infectionsByRequestedTime' : int(severeImpact['currentlyInfected'] *
                              (2 ** int(requestedTime/3)))})
  
  severeImpact.update({ 'severeCasesByRequestedTime' : int(0.15 * 
                              severeImpact['infectionsByRequestedTime'])})
  
  severeImpact.update({ 'hospitalBedsByRequestedTime' : int((0.35 * 
                              (data['totalHospitalBeds']))- 
                              severeImpact['severeCasesByRequestedTime']) })
  
  severeImpact.update({'casesForICUByRequestedTime' : int(0.05 * 
                              severeImpact['infectionsByRequestedTime'])})
  
  severeImpact.update({'casesForVentilatorsByRequestedTime' : int(0.02 * 
                              severeImpact['infectionsByRequestedTime'])})
  
  severeImpact.update({'dollarsInFlight' : int((severeImpact['infectionsByRequestedTime']) *
                              (data['region']['avgDailyIncomePopulation']) * 
                              (data['region']['avgDailyIncomeInUSD']) / requestedTime)})
  
  
  return {
            'data' : data,
            'impact': impact,
            'severeImpact' : severeImpact
          }

def main():

  input_data= {   
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
              }

  result = estimator(input_data)
  # print(result)
  pprint.pprint(result)

if __name__ == "__main__":
  main()
