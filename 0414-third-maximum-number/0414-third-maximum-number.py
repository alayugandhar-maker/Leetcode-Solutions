class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=list(set(nums))
        if len(s)<3:
            return max(s)
        
        s.sort()
        return s[-3]
        

        