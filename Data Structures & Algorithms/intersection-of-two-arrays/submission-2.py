class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)

        n2 = []
        for n in nums2:
            if n in n1:
                n2.append(n)
                n1.remove(n)
        
        return n2
