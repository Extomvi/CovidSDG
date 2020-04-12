class covid19ImpactEstimator:
      pass
#      return currentlyInfected

class impact(covid19ImpactEstimator):
      reportedCases = input("To calculate for the impact, " + "\nTotal Reported Cases :")
      reportedCases = int(reportedCases)
      currentlyInfected = reportedCases*10
      infectionByRequestTime = currentlyInfected*512 #for predicting towards the next 28 days with the rate doubling in every 3 days
print("Number of currently impacted cases are {} cases.".format(impact.currentlyInfected))

class severeImpact(covid19ImpactEstimator):
      reportedCases = input("To calculate for severe impact, " + "\nTotal Reported Cases :")
      reportedCases = int(reportedCases)
      currentlyInfected = reportedCases*50
      infectionByRequestTime = currentlyInfected*512 #for predicting towards the next 28 days with the rate doubling in every 3 days
      def duration(self, days, weeks, months):
            self.days = days
            days = input("How many days: ")
            self.weeks = weeks
            weeks = input("How many weeks: ")
            self.months = months
            months = input("How many months: ")
            for days, weeks, months in self.days,self.weeks,self.months:
                  if months == 1:
                        days = 30
                        weeks = 4
                  elif months >= 2:
                        days = 30*months
                        weeks = 4*months
                  elif weeks == 1:
                        days = 7
                  elif weeks >= 2:
                        days = 7*weeks
            return days

#      return currentlyInfected

print("Total number of severe impact are {} cases.".format(severeImpact.currentlyInfected))

            
#      infectionByRequestedTime = currentlyInfected* (2**day)


'''
def estimator(data):
    return data
'''