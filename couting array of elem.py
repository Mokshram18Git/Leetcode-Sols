class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
       freq = {}

       for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

       result = []
       for key in freq:
        result.append([[key,freq[key]]])

       return result