class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if(len(arr)<=2):
            return True
        difference = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if(arr[i]-arr[i-1] != difference):
                return False
        return True
        # Firstly, we sort to make things easier
        # Then we get the difference (from first 2 numbers) that should be command for every consecutive number
        # Starting from the second element, we check that difference
        # If ever the difference is not the same, we cannot make the arithmetic progression