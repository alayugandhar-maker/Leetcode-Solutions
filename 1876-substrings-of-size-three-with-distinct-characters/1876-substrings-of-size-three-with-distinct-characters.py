class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        l,r=0,0
        count=0
        d={}
        while r<n:
            d[s[r]]=d.get(s[r],0)+1
            if r-l+1==3:
                if len(d)==3:
                    count+=1
                #count+=1
            
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1 
            r+=1

        return count

        