#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
using namespace std;
ifstream fin("input", ifstream::in);
ofstream fout("output", ifstream::out);

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int len = nums.size(), n = pow(2, len);
        vector<vector<int>> subsets(n);
        int jump = 1;
        bool flag = false;
        for (int i = 0 ; i < len ; i ++) {
            for (int j = 0 ; j < n ; j ++) {
                if (flag)
                    subsets[j].push_back(nums[i]);
                if (j % jump == 0)
                    flag ^= true; 
            }
            jump *=2;
        }
        return subsets;
    }
};

int main() {
    int n;
    while(fin >> n) {
        vector<int> nums(n);
        for (int i = 0 ; i < n ; i ++)
            fin >> nums[i];
        Solution *sol = new Solution();
        vector<vector<int>> ans = sol->subsets(nums);
        for (int i = 0 ; i < ans.size() ; i ++) {
            for (int j = 0 ; j < ans[i].size() ; j ++)
                fout << ans[i][j] << ' ';
            fout << endl;
        }

    }
    return 0;
}