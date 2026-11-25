func islandPerimeter(grid [][]int) int {
	// do a search to find land
	x, y := findIsland(grid)

	// keep track of visited cells
	visited := make(map[[2]int]struct{}) 

	var measurePerimeter func(int, int) int
	measurePerimeter = func(i int, j int) int {
		// if cell has been visited, return 0
		if _, exists := visited[[2]int{i,j}]; exists {
			return 0
		}
		// if cell is water, return 1
		if grid[i][j] == 0 {
			return 1
		}

		visited[[2]int{i,j}] = struct{}{}

		// track perimeter
		perimeter := 0

		// we calculate it's sides
		// top side
		if i == 0 {
			perimeter++
		} else {
			perimeter += measurePerimeter(i-1, j)
		}

		// left side
		if j == 0 {
			perimeter++
		} else {
			perimeter += measurePerimeter(i, j-1)
		}

		// bottom side
		if i == len(grid)-1 {
			perimeter++
		} else {
			perimeter += measurePerimeter(i+1, j)
		}

		// right side
		if j == len(grid[0])-1 {
			perimeter++	
		} else {
			perimeter += measurePerimeter(i, j+1)
		}

		return perimeter
	}

	return measurePerimeter(x,y)
}

func findIsland(grid [][]int) (int,int) {
	for i:=0; i<len(grid); i++ {
		for j:=0; j<len(grid[0]); j++ {
			if grid[i][j] == 1 {
				return i, j
			}
		}
	}
	return -1, -1
}
