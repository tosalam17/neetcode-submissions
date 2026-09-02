class Solution:
    def isValid(self, s: str) -> bool:
        key_map = {"}": "{", "]":"[", ")": "("}
        res = []

        for char in s:
            if char in key_map:
                if res and res[-1] == key_map[char]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)

        return not res
                