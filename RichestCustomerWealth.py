class Solution(object):
    def maximumWealth(self, accounts):
        max = 0
        tempMax = 0
        for account in accounts:
            for money in account:
                tempMax += money
            if(tempMax > max):
                max = tempMax
            tempMax = 0
        return max