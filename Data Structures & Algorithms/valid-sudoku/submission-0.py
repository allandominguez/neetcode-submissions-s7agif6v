class Solution:
    def _get_pre_mid_post_index(self, i: int) -> int:
        if 0 <= i <= 2:
            return 0
        elif 3 <= i <= 5:
            return 1
        else:
            return 2
    
    def _get_quadrant(self, i: int, j: int) -> List[int]:
        return [self._get_pre_mid_post_index(i), self._get_pre_mid_post_index(j)]

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # quadrant sets
        board_quadrants = [
            [set(), set(), set()],
            [set(), set(), set()],
            [set(), set(), set()]
        ]

        # column sets
        cols = [set() for _ in range(0,9)]
        
        for i, row in enumerate(board):
            row_set = set()
            for j, item in enumerate(row):
                if item == ".":
                    continue
                quad_i, quad_j = self._get_quadrant(i, j)
                if any((
                    item in row_set,
                    item in cols[j],
                    item in board_quadrants[quad_i][quad_j]
                )):
                    return False
                row_set.add(item)
                cols[j].add(item)
                board_quadrants[quad_i][quad_j].add(item)
        
        return True
                