class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        lst=[]
        while nums:
            m1=min(nums)
            m2=max(nums)
            ans=(m1+m2)/2
            lst.append(ans)
            nums.remove(m1)
            nums.remove(m2)
        return min(lst)