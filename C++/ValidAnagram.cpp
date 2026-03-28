class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        map<char, int> sCount;
        map<char, int> tCount;
        for(int i=0; i<s.size(); i++){
            if(sCount.contains(s[i])){
                sCount[s[i]]+=1;
            }
            else{
                sCount[s[i]]=1;
            }
        }
        for(int i=0; i<t.size(); i++){
            if(tCount.contains(t[i])){
                tCount[t[i]]+=1;
            }
            else{
                tCount[t[i]]=1;
            }
        }
        return (sCount == tCount);
    }
};