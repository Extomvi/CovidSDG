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

print("Data for input is: {}.".format(covid19ImpactEstimator(full_dictionary)))


class impact():
    reportedCases = covid19ImpactEstimator(full_dictionary)[0][5]
    periodType = covid19ImpactEstimator(full_dictionary)[0][4]


    def __init__(self):
        self.currentlyInfected = self.reportedCases * 10
        if covid19ImpactEstimator(full_dictionary)[0][4] == 'days':
            self.days = covid19ImpactEstimator(full_dictionary)[0][5]
            self.infectionsByRequestedTime = self.currentlyInfected * (2**(self.days//3))
        elif covid19ImpactEstimator(full_dictionary)[0][4] == 'weeks':
            self.weeks = covid19ImpactEstimator(full_dictionary)[0][5] * 7
            self.currentlyInfected = self.currentlyInfected * (2**(self.weeks//3))
        elif covid19ImpactEstimator(full_dictionary)[0][4] == 'months':
            self.months = covid19ImpactEstimator(full_dictionary)[0][5] * 30
            self.currentlyInfected = self.currentlyInfected * (2**(self.months//3))

        self.severeCasesByRequestedTime = 0.15 * self.infectionsByRequestedTime
        self.totalHospitalBeds = covid19ImpactEstimator(full_dictionary)[0][8]
        self.hospitalBedsByRequestedTime = int((0.65 * 0.95 * self.totalHospitalBeds) - self.severeCasesByRequestedTime)

        # computing the total number of available beds using this formula
    def __str__(self):
        return "data: {}, currentlyInfected: {}".format(full_dictionary,self.currentlyInfected)


new = impact()
'''
print("\nNumber of currently impacted cases are {} cases.".format(new.currentlyInfected))
print("\nTotal number of severe cases by the requested time of 28 days would be: {} cases".format(new.infectionsByRequestedTime))
print("\nSevere cases by requested time would be {}.".format(new.severeCasesByRequestedTime))
print("\nHospital Beds by Requested time would be: {}.".format(new.hospitalBedsByRequestedTime))
'''
print("\nData for impact would be: {}.".format(new))


class severeImpact(impact):
    def __init__(self):
        self.currentlyInfected = self.reportedCases * 50
        if covid19ImpactEstimator(full_dictionary)[0][4] == 'days':
            self.days = covid19ImpactEstimator(full_dictionary)[0][5]
            self.infectionsByRequestedTime = self.currentlyInfected * (2**(self.days//3))
        elif covid19ImpactEstimator(full_dictionary)[0][4] == 'weeks':
            self.weeks = covid19ImpactEstimator(full_dictionary)[0][5] * 7
            self.currentlyInfected = self.currentlyInfected * (2**(self.weeks//3))
        elif covid19ImpactEstimator(full_dictionary)[0][4] == 'months':
            self.months = covid19ImpactEstimator(full_dictionary)[0][5] * 30
            self.currentlyInfected = self.currentlyInfected * (2**(self.months//3))

        self.severeCasesByRequestedTime = 0.15 * self.infectionsByRequestedTime
        self.totalHospitalBeds = covid19ImpactEstimator(full_dictionary)[0][8]
        self.hospitalBedsByRequestedTime = int((0.65 * 0.95 * self.totalHospitalBeds) - self.severeCasesByRequestedTime)

new1 = severeImpact()
'''
print("\nNumber of severely impacted cases are {} cases.".format(new1.currentlyInfected))
print("\nTotal number of severe cases by the requested time of 28 days would be: {} cases".format(new1.infectionsByRequestedTime))
print("\nSevere cases by requested time would be {}.".format(new1.severeCasesByRequestedTime))
print("\nHospital Beds by Requested time would be: {}.".format(new1.hospitalBedsByRequestedTime))
'''
print("\nData for severe impact would be: {}.".format(new1))

