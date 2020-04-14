import json
#print(2900 * (2**(58//3))) #checking mathematical computation in code
full_dictionary = {"data": {
"region": {
"name": "Africa",
"avgAge": 19.7, "avgDailyIncomeInUSD": 5, "avgDailyIncomePopulation": 0.71
    },
  "periodType": "days",
  "timeToElapse": 58,
  "reportedCases": 674,
  "population": 66622705,
  "totalHospitalBeds": 1380614
},
"estimate": {"impact":{
"currentlyInfected": 27470,
"infectionByRequestedTime": 112517120,
"severeCasesByRequestedTime": 16877568,
"hospitalBedsByRequestedTime": -168639962,
"casesForICUByRequestedTime": 5625856,
"casesForVentilatorsByRequestedTime": 2250342,
"dollarsInFlight": 12484899635.2
},
"severImpact": {
"currentlyInfected": 137350,
"infectionByRequestedTime": 562585600,
"severeCasesByRequestedTime":84387840,
"hospitalBedsByRequestedTime": -84150234,
"casesForICUByRequestedTime": 28129280,
"casesForVentilatorsByRequestedTime": 11251712,
"dollarsInFlight": 62424498176
}

}
}


def covid19ImpactEstimator(dictionary):
    #first_lst is to extract the dictionary for the first challenge
    first_lst = [dictionary[key] for key in full_dictionary.keys()][0]
    # For the first_lst :
    # [0][0]-name, [0][1]-avgAge, [0][2]-avgDailyIncomeInUSD, [0][3]-avgDailyIncomePopulation,
    # [0][4]-periodType, [0][5]-timeToElapse, [0][6]-reportedCases, [0][7]- population,
    # [0][8]-totalHospitalBeds

    second_lst_tentaive = [full_dictionary[key] for key in full_dictionary.keys()][1]
    second_lst = [value[key] for value in second_lst_tentaive.values() for key in value]
    #For the second_lst :
        # For impact:
            # [1][0]- currentlyInfected, [1][1]- infectionByRequestedTime,
            # [1][2]- severeCasesByRequestedTime [1][3]- hospitalBedsByRequestedTime,
            # [1][4]- casesForICUByRequestedTime [1][5]- casesForVentilatorsByRequestedTime
            # [1][6] - dollarsInFlight
        # For severe impact :
            # [1][7]- currentlyInfected, [1][8]- infectionByRequestedTime,
            # [1][9]- severeCasesByRequestedTime [1][10]- hospitalBedsByRequestedTime,
            # [1][11]- casesForICUByRequestedTime [1][12]- casesForVentilatorsByRequestedTime
            # [1][13] - dollarsInFlight


    extracted_lst = []
    for value in first_lst.values():
        if type(value) is dict:
            for s_value in value.values():
                extracted_lst.append(s_value)
        else:
            extracted_lst.append(value)
    return extracted_lst, second_lst
    #This returns a list of tuples

#print(covid19ImpactEstimator(full_dictionary))


class impact():
    """ To compute for the impact """
    # These instance variables are similar to both of the classes
    # So instead of calling it everytime in the class, I have decided to call them here
    reportedCases = covid19ImpactEstimator(full_dictionary)[0][6]
    periodType = covid19ImpactEstimator(full_dictionary)[0][4]
    timeToElapse = covid19ImpactEstimator(full_dictionary)[0][5]
    totalHospitalBeds = covid19ImpactEstimator(full_dictionary)[0][8]
    avgDailyIncomeInUSD = covid19ImpactEstimator(full_dictionary)[0][2]
    avgDailyIncomePopulation = covid19ImpactEstimator(full_dictionary)[0][3]



    def __init__(self):
        self.currentlyInfected = self.reportedCases * 10
        if self.periodType == 'days':
            self.infectionsByRequestedTime = self.currentlyInfected * (2 **(self.timeToElapse//3))
        elif self.periodType == 'weeks':
            self.infectionByRequestTime = self.currentlyInfected * ( 2 ** ((self.timeToElapse * 7)//3))
        elif self.periodType == 'months':
            self.infectionsByRequestedTime = self.currentlyInfected * (2 ** ((self.timeToElapse * 30)//3))

        self.severeCasesByRequestedTime = 0.15 * self.infectionsByRequestedTime
        self.hospitalBedsByRequestedTime = int((0.35 * 0.95 * self.totalHospitalBeds) - self.severeCasesByRequestedTime)
        self.casesForICUByRequestedTime = 0.05 * self.infectionsByRequestedTime
        self.casesForVentilatorsByRequestedTime = 0.02 * self.infectionsByRequestedTime
        self.dollarsInFlight = self.infectionsByRequestedTime * self.avgDailyIncomePopulation * self.avgDailyIncomeInUSD * self.timeToElapse

    def __str__(self):
        return "impact: [ currentlyInfected : {}, infectionsByRequestedTime: {}, severeCasesByRequestedTime: {}, hospitalBedsByRequestedTime : {}, casesForICUByRequestedTime: {}, casesForVentilatorsByRequestedTime: {} ]".format(self.currentlyInfected, self.infectionsByRequestedTime, self.severeCasesByRequestedTime, self.hospitalBedsByRequestedTime, self.casesForICUByRequestedTime, self.casesForVentilatorsByRequestedTime)

# For Debugging
'''new = impact()
print(new.currentlyInfected)
print(new.infectionsByRequestedTime)
print(new.severeCasesByRequestedTime)
print(new)
print(new.hospitalBedsByRequestedTime)
print(new.dollarsInFlight)'''

class severeImpact(impact):
    """ To compute for severe impact parallel to the impact class """
    # This class inherits from the impact class
    def __init__(self):
        self.currentlyInfected = self.reportedCases * 50
        if self.periodType == 'days':
            self.infectionsByRequestedTime = self.currentlyInfected * (2 **(self.timeToElapse//3))
        elif self.periodType == 'weeks':
            self.infectionByRequestTime = self.currentlyInfected * ( 2 ** ((self.timeToElapse * 7)//3))
        elif self.periodType == 'months':
            self.infectionsByRequestedTime = self.currentlyInfected * (2 ** ((self.timeToElapse * 30)//3))

        self.severeCasesByRequestedTime = 0.15 * self.infectionsByRequestedTime
        self.hospitalBedsByRequestedTime = int((0.35 * 0.95 * self.totalHospitalBeds) - self.severeCasesByRequestedTime)
        self.casesForICUByRequestedTime = 0.05 * self.infectionsByRequestedTime
        self.casesForVentilatorsByRequestedTime = 0.02 * self.infectionsByRequestedTime
        self.dollarsInFlight = self.infectionsByRequestedTime * self.avgDailyIncomePopulation * self.avgDailyIncomeInUSD * self.timeToElapse

    def __str__(self):
        #This does not contain the 'data' output in comaparsion to the __str__ output of the impact class
        return "severeImpact: [ currentlyInfected : {}, infectionsByRequestedTime: {}, severeCasesByRequestedTime: {}, hospitalBedsByRequestedTime : {}, casesForICUByRequestedTime: {}, casesForVentilatorsByRequestedTime: {} ]".format(self.currentlyInfected, self.infectionsByRequestedTime, self.severeCasesByRequestedTime, self.hospitalBedsByRequestedTime, self.casesForICUByRequestedTime, self.casesForVentilatorsByRequestedTime)

# For Debugging
'''new1 = severeImpact()
print(new1.currentlyInfected)
print(new1.infectionsByRequestedTime)
print(new1.severeCasesByRequestedTime)
print(new1)
print(new1.hospitalBedsByRequestedTime)
print(new1.dollarsInFlight)'''

# Concerning The Output of the class required which is:
'''
    data: {}, // This is in the __str__ method
    impact: {},
    severeImpact: {}
'''
new = covid19ImpactEstimator(full_dictionary)
impact_output = impact()
severeImpact_output = severeImpact()
print(new)
print("\n{} ".format(impact_output))
print("\n{} ".format(severeImpact_output))
