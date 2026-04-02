class Solution {
    private boolean logMPlusLogN(int[][] matrix, int target) {
        int l = 0, r = matrix.length - 1;
        int m;
        
        // find the row
        while (l <= r) {
            m = (l + r) / 2;
            if (matrix[m][0] == target) return true;
            if (target > matrix[m][0]) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        // iterate the row
        int row = (l + r) / 2;
        l = 0;
        r = matrix[row].length - 1;
        while (l <= r) {
            m = (l + r) / 2;
            if (matrix[row][m] == target) return true;
            if (target > matrix[row][m]) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        
        return false;
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        return logMPlusLogN(matrix, target);
    }
}
