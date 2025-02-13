class Solution(object):
    def hammingWeight(self, n):
        
        result = 0
        while n:
            n = n & (n - 1)
            result += 1
        return result
