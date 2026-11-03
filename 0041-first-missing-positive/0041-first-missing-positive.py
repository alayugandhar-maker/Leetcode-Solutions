class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        s=set(nums)
        m=max(nums)
        if m<0:
          return 1
        for i in range(1,m+1):
            if i not in s:
                return i
            
        return m+1