class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        # First we iterate through items1, storing them in dictionary where value:weight
        weightDict = {}
        for index, item in enumerate(items1):
            weightDict[item[0]] = item[1]
        # Then iterate through items1, if value is not yet in dictionary, just add it as is
        # If it already is, just add the weights since they have same value
        for index, item in enumerate(items2):
            if item[0] not in weightDict:
                weightDict[item[0]] = item[1]
            else:
                weightDict[item[0]] += item[1]
        # Get the list of keys and sort them
        dictKeys = list(weightDict.keys())
        dictKeys.sort()
        # Then make a new 2D list where each elements is the value and its new weight. This is now in ascending order
        merge = [[int(keys),int(weightDict[keys])] for keys in dictKeys]

        return merge