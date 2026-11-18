func findChampion(n int, edges [][]int) int {
	// teams are labelled 0 to n-1
	// strongest just means a node without weaknesses

	// create a hashset, winners, of 0 to n-1
	winners := make(map[int]struct{})
	for i := 0; i < n; i++ {
		winners[i] = struct{}{}
	}
	
	// iterate the edges:
	for _, edge := range edges {
		// just looking at the losers
		loser := edge[1]
		// remove them from the winners
		delete(winners, loser)
	}
	
	// if winners is empty, or size > 1, then return -1
	if len(winners) > 1 || len(winners) == 0 {
		return -1
	}
	for team, _ := range winners {
		return team
	}
	return -1
}
