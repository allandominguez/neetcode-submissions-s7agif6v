class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    self.search_island(grid, r, c, visited)
                    islands += 1
        return islands
    
    def search_island(self, grid: List[List[str]], r: int, c: int, visited: Set) -> None:
        directions = ([1,0], [-1,0], [0,1], [0,-1])
        queue = deque([(r,c)])
        while queue:
            curr_r, curr_c = queue.popleft()
            if grid[curr_r][curr_c] == "1" and (curr_r,curr_c) not in visited:
                visited.add((curr_r, curr_c))
                for adj_r, adj_c in directions:
                    if (
                        0 <= adj_r + curr_r < len(grid) and
                        0 <= adj_c + curr_c < len(grid[0]) and
                        grid[adj_r + curr_r][adj_c + curr_c] == "1"
                    ):
                        queue.append((adj_r + curr_r, adj_c + curr_c))
        