class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # This dic stores the last occurence index of each char
        # help whether a char can be removed or added later
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        stack = []
        # Since stack takes O(1) time to search whether the ele
        # exits or not
        # That's why I made the set
        in_stack = set()

        for i, ch in enumerate(s):
            if ch in in_stack:
                continue

            while stack and ch < stack[-1] and last[stack[-1]] > i:
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(ch)
            in_stack.add(ch)

        return "".join(stack)
