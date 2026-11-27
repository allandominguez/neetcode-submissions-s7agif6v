/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 
func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return nil
	}
	// searching for the node
	// check the key against the current node (root)
	// if <, perform deleteNode on left subtree; assign root.Left
	if key < root.Val {
		root.Left = deleteNode(root.Left, key)
		return root
	// elif >, perform deleteNode on right subtree; assign root.Right
	} else if key > root.Val {
		root.Right = deleteNode(root.Right, key)
		return root
	}

	// else, this root node == key
	// if either LEFT or RIGHT subtrees are empty, return the other
	if root.Left == nil {
		return root.Right
	}
	if root.Right == nil {
		return root.Left
	}
	// the only nodes that can replace this node is either
		// - the largest leaf node from the LEFT subtree
		// - or the smallest leaf node from the RIGHT subtree (using this)
	// start from the right node, then traverse down the left nodes until reaching the leaf node
	cur := root.Right
	for cur.Left != nil {
		cur = cur.Left
	}
	// now everything to the left of the root node (in a BST) is < this leaf node
	// so we can assign the root's left subtree to the left of the leaf node
	cur.Left = root.Left
	// and now we return the new root of the right subtree, i.e. root.Right
	return root.Right
}
