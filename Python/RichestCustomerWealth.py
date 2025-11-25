class Solution(object):
    def maximumWealth(self, accounts):
        max = 0
        tempMax = 0
        # Also another simple problem, we traverse each row (account) and get each row's total (money)
        # Keep a max variable for tracing max value and keep checking for each row
        for account in accounts:
            for money in account:
                tempMax += money
            if(tempMax > max):
                max = tempMax
            tempMax = 0
        return max