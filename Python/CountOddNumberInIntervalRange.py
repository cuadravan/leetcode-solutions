class Solution:
    def countOdds(self, low: int, high: int) -> int:
        rangeInt = high - low + 1
        evenLowCheck = low%2
        evenHighCheck = high%2
        oddCount = rangeInt // 2
        if(evenLowCheck == evenHighCheck and evenLowCheck != 0):
            oddCount += 1
        return oddCount
        #If there are an even number in a range, then oddCount = evenCount
        #There can only be even number if low and high have different parity
        #So we divide by 2
        #If there is an odd number in a range, then it depends
        #An odd number in a range can only happen when low and high have same parity
        #If odd, just do an integer divide by 2, then add 1
        #If even, do an integer divide by 2
        #This works because if both start and finish are odd
        #Then it is 1 step away from becoming an even-numbered range
        #But that 1 step away is an even number, hence, treat it as if half of them are odd
        # But since int division floors it, offset the floor
        #If it is even, it is 1 step away from becoming even-numbered range but the step is even
        #Hence, just half-1 is the odd count, but int division already floors it 