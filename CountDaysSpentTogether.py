class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        # I made a function to convert a string of "MM-DD" to an integer of how many days that date is from the start of the year
        # Note, no leap years
        # We note who arrives next, and who leaves first, since if the first person leaves before the second person arrives, they never meet
        # Otherwise, we subtract how many days the first person leaves first to when the second person arrives next to get how many days they meet
        # We add 1 since it is inclusive
        arriveAliceDays = self.stringToDayOfMonth(arriveAlice)
        leaveAliceDays = self.stringToDayOfMonth(leaveAlice)
        arriveBobDays = self.stringToDayOfMonth(arriveBob)
        leaveBobDays = self.stringToDayOfMonth(leaveBob)
        arriveFirst, arriveNext = (arriveAliceDays, arriveBobDays) if arriveAliceDays < arriveBobDays else (arriveBobDays, arriveAliceDays)
        leaveFirst, leaveNext = (leaveAliceDays, leaveBobDays) if leaveAliceDays < leaveBobDays else (leaveBobDays, leaveAliceDays)
        if(leaveFirst < arriveNext):
            return 0
        else:          
            days = leaveFirst - arriveNext + 1
            return days
    
    def stringToDayOfMonth (self, date):
        daysPerMonth = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        dayOfMonth = 0
        month, day = map(int, date.split('-'))
        if(month > 1):
            for month in range(1, month):
                dayOfMonth += daysPerMonth[month]
        return dayOfMonth + day
        