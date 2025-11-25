class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        # Very simple, we check 11th and 12th letter in the list of strings if its integer equivalent is above 60
        # If so, we add 1 to the count of seniors
        count = 0
        for passenger in range(len(details)):
            age = int(details[passenger][11] + details[passenger][12])
            if age > 60:
                count += 1
        return count