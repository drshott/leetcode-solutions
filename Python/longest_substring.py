import unittest

class Solution:

    def longest_substring(self, s: str) -> int:
        n = len(s)
        char_set = set()
        max_length = 0

        left = 0

        for right in range(n):
            if s[right] not in char_set:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
            else:
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1
                char_set.add(s[right])

        return max_length
