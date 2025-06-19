class Solution:

    def str_str(self, haystack: str, needle: str) -> int:

        char_index = -1
        j = 0

        for i in range(len(haystack)):
            if haystack[i] == needle[j]:
                if j == 0:
                    char_index = i
                if j >= len(needle) - 1:
                    return char_index
                j += 1
            else:
                char_index = -1
                j = 0

        return char_index
