class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        ans=0
        for num in nums:
            count=0
            temp=num
            while num>0:
                d=num%10
                count+=1
                num//=10 
            if count%2==0:
                ans+=1
        return ans
        