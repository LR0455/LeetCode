#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
ifstream fin("input", ifstream::in);
ofstream fout("output", ifstream::out);

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int len = nums.size();
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        
        //   a+b+c+d = target
        //-> a+b = target-(c+d)
        //-> find all two pair O(n^2)
        map<int, vector<pair<int, int>>> pairs;
        for (int i = 0 ; i < len ; i ++)
            for (int j = i+1 ; j < len ; j ++)
                // key -> a+b, val = (a_index,b_index)
                pairs[nums[i]+nums[j]].push_back(pair<int, int>(i, j));
        
        for (int i = 0 ; i < len ; i ++) {
            if (i > 0 && nums[i-1] == nums[i]) continue;
            for (int j = i+1 ; j < len ; j ++) {
                // if nums[j-1] == nums[j] and answer is exist -> must cause duplicates
                // ex: [-5,0,0,1,4], 0 -> [-5,0,1,4] is duplicates
                if (j > i+1 && nums[j-1] == nums[j]) continue;
                int cd = target - nums[i] - nums[j];
                // cd is exist = key is found
                if (pairs.find(cd) != pairs.end())
                    for (auto p:pairs[cd]) {
                        int ai = i, bi = j;
                        int ci = p.first, di = p.second;
                        // index must: a<b<c<d
                        if (bi < ci) {
                            vector<int> tmp = {nums[ai], nums[bi], nums[ci], nums[di]};
                            // remove duplicates
                            if (ans.size() > 0 && tmp == ans.back()) continue;
                            ans.push_back(tmp);
                        }
                    }       
            }
        }
        
        return ans;
    }
};

int main() {
    int n, target;
    while(fin >> n) {
        vector<int> nums(n);
        for (int i = 0 ; i < n ; i ++)
            fin >> nums[i];
        fin >> target;
        Solution *sol = new Solution();
        vector<vector<int>> ans = sol->fourSum(nums, target);

        for (int i = 0 ; i < ans.size() ; i ++) {
            for (int j = 0 ; j < ans[i].size() ; j ++) {
                if (j) fout << ',';
                fout << ans[i][j];
            }
            fout << endl;
        }

    }
    return 0;
}