
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # starting beyond that point would go out of the range
        for i in range(len(haystack) - len(needle) + 1):
            # This expression extracts a substring from haystack
            # i: starting index, i + len(needle): ending index
            if haystack[i: i + len(needle)] == needle:
                return 1
        return -1
"""
Time complexity: O(n x m)
We check up to n starting points
And each comparison takes up to m chars
"""