#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("input", ifstream::in);
ofstream fout("output", ifstream::out);

int addDigits(int num) {
    if (num == 0)
        return 0;
    if (num % 9 == 0)
        return 9;
    return num % 9;
}

int main() {
    int num;
    while(fin >> num) {
        fout << addDigits(num) << endl;
    }

    return 0;
}