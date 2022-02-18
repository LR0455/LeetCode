#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
ifstream fin("input", ifstream::in);
ofstream fout("output", ifstream::out);

int maximumWealth(vector<vector<int>>& accounts) {
    int max_sum = 0;
    for (int i = 0 ; i < accounts.size() ; i ++) {
        int sum = 0;
        for (int j = 0 ; j < accounts[i].size() ; j ++)
            sum += accounts[i][j];
        max_sum = max(max_sum, sum);
    }
    return max_sum;
}

int main() {
    int m, n;
    fin >> m >> n;
    vector<vector<int>> accounts;
    for (int i = 0 ; i < m ; i ++) {
        accounts.push_back(vector<int>(n));
        for (int j = 0 ; j < n ; j ++)
            fin >> accounts[i][j];
    }
    fout << maximumWealth(accounts) << endl;
    return 0;
}