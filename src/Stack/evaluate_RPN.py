from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # create a number stack and an operator stack
        nums = []
        operators = ["+", "-", "*", "/"]

        # filter the tokens whether it is a number or operators
        for token in tokens:
            if token not in operators:
                nums.append(int(token))
                continue

            # 1, 2 -> 2, 1
            b = nums.pop()
            a = nums.pop()

            match token:
                case "+":
                    nums.append(a + b)
                case "-":
                    nums.append(a - b)
                case "*":
                    nums.append(a * b)
                case "/":
                    nums.append(int(a / b))
        return nums[-1]

if __name__ == "__main__":
    tokens = ["1", "2", "+", "3", "*", "6", "-"]
    sol = Solution()
    print(sol.evalRPN(tokens))  #