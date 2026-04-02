class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        // count occurrences of every n in nums
        const count = new Map();
        for (let n of nums) {
            count.set(n, (count.get(n) || 0) + 1);
        }

        // use a MinPriorityQueue to keep track of top k occurrences
        const heap = new MinPriorityQueue((x) => x[1]);
        
        // iterate on count and keep track of heap size
        for (let x of count) {
            heap.enqueue(x);
            if (heap.size() > k) {
                heap.dequeue();
            }
        }

        // extract and return only the n (not the count)
        return Array.from(heap, x => x[0]);
    }
}
