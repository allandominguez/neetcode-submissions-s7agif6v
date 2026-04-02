class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # need an array size +1 on both dimensions as padding
        self.sum_matrix = [
            [0] * (len(matrix[0]) + 1) 
            for _ in range(len(matrix) + 1)
        ]
        # gather the prefix-sums of (0,0) to (x,y)
        # and plug it into its corresponding (x+1,y+1) in sum_matrix; 
        # considering padding
        for x, row in enumerate(matrix):
            prefix = 0
            for y, c in enumerate(row):
                above = self.sum_matrix[x][y + 1]
                curr_sum = prefix + above + matrix[x][y]
                self.sum_matrix[x + 1][y + 1] = curr_sum
                prefix += matrix[x][y]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # (row1, col1) is top-left, (row2, col2) is bottom-right
        # to calculate our region, we get the corresponding bottom-right sum
        # in our sum_matrix, 
        curr_sum = self.sum_matrix[row2 + 1][col2 + 1]
        # subtracting the prefix on the x and y axes, 
        x_prefix = self.sum_matrix[row1][col2 + 1]
        y_prefix = self.sum_matrix[row2 + 1][col1]
        # plus the top-left (row1-1, col1-1) value as we subtracted it twice
        # from x and y axes.
        top_left_prefix = self.sum_matrix[row1][col1]
        return curr_sum - x_prefix - y_prefix + top_left_prefix


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)