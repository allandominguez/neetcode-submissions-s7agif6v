class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> nums_index = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            nums_index.put(nums[i], i);
        }

        int remainder;
        for (int i = 0; i < nums.length; i++) {
            remainder = target - nums[i];
            if (nums_index.containsKey(remainder) && nums_index.get(remainder) != i) {
                return new int[] {i, nums_index.get(remainder)};
            }
        }
        return new int[] {0, 0};
    }
}
