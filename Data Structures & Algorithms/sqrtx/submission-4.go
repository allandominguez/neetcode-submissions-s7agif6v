func mySqrt(x int) int {
	l, r := 0, x
	last_valid := 0

	for l <= r {
		mid := (l + r) / 2
		exp := mid * mid
		if exp > x {
			r = mid - 1
		} else if exp < x {
			l = mid + 1
			last_valid = mid
		} else {
			return mid
		}
	}

	return last_valid
}
