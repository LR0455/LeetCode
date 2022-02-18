#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream fin("input", ifstream::in);
ofstream fout("output", ifstream::out);
string removeKdigits(string num, int k) {
    if (num.size() == k) return "0";
    int i;
    while(k --) {
        int len = num.size();
        for(i = 1 ; i < len ; i ++) 
            if (num[i-1] > num[i]) {
                num.erase(num.begin()+i-1);
                break;
            }
        if (i == len)
            num.erase(num.begin()+i-1);
    }
    for (i = 0 ; num[i] == '0' ; i ++); // remove zero
    num.erase(num.begin(), num.begin()+i);
    
    return num.size() ? num : "0";
}
int main() {
    string num;
    int k;
    while (fin >> num >> k) {
        fout << removeKdigits(num, k) << endl;
    }
    return 0;
}