class Solution {
    private int recBinarySearch(int l, int r, int[] nums, int target) {
        if (l > r) return -1;

        int m = (l + r) / 2;

        if (nums[m] == target) return m;
        if (target > nums[m]) {
            return recBinarySearch(m + 1, r, nums, target);
        } else {
            return recBinarySearch(l, m - 1, nums, target);
        }
    }

    private int itrBinarySearch(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        int m;

        while (l <= r) {
            m = (l + r) / 2;
            if (nums[m] == target) return m;
            if (target > nums[m]) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return -1;
    }

    public int search(int[] nums, int target) {
        // return recbinarySearch(0, nums.length - 1, nums, target);
        return itrBinarySearch(nums, target);
    }
}
