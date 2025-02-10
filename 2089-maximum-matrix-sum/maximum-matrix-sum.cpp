#include<math.h>
class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        int sm = INT_MAX;
        int neg = 0;
        long long sum = 0;
        int n = matrix.size();
        for (int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if (matrix[i][j]<0){
                    neg++;
                }
                if (abs(matrix[i][j]) < sm){
                    sm = abs(matrix[i][j]);
                }
                sum += abs(matrix[i][j]);
            }
        }
        return neg % 2 == 0 ? sum : sum - 2*sm;
    }
};