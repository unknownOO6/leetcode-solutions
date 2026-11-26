class Solution:
    def reverse(self, x):
        s = -1 if x < 0 else 1
        r = int(str(abs(x))[::-1]) * s
        return r if -(2**31) <= r <= 2**31 - 1 else 0