/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <iostream>
using namespace std;

/**
 * Definition for a binary tree node.
 */
class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        int sum = 0;
        bstToGstHelper(root, sum);
        return root;
    }
    
private:
    void bstToGstHelper(TreeNode* node, int& sum) {
        if (node == nullptr) {
            return;
        }
        
        // Traverse the right subtree first
        bstToGstHelper(node->right, sum);
        
        // Update the current node
        sum += node->val;
        node->val = sum;
        
        // Traverse the left subtree
        bstToGstHelper(node->left, sum);
    }
};

// Helper function to print the tree in-order (for testing)
void printInOrder(TreeNode* root) {
    if (root == nullptr) {
        return;
    }
    printInOrder(root->left);
    cout << root->val << " ";
    printInOrder(root->right);
}