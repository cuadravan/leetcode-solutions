class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        map<int, int> futureIndex; // Index : Number
        int newIndex = 0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i] != 0){
                futureIndex[newIndex] = nums[i];
                nums[i] = 0;
                newIndex++;
            }
        }
        for(int i=0; i<newIndex; i++){
            nums[i] = futureIndex[i];
        }
    }
};