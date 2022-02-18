#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
ifstream fin("input", ifstream::in);
ofstream fout("output", ifstream::out);

void rotate(vector<int>& nums, int k) {
    int len = nums.size();
    int start = len - (k % len);
    reverse(nums.begin(), nums.begin()+start);
    reverse(nums.begin()+start, nums.end());
    reverse(nums.begin(), nums.end());    
}

int main() {
    int n, k;
    fin >> n;
    vector<int> nums(n);
    for (int i = 0 ; i < n ; i ++)
        fin >> nums[i];
    fin >> k;
    rotate(nums, k);
    for (int i = 0 ; i < n ; i ++)
        fout << nums[i] << ' ';
    fout << endl;
    return 0;
}