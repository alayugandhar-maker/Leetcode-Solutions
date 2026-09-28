class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        maxans=0
        for ch in s:
            if ch=='(':
                ans+=1
            elif ch==')':
                ans-=1 
            maxans=max(maxans,ans)
        return maxans
        