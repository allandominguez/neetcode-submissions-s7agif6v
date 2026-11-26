func shipWithinDays(weights []int, days int) int {
	// e.g. weights = [2,4,6,1,3,10], days = 4
	// we know that the minimum capacity has to be the max package weight
	// and the maximum capacity (day = 1) is the total weight
	l, r := 0, 0
	for _, weight := range weights {
		l = max(l, weight)
		r += weight
	}
	
	// now we can binary search based on that window
	for l <= r {
		// e.g. l, r = 10, 26
		// capacity = 10 + (26-10) / 2 = 18
		var capacity int = l + (r - l) / 2
		// check if capacity can ship — external function
		// if possible: check left window; r = mid - 1
		if canShip(weights, days, capacity) {
			r = capacity - 1
		// else (not possible): check right window; l = mid + 1
		} else {
			l = capacity + 1
		}
	}
	
	// since left is looking for lowest possible, it should land on it
	return l
}

func canShip(weights []int, days int, capacity int) bool {
	currCap := capacity
	// iterate weights:
	for _, weight := range weights {
		// check if currCapacity - package < 0:
		if currCap - weight < 0 {
			// decrement days
			days--
			// reset currCapacity (and decrement it by package)
			currCap = capacity - weight
		} else {
			currCap -= weight
		}
		// if days <= 0: return false
		if days <= 0 { return false }
	}
	return true

}
