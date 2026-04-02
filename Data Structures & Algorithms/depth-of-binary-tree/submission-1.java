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
    private int itrCalcDepth(TreeNode root) {
        Stack<Pair<TreeNode, Integer>> stack = new Stack<>();
        stack.push(new Pair<>(root, 1));
        int maxCount = 0;
        while (!stack.empty()) {
            Pair<TreeNode, Integer> entry = stack.pop();
            TreeNode node = entry.getKey();
            Integer depth = entry.getValue();

            if (node != null) {
                maxCount = Math.max(maxCount, depth);
                stack.push(new Pair<>(node.left, depth + 1));
                stack.push(new Pair<>(node.right, depth + 1));
            }
        }
        return maxCount;
    }

    private int recCalcDepth(Pair<TreeNode, Integer> entry) {
        // todo
        return 0;
    }

    public int maxDepth(TreeNode root) {
        return itrCalcDepth(root);
        // return recCalcDepth(new Pair<>(root, 1));
    }
}
