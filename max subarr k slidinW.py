class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        
        n = len(arr)
        
        if k == 0 or k > n:
            return None
            
        window_sum = sum(arr[0:k])
        max_sum = window_sum
        
        for i in range(k,n):
            window_sum = window_sum + arr[i] - arr[i-k]
            if window_sum > max_sum:
                max_sum = window_sum
        return max_sum