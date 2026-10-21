class Solution(object):
    def reverseBits(self, n):
        n = n & 0xffffffff
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1

        if result >= 2**32:
            result -= 2**31
        return result