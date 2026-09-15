class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v='aeiou'
        n=len(s)
        l,r=0,0
       #s1=""
        maxcount=0
        count=0
        while r<n:
            if s[r] in v:
                count+=1
            if r-l+1==k:
                maxcount=max(count,maxcount)
                if s[l] in v:
                   count-=1
                l+=1
            r+=1
        return maxcount
            
        