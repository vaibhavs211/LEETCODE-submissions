class Solution {
public:
    string clearDigits(string s) {
        string s1 = "";
        for (char ch : s){
            if (ch>='0' && ch <= '9'){
                s1.pop_back();
            }
            else{
                s1 += ch;
            }
        }
        return s1;
    }
};