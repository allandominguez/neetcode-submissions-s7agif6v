func minSubArrayLen(target int, nums []int) int {
	// e.g. target = 10, nums = [2,1,5,1,5,3]
	l, r := 0, 0
	currSum := 0
	minLen := len(nums) + 1

	for r < len(nums) {
		currSum += nums[r]
		for currSum >= target && l <= r {
			minLen = min(minLen, r - l + 1)
			currSum -= nums[l]
			l++
		}
		r++
	}
	
	if minLen == len(nums) + 1 {
		return 0
	}
	return minLen
}
