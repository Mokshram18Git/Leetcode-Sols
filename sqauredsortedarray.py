class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        n = len(nums)
        start = 0
        end = n-1
        a = [0] * n

        for i in range(n-1,-1,-1):
            if abs(nums[start]) > abs(nums[end]):
                a[i] = nums[start] * nums[start]
                start = start + 1

            else:
                a[i] = nums[end] * nums[end]
                end = end - 1
            
        return a


            
        