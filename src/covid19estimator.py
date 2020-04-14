import json
json_dictionary = {
"region": {
"name": "Africa",
"avgAge": 19.7, "avgDailyIncomeInUSD": 5, "avgDailyIncomePopulation": 0.71
    },
  "periodType": "days",
  "timeToElapse": 58,
  "reportedCases": 674,
  "population": 66622705,
  "totalHospitalBeds": 1380614
}
def covid19ImpactEstimator(dictionary):
    # [0]-name, [1]-avgAge, [2]-avgDailyIncomeInUSD, [3]-avgDailyIncomePopulation,
    # [4]-periodType, [5]-timeToElapse, [6]-reportedCases, [7]- population,
    # [8]-totalHospitalBeds
    extracted_lst = []
    for value in dictionary.values():
        if type(value) is dict:
            for s_value in value.values():
                extracted_lst.append(s_value)
        else:
            extracted_lst.append(value)
    return extracted_lst
print(covid19ImpactEstimator(json_dictionary))

class impact():
    reportedCases = covid19ImpactEstimator(json_dictionary)[5]
    periodType = covid19ImpactEstimator(json_dictionary)[4]


    def __init__(self):
        self.currentlyInfected = self.reportedCases * 10
        if covid19ImpactEstimator(json_dictionary)[4] == 'days':
            self.days = covid19ImpactEstimator(json_dictionary)[5]
            self.infectionByRequestedTime = self.currentlyInfected * (2**(self.days//3))
        elif covid19ImpactEstimator(json_dictionary)[4] == 'weeks':
            self.weeks = covid19ImpactEstimator(json_dictionary)[5] * 7
            self.currentlyInfected = self.currentlyInfected * (2**(self.weeks//3))
        elif covid19ImpactEstimator(json_dictionary)[4] == 'months':
            self.months = covid19ImpactEstimator(json_dictionary)[5] * 30
            self.currentlyInfected = self.currentlyInfected * (2**(self.months//3))

    def __str__(self):
        return "Currently Infected people are : {}".format(self.currentlyInfected)


new = impact()
print("Number of currently impacted cases are {} cases.".format(new.currentlyInfected))
print("Total cases by the requested time of 28 days would be: {} cases".format(new.infectionByRequestedTime))

class severeImpact(impact):
    def __init__(self):
        self.currentlyInfected = self.reportedCases * 50
        if covid19ImpactEstimator(json_dictionary)[4] == 'days':
            self.days = covid19ImpactEstimator(json_dictionary)[5]
            self.infectionByRequestedTime = self.currentlyInfected * (2**(self.days//3))
        elif covid19ImpactEstimator(json_dictionary)[4] == 'weeks':
            self.weeks = covid19ImpactEstimator(json_dictionary)[5] * 7
            self.currentlyInfected = self.currentlyInfected * (2**(self.weeks//3))
        elif covid19ImpactEstimator(json_dictionary)[4] == 'months':
            self.months = covid19ImpactEstimator(json_dictionary)[5] * 30
            self.currentlyInfected = self.currentlyInfected * (2**(self.months//3))

new1 = severeImpact()
print("Number of severely impacted cases are {} cases.".format(new1.currentlyInfected))
print("Total number of severe cases by the requested time of 28 days would be: {} cases".format(new1.infectionByRequestedTime))
