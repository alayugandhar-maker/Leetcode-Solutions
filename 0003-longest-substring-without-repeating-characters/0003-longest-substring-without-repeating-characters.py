class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l=0
        r=0
        maxlen=0
        lst=[-1]*(256)
        while(r<n):
            if lst[ord(s[r])]!=-1:
                if lst[ord(s[r])]>=l:
                    l=lst[ord(s[r])]+1
            le=r-l+1
            maxlen=max(maxlen,le)
            lst[ord(s[r])]=r
            r+=1 
        return maxlen

        