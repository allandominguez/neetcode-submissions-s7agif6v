class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        // two pointers at the start and end
        let l = 0;
        let r = numbers.length - 1;
        
        // sum the pointers
            // if sum is too larger, shift right pointer down
            // if too small, shift left pointer up
        while (l < r) {
            let sum = numbers[l] + numbers[r];
            if (sum === target) {
                return [l + 1, r + 1];
            } else if (sum > target) {
                r--;
            } else {
                l++;
            }
        }
        return [l + 1, r + 1];
    }
}
