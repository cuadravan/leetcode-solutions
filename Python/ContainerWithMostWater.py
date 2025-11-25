class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # The thing to note here is that
        # The biggest possible area will come from the farthest element
        # So start checking from the farthest (first and last)
        # Additionally, the highest possible height can only come from the bigger element
        # So to check at next step (meaning we shrink the width by 1), always move the smaller element
        # Why? We want to reduce the possible loss but also maintain possible gains
        # The bigger element is always a possible gain, the next element after the smaller element may be bigger or smaller
        # But the max possible value we can get from it will always come from the bigger element
        max = 0
        firstPointer = 0
        lastPointer = len(height) - 1
        while(lastPointer > firstPointer):
            temp = min(height[firstPointer], height[lastPointer]) * (lastPointer - firstPointer)
            max = temp if (temp > max) else max
            if height[lastPointer] <= height[firstPointer]:
                lastPointer -= 1
            elif height[firstPointer] < height[lastPointer]:
                firstPointer += 1
        return max