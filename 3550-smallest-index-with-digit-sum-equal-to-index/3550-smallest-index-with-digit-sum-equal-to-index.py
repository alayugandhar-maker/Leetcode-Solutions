class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(0,n):
            add=0
            a=nums[i] 
            while a>0:
                d=a%10 
                add+=d 
                a//=10 
            #print(add,":",i) 
            if add==i:
                return i 
        return -1
        