func specialArray(nums []int) int {
    l, r := 0, len(nums)

	for l <= r {
		m := (l + r) / 2
		count := 0
		for _, n := range nums {
			if n >= m {
				count++
			}
		}
		if count > m {
			l = m + 1
		} else if count < m {
			r = m - 1
		} else {
			return m
		}
	}

	return -1
}