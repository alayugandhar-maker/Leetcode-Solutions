class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        s=list(set(nums))
        n=len(s)
        s.sort()
        lst=[]
        for i in range(n-1,-1,-1):
            lst.append(s[i])
            if len(lst)==k:
                break 
        return lst

        