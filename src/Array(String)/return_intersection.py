class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return values must be unique -> set
        set1 = set(nums1)
        result = set()  # To return a new set


        # Don't overthink it
        for i in nums2:
            if i in set1:
                result.add(i)

        return list(result)