from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Use two pointer to check the max area
        left = 0
        right = len(height) -1
        largest = 0

        while left < right:
            # width, height, area
            # the lower height always limits the area
            h = min(height[left], height[right])
            w = right - left
            largest = max(largest, h * w)

            # move the shorter pointer to potentially increase the height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return largest

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]

    sol = Solution()
    k = sol.maxArea(height)
    print("k =", k)
