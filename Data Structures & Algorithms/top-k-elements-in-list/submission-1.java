class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        return minHeapMethod(nums, k);
    }

    private int[] minHeapMethod(int[] nums, int k) {
        // count the elements
        Map<Integer, Integer> count = new HashMap<>();
        for (int n : nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }

        // use min-heap to narrow top k
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            heap.offer(new int[]{
                entry.getKey(), entry.getValue()
            });
            if (heap.size() > k) {
                heap.poll();
            }
        }

        // translate back into an array
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = heap.poll()[0];
        }
        return result;
    }
}
