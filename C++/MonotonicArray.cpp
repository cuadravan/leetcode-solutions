class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        if(nums.size() <= 2){
            return true;
        }
        bool initialized = false;
        bool isIncreasing = false;
        for(int i=1; i<nums.size(); i++){
            if(nums[i-1] == nums[i]){
                continue;
            }
            else if(nums[i-1] < nums[i]){
                if(initialized){
                    if(isIncreasing)
                        continue;
                    else
                        return false;
                }
                else{
                    isIncreasing = true;
                    initialized = true;
                }
            }
            else{
                if(initialized){
                    if(isIncreasing)
                        return false;
                    else
                        continue;
                }
                else{
                    isIncreasing = false;
                    initialized = true;
                }
            }
        }
        return true;
    }
};