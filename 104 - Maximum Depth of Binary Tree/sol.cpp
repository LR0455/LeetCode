#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
ifstream fin("input", ifstream::in);
ofstream fout("output", ifstream::out);
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

int max_depth = 0;
void dfs(TreeNode *tn, int depth) {
    if (tn == NULL)
        return;
    max_depth = max(max_depth, depth);
    dfs(tn->left, depth+1);
    dfs(tn->right, depth+1);
}
int maxDepth(TreeNode* root) {
    dfs(root, 1);
    return max_depth;
}

TreeNode* build(vector<int> &vals, int &len, int i) {
    if (i > len || vals[i] == -1000) return NULL;
    TreeNode *tn = new TreeNode(vals[i]);
    tn->left = build(vals, len, 2*i);
    tn->right = build(vals, len, 2*i+1);
    return tn;
}

int main() {
    int n, val;
    TreeNode *root;
    while(fin >> n) {
        vector<int> vals(n+1);
        for (int i = 1 ; i <= n ; i ++)
            fin >> vals[i];
        root = build(vals, n, 1);
    }
    fout << maxDepth(root) << endl;
    return 0;
}