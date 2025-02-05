class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int diff = 0;
        vector<vector<char>> diff_ch;
        
        for (int i = 0; i < s1.length(); i++) {
            if (s1[i] != s2[i]) {
                diff++;
                diff_ch.push_back({s1[i], s2[i]});
            }
            if (diff > 2) {
                return false;
            }
        }
        
        if (diff == 0) {
            return true;
        } else if (diff == 2) {
            return (diff_ch[0][1] == diff_ch[1][0] && diff_ch[0][0] == diff_ch[1][1]);
        } else {
            return false;
        }
    }
};