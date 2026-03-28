class Solution {
    // The goal here is to check if the a num's addend is the one that matches the one we are currently checking
    // So at first loop, it will always fail the check (since we only have data for one number)
    // Then we subtract total with that num to get a possible addend
    // Then do subsequent checks for next num to check if it is the addend
    // We store the addend as the key since that is what we're checking
    // Then the index of the num that would pair with that addend is store
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> possibleAddends;
        for(int index=0; index<nums.size(); index++){
            if(possibleAddends.contains(nums[index])){
                // vector<int> returnResult;
                // returnResult.push_back(possibleAddends[nums[index]]);
                // returnResult.push_back(index);
                // return returnResult;
                return {possibleAddends[nums[index]], index};
            }
            int addend = target - nums[index];
            if(!possibleAddends.contains(addend)){
                possibleAddends[addend] = index;
            }
        }
        return {}; // Technically this is not possible as per LeetCode's testcases
    }
};