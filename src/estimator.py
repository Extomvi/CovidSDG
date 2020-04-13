class covid19ImpactEstimator:
    reportedCases = input("This is for COVID19 Estimation." + "\nPress ENTER to Proceed")
    """This checks the impact of the reported Cases"""

    def _init_(self):
        reportedCases = int(input("Please input the number of reportedCases: "))
        self.reportedCases = reportedCases
        self.currentlyInfected = reportedCases * 10

    def _str_(self):
        return "currently Infected people are : {}".format(self.currentlyInfected)

#new = covid19ImpactEstimator()
#print(new.currentlyInfected)

class impact(covid19ImpactEstimator):
#      reportedCases = input("To calculate for the impact, " + "\nTotal Reported Cases :")
#      reportedCases = int(reportedCases)
      reportedCases = int(input("Please input the number of reportedCases: "))
      currentlyInfected = reportedCases*10
      infectionByRequestTime = currentlyInfected*512 #for predicting towards the next 28 days with the rate doubling in every 3 days
new = impact()
print("Number of currently impacted cases are {} cases.".format(new.currentlyInfected))
print("Total cases by the requested date of 28 days would be: {} cases".format(new.infectionByRequestTime))

            

'''
def estimator(data):
    return data
'''