/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 
func deleteNode(root *TreeNode, key int) *TreeNode {
	// if root is null, return null
	if root == nil {
		return nil
	}
	
	// traverse BST based on root and key; recursion
	if key < root.Val {
		root.Left = deleteNode(root.Left, key)
		return root
	} else if key > root.Val {
		root.Right = deleteNode(root.Right, key)
		return root
	}
	
	// once we've found the target
	// if the left or right subtrees are empty, then return the other
	if root.Left == nil {
		return root.Right
	}
	if root.Right == nil {
		return root.Left
	}
	// retrieve replacement from the largest node of the left subtree
	leftMax := root.Left
	for leftMax.Right != nil {
		leftMax = leftMax.Right
	}
	// assign the root.Right to the leftMax.Right
	leftMax.Right = root.Right
	// return the root.Left
	return root.Left
}
