#include <cmath>
class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {        
        if(arr.size()==2){
            return true;
        }
        sort(arr.begin(), arr.end());
        int difference = abs(arr[0] - arr[1]);
        for(int i=2; i<arr.size(); i++){
            if(abs(arr[i]-arr[i-1]) != difference){
                return false;
            }
        }
        return true;
    }
};