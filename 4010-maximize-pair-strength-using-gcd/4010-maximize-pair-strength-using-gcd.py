class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        ans=float('-inf')
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                g=math.gcd(nums[i],nums[j])
                a=nums[i]*nums[j]
                aa=a//(g*g)
                ans=max(ans,aa)
        return ans


        