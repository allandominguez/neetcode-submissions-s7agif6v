/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private TreeNode recInvertTree(TreeNode root) {
        if (root == null) {
            return null;
        }

        TreeNode tmp = root.left;
        root.left = root.right;
        root.right = tmp;
        
        recInvertTree(root.left);
        recInvertTree(root.right);

        return root;
    }

    // private TreeNode itrInvertTree(TreeNode root) {
    //     Stack<TreeNode> stack = new Stack<>();
    //     TreeNode curr = root;
    //     TreeNode tmp;
    //     while (!stack.empty()) {
            
    //     }
    // }

    public TreeNode invertTree(TreeNode root) {
        return recInvertTree(root);
    }
}
