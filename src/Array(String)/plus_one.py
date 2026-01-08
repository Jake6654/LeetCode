from string import digits
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # (len(digits) - 1, -1, -1) ->
        # len(digits) -1 means starts from last index of list
        # range(start, stop, step)
        # if stop value is -1, it stops right before -1, which means index 0
        # digits [1,3,9]
        for i in range(len(digits) -1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

            # prepend 1 to the list when all elements are 9
            return [1] + digits
