class Solution:

    def reverse_integer(self, x: int) -> int:
        if x < 0:
            x = str(-x)
            x = x[::-1]
            x = -int(x)
        if x >= 0:
            x = str(x)
            x = x[::-1]
            x = int(x)

        if x < -2**31 or x > 2**31 - 1:
            return 0
        return x