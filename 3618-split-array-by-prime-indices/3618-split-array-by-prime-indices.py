class Solution:
    def splitArray(self, nums: List[int]) -> int:
        if len(nums)<2:
            return abs(nums[0])
        n=len(nums)
        box=[1]*(n)
        box[0],box[1]=0,0
        a=0
        b=0

        for i in range(2,int(n**0.5)+1):
            if box[i]:
                for j in range(i*i,n,i):
                    box[j]=0
        
        for i in range(0,n):
            if box[i]:
                a+=nums[i]
            else:
                b+=nums[i]
        return abs(a-b)

