from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # is it okay if I the function return new Integer array?
        nums1 = []
        for i in nums:
            if i == val:
                continue
            else:
                nums1.append(i)
        k = len(nums1)
        # replace the first k elements of nums with nums1
        nums[:k] = nums1
        return k


if __name__ == "__main__":
    nums = [1,2,2,3,2,3,2]
    val = 2

    sol = Solution()
    k = sol.removeElement(nums, val)
    print("k =", k)


