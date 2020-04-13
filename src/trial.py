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
        elif months >= 0:
            days = months*0 + weeks*7 + days
        infectionByRequestTime = currentlyInfected* 512 #28days
        day = days//3
        pwr = 2**day
        infectionByRequestTime= currentlyInfected*pwr

        return "Currently Infected is {} cases.".format(currentlyInfected), "and the rate of cases by the inputed period of {} days would be: {} cases".format(days,infectionByRequestTime)



#        return "Currently Infected is {} cases.".format(currentlyInfected, "Rate of cases by the inputed period of {} days would be: {} cases".format(days,infectionByRequestTime)