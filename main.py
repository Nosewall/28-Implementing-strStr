class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if i + j < len(haystack):
                        print(haystack[i + j])
                    if i + j < len(haystack) and haystack[i + j] != needle[j]:
                        break
                    if i + j >= len(haystack):
                        break
                    if j == (len(needle) - 1):
                        return i
        return -1

sol = Solution()
print(sol.strStr("mississippi", "sippia"))




