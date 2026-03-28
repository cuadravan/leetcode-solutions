class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int size = (word1.size() < word2.size()) ? word1.size() : word2.size();
        string merged;
        for(int i = 0; i<size; i++){
            merged.push_back(word1[i]);
            merged.push_back(word2[i]);
        }
        if(word1.size() > word2.size()){
            merged.append(word1.substr(word2.size())); // Append the substring of word1 starting at word2.size(); basically left over of word1 is it is longer than word2
        }else{       
            merged.append(word2.substr(word1.size())); // Opposite of the previous
        }

        return merged;
    }
};