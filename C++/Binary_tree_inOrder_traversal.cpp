class Solution {
public:

void inOrder(TreeNode *root, vector<int> &ans) {
        if(root != NULL){
            inOrder(root->left, ans);
            ans.push_back(root->val);
            inOrder(root->right, ans);
        }
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int>ans;
        inOrder(root, ans);
        return ans;
    }
};
