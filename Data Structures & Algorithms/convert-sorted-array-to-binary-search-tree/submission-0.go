func sortedArrayToBST(nums []int) *TreeNode {
	// the array gives us the flattened structure of the BST
	// each node is the mid-point of each sub-array

	// start with the left and right pointers

	var dfs func(int, int) *TreeNode
	// use recursion to iterate each sub-array
	dfs = func(l int, r int) *TreeNode {
		// end condition: if left > right
		if l > r {
			return nil
		}

		// calculate the mid-point and create a new node
		m := l + (r - l) / 2
		node := &TreeNode{Val: nums[m]}
		// recursively process the left sub-array 
		node.Left = dfs(l, m - 1)
		// recursively process the right sub-array 
		node.Right = dfs(m + 1, r)

		// return the mid-point node
		return node
	}
	
	// return the recusive call on original left and right pointers
	return dfs(0, len(nums) - 1)
}
