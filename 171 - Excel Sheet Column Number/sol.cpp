#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("input", ifstream::in);
ofstream fout("output", ifstream::out);

class Solution {
public:
    int titleToNumber(string columnTitle) {
        int column_num = 0;
        for (int i = 0 ; i < columnTitle.size() ; i ++) {
            if (i)
                column_num *= 26;
            column_num += (columnTitle[i] - 'A' + 1);
        }
        return column_num;
    }
};

int main() {
    string columnTitle;
    while(fin >> columnTitle) {
        Solution *sol = new Solution();
        fout << sol->titleToNumber(columnTitle) << endl;
    }
    return 0;
}