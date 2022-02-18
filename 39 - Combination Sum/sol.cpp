#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
ifstream fin("input", ifstream::in);
ofstream fout("output", ifstream::out);

bool exist[500] = {};
vector<vector<int>> ans;
void dfs(vector<int>& candidates, int target, vector<int> &comb, int index=0) {
    if (target < 0) return;
    if (target == 0) {
        ans.push_back(comb);
        return;
    }
    exist[target] = true;
    for (int i = index ; i < candidates.size() ; i ++) {
        comb.push_back(candidates[i]);
        dfs(candidates, target-candidates[i], comb, i);
        comb.pop_back();
    }
    
}
vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    
    vector<int> comb;
    dfs(candidates, target, comb);
    
    return ans;
}

int main() {
    int n, target;
    while(fin >> n) {
        vector<int> candidates(n);
        for (int i = 0 ; i < n ; i ++)
            fin >> candidates[i];
        fin >> target;
        vector<vector<int>> ans;
        ans = combinationSum(candidates, target);
        for (int i = 0 ; i < ans.size() ; i ++) {
            for (int j = 0 ; j < ans[i].size() ; j ++)
                fout << ans[i][j] << ' ';
            fout << endl;
        }


    }
    return 0;
}