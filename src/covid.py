class covid19ImpactEstimator:
    reportedCases = int(input("Please input the reported cases: "))
    def _init_(self):
        pass
    def _str_(self):
        return '{}'.format(self.reportedCases)
class impact(covid19ImpactEstimator):
    #The superclass for this impact class is covid19ImpactEstimator
    #inherits from the covid19ImpactEstimator class but overwrites the returned string
    """This checks the impact of the reported Cases"""
    def _init_(self):
        self.currentlyInfected = self.reportedCases * 10
    def _str_(self):
        return "Currently Infected people are : {}".format(self.currentlyInfected)

    #what i want to start working on
    '''def infectionByRequestedTime(self, days, weeks, months):
        self.days = days
        self.weeks = weeks
        self.months = months'''
class severeImpact(impact):
    #The superclass for this severeImpact class is the impact class
    #Inherits from the impact class but overwrites the _init_  of the superclass (impact)
    def _init_(self):
        #overwrites the _init_ method of the impact class for the self.currentlyInfected calculation
        self.currentlyInfected = self.reportedCases * 50

    def _str_(self):
        return "Currently Severely Infected people are : {}".format(self.currentlyInfected)
new = severeImpact()
print(new.currentlyInfected)
