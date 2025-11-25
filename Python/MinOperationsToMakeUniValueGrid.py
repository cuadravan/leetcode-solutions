class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # The goal here is to find the minimum number of operations to add/subtract x from the elements of a grid to make all values uniform
        # Theoretically, the median should be the ideal target for the univalue grid since it is in the middle
        # Hence, we make the 2D list into 1D and sort to find median
        # Then we get the remainder of median divided by x, because if ever any other element divided with x has a remainder that is not the same, then it is impossible to make all elements uniform
        # Why? If two values have the same remainder when divided with x, then adding/subtracting x repeatedly will eventually make them equal
        # The remainder is something that adding/subtracting x can never change, so they need to be equal
        # For example 3 and 9, if x = 3, remainder of both is 0, so if we add 3 to 3 and subtract 3 from 9, they both become 6
        # Another example, 4 and 10, if x = 3, remainder of both is 1, so if we add 3 to 4 and subtract 3 from 10, they both become 7
        # The remainder is something that is never changed, so if it is equal, then they are bound to become equal even if it takes a lot of operations

        # First, we turn the 2D list into a 1D list
        flatList = []
        for row in grid:
            flatList.extend(row)
        # Then we sort that
        flatList.sort()
        # We get the median of the sorted 1D list
        median = flatList[len(flatList)/2]
        # We find the remainded if the median is divided with x
        remainder = median % x
        operationCount = 0
        # We loop through the flatlist
        for i in range(len(flatList)):
            if(flatList[i] == median): # Excluding the median of course since it is our target number
                continue
            if(flatList[i] % x == remainder): # If the remainders are equal
                difference = median - flatList[i] # First get the absolute difference between median and the number
                operationCount += (abs(difference) / x) # Then divide it by x, this will yield how many operations of addition or subtraction are needed to remove this difference (it is absolute so sign does not matter)
                # Also note, it will always yield an integer because we know they have the same remainder, so the difference between them will always be divisible by x
            else: # If not then return -1, meaning it is impossible to make the grid into uni-value
                return -1
        return operationCount
            

        