from curses.ascii import isdigit


class Solution:

    def myAtoi(self, s: str) -> int:

        s = s.strip()
        sign = True
        digits = ""

        if s[0] in ['+', '-']:
            if s[0] == '-':
                sign = False
                s = s[1:]
        if s[0] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']:
            return 0

        for i in range(len(s)):
            if s[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                digits += s[i]
            elif s[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and len(digits) > 0:
                break
            else:
                continue

        if not sign:
            return -int(digits)
        else:
            return int(digits[1])
