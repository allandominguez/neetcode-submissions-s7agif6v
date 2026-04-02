class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> visited = new HashSet<Integer>();
        for (int n : nums) {
            if (visited.contains(n)) {
                return true;
            }
            visited.add(n);
        }
        return false;
    }
}
