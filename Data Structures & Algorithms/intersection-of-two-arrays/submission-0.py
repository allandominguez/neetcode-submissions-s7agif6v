class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        i = j = 0
        nums1.sort()
        nums2.sort()

        while i < len(nums1) and j < len(nums2):
            if i > 0 and nums1[i - 1] == nums1[i]:
                i += 1
                continue
            if j > 0 and nums2[j - 1] == nums2[j]:
                j += 1
                continue
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return res
