from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # This pb requires O(log n) time complexity
        # which means you have to use Binary search
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Set pivot
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                # add or subtract 1 not to overlap the element
                left = mid + 1
            else:
                right = mid - 1

        return left