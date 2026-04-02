class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        // iterate to gather products of every left num of index
        const left = new Array(nums.length);
        let product = 1;
        for (let i = 0; i < nums.length; i++) {
            product *= nums[i];
            left[i] = product;
        }

        // then gather products of right
        const right = new Array(nums.length);
        product = 1;
        for (let i = nums.length - 1; i >= 0; i--) {
            product *= nums[i];
            right[i] = product;
        }

        // now iterate and multiply the left and right of each index
        const res = new Array(nums.length);
        for (let i = 0; i < nums.length; i++) {
            if (i === 0) {
                res[i] = right[1];
            } else if (i === nums.length - 1) {
                res[i] = left[i - 1];
            } else {
                let r = right[i + 1];
                let l = left[i - 1];
                res[i] = r * l;
            }
        }
        return res;
    }
}
