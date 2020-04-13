class covid19ImpactEstimator:
      pass
#      return currentlyInfected

class impact(covid19ImpactEstimator):
      reportedCases = input("To calculate for the impact, " + "\nTotal Reported Cases :")
      reportedCases = int(reportedCases)
      currentlyInfected = reportedCases*10
      infectionByRequestTime = currentlyInfected*512 #for predicting towards the next 28 days with the rate doubling in every 3 days
print("Number of currently impacted cases are {} cases.".format(impact.currentlyInfected))


            

'''
def estimator(data):
    return data
'''