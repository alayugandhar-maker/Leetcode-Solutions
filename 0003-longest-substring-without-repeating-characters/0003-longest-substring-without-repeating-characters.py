class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l=0
        r=0
        maxlen=0
        hasht=[-1]*(256)
        while(r<n):
            if hasht[ord(s[r])]!=-1:
                if hasht[ord(s[r])]>=l:
                    l=hasht[ord(s[r])]+1
            le=r-l+1
            maxlen=max(maxlen,le)
            hasht[ord(s[r])]=r
            r+=1 
        return maxlen

        