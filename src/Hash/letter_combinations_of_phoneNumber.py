from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtracking(i, curStr):
            # base case
            # when the length of curStr is the same as the length of digits
            # add curStr it to list and go to next the letter
            if len(digits) == len(curStr):
                res.append(curStr)
                return

            for c in digToChar[digits[i]]:
                backtracking(i +1, curStr + c)

        if digits:
            backtracking(0, "")
        return res
