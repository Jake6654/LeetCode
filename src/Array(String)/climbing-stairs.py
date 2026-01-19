class Solution:
    def climbStairs(self, n: int) -> int:
        # I think there's a pattern to solve this problem
        # if n = 4 , 1111, 112,121,211,22 -> 5
        # if n = 5, 11111, 1112, 1121, 1211, 2111, 122, 22
        # f(n) = f(n-1) + f(n-2) -> fibonacci
        if n <= 2:
            return n

        prev2 = 1  # f(1)
        prev1 = 2  # f(2)

        for _ in range(3, n + 1):
            # keep updating all values until end
            curr = prev1 + prev2  # 3
            prev2 = prev1  # 2
            prev1 = curr  # 3
        return prev1