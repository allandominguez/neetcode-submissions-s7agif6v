class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)

        n2 = set()
        for n in nums2:
            if n in n1:
                n2.add(n)
        
        return list(n2)
