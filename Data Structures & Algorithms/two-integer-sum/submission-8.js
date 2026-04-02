class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // store the indices of each n in nums; numsInd
        const numsInd = new Map();
        for (let i = 0; i < nums.length; i++) {
            numsInd.set(nums[i], i);
        }
        
        // iterate through nums and find if target-n is in numsInd
        for (let i = 0; i < nums.length; i++) {
            let diff = target - nums[i];
            if (numsInd.has(diff) && numsInd.get(diff) !== i) {
                return [i, numsInd.get(target - nums[i])];
            }
        }
        return [];
    }
}
