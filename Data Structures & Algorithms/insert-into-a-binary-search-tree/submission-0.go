/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func insertIntoBST(root *TreeNode, val int) *TreeNode {
    // assuming we don't need to keep the BST balanced

	// recursively search until we find an empty space 
	// take a node and a val
	// if node == nil: create and return new val node
	if root == nil {
		return &TreeNode{Val: val}
	}
	// if val > node.Val: search right subtree
	if val > root.Val {
		// node.Right = recursion(node.Right, val)
		root.Right = insertIntoBST(root.Right, val)
	} else {
	// else (guaranteed val does not exist): search left subtree
		// node.Left = recursion(node.Left, val)
		root.Left = insertIntoBST(root.Left, val)
	}
	// return node
	return root
}
