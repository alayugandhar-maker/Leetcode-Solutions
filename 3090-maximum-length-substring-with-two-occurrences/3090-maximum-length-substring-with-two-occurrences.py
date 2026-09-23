class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d={}
        l,r=0,0
        n=len(s)
        maxlen=0 
        while r<n:
            d[s[r]]=d.get(s[r],0)+1 
            while d[s[r]]>2:
                d[s[l]]-=1 
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
            maxlen=max(maxlen,r-l+1) 

            r+=1 
        return maxlen

        