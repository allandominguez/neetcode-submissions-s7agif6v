class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] left = new int[length];
        int[] right = new int[length];
        
        left[0] = nums[0];
        int endI = length - 1;
        right[endI] = nums[endI];
        for (int i = 1; i < length; i++) {
            endI--;
            left[i] = nums[i] * left[i - 1];
            right[endI] = nums[endI] * right[endI + 1];
        }
        
        int[] output = new int[length];
        output[0] = right[1];
        output[length - 1] = left[length - 2];
        for (int i = 1; i < length - 1; i++) {
            output[i] = left[i - 1] * right[i + 1];
        }
        return output;
    }
}  
