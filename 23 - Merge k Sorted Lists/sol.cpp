#include <iostream>
#include <fstream>
#include <vector>
#include <limits.h>
#include <sstream>
using namespace std;
ifstream fin("input", ifstream::in);
ofstream fout("output", ifstream::out);

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* mergeKLists(vector<ListNode*>& lists) {
    ListNode *ans = new ListNode(), *ptr = ans;
    do {
        int val = INT_MAX, k = -1;
        
        for(int i = 0 ; i < lists.size() ; i ++) 
            if (lists[i] && val >= lists[i]->val) {
                val = lists[i]->val;
                k = i;
            }
        if (k == -1) break;
        
        ptr->next = lists[k];
        lists[k] = lists[k]->next;
        ptr = ptr->next;
    } while(true);
    return ans->next;
}

int main() {
    int n, num;
    vector<ListNode*> lists;
    while(fin >> n) {
        string line;
        getline(fin, line); // endline bug

        while(n --) {
            ListNode *head = new ListNode(), *ptr = head, *pnt = NULL;
            getline(fin, line);
            stringstream ss(line);
            while (ss >> num) {
                ptr->val = num;
                ptr->next = new ListNode();
                pnt = ptr;
                ptr = ptr->next;    
            }
            pnt->next = NULL;
            
            lists.push_back(head);
        }
        ListNode *ans = mergeKLists(lists);
        while(ans) {
            fout << ans->val << ' ';
            ans = ans->next;
        }
        fout << endl;
    }

    return 0;
}