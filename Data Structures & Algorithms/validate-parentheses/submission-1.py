class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = { ')':'(', '}':'{', ']':'['}
        for char in s:
            if char not in map:
                stack.append(char)
            else:
                if stack and stack[-1] == map[char]:
                    stack.pop()
                else:
                    return False
        return not stack
        