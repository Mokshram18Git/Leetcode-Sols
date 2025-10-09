class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1

        while i>=0:
            digits[i] += 1

            if digits[i]<10:
                return digits
            
            digits[i] = 0
            i = i-1

        digits = [1] + digits

        return digits