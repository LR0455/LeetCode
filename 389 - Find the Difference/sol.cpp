#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("input", ifstream::in);
ofstream fout("output", ifstream::out);

char findTheDifference(string s, string t) {
    int count[26] = {0}, i;
    for (i = 0 ; i < s.size() ; i ++)
        count[s[i] - 'a'] ++;
    for (i = 0 ; i < t.size() ; i ++)
        count[t[i] - 'a'] --;
    for (i = 0 ; i < 26 ; i ++)
        if (count[i])
            return 'a' + i;
    return -1;
}

int main() {
    string s, t;
    while(getline(fin, s)) {
        getline(fin, t);
        fout << findTheDifference(s, t) << endl;
    }

    return 0;
}