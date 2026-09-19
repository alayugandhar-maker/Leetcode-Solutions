class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        lst=[0]*(n+1)
        lst[0]=0
        lst[1]=gain[0]
        ans=0

        for i in range(0,len(gain)):
            ans+=gain[i]
            lst[i+1]=ans
        return max(lst)

    


        