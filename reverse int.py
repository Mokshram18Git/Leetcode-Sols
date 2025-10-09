class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            sign = -1
        else:
            sign = 1

        x = abs(x)

        ans = 0

        while x != 0:
            last = x%10
            ans = ans * 10 + last
            x = x//10
        return sign * ans
