class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key = lambda x:x[0]) # Note that intervals have 2 elements, but we only need to sort the first one
        # Our goal here is if two intervals are intersecting, they must be combined
        # By having it sorted, we only need to traverse through the list of intervals once
        mergedIntervals = []
        outerPointer = 0 # This keeps track of the index within the merged intervals list
        mergedIntervals.append(intervals[0]) # Add the first interval
        for index in range(1, len(intervals)): # Traverse starting from second interval || crucial to note that index keeps track within the list of intervals we have yet to merge
            if(mergedIntervals[outerPointer][1] >= intervals[index][0]): #If the rightPoint of the previously added mergedInterval is greater than the leftPoint of the notYetAddedInterval, meaning they intersect
                # We expand the previously added Interval's right point with whichever of the two interval's right points is bigger, thus mergingn them
                mergedIntervals[outerPointer][1] = max(intervals[index][1], mergedIntervals[outerPointer][1])
            else: # If they don't intersect, we now know the previously added interval can no longer merge (we know this because of our sort)
                mergedIntervals.append(intervals[index]) # We added the non-conflicting interval
                outerPointer += 1 # Now we properly point to the newly added interval in the merged intervals list
        return mergedIntervals