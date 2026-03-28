class Solution {
public:
    char findTheDifference(string s, string t) {
        map<char, int> letterCountInFirstString;
        // Loop through first string and get the count of each character
        for(int i=0; i<s.size(); i++){
            if(letterCountInFirstString.find(s[i]) == letterCountInFirstString.end()){
                letterCountInFirstString[s[i]] = 1;
            }else{
                letterCountInFirstString[s[i]] += 1;
            }
        }
        // Loop through second string, if found, we subtract by 1, but if already 0, return the character
        // Or return character if it is not found
        for(int i=0; i<t.size(); i++){
            if(letterCountInFirstString.find(t[i]) != letterCountInFirstString.end()){
                if(letterCountInFirstString[t[i]] == 0){
                    return t[i];
                }
                letterCountInFirstString[t[i]] -= 1;
            }
            else{
                return t[i];
            }
        }
        return '\0';
    }
};