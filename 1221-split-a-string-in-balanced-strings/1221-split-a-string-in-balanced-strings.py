class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans=0
        maxans=0
        for i in range(0,len(s)):
            if s[i]=='L':
                ans+=1
            else:
                ans-=1
            if ans==0:
                maxans+=1
        return maxans
