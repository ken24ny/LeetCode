class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_hay = len(haystack)
        len_need = len(needle)

        if needle == '':
            return 0
        elif len_hay < len_need:
            return -1
        else:
            for i in range(0,len_hay - len_need + 1):
                if haystack[i:i+len_need] == needle:
                    return i
            return -1

