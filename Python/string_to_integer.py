from curses.ascii import isdigit


class Solution:

    def myAtoi(self, s: str) -> int:

        s = s.strip()
        sign = True
        digits = ""
        num_match = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        sign_match = ['+', '-']

        for i in range(len(s)):
            if i == 0:
                if s[i] in sign_match and s[i] == '-':
                    sign = False
                if s[i] not in num_match + sign_match:
                    return 0
            if s[i] in num_match:
                digits += s[i]
            elif s[i] not in num_match and len(digits) > 0:
                break
            else:
                continue

        if not sign:
            return -int(digits)
        else:
            return int(digits)
