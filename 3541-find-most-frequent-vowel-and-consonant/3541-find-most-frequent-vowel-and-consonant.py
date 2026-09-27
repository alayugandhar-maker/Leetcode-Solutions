class Solution:
    def maxFreqSum(self, s: str) -> int:
        d={}
        v='aeiou'
        for ch in s:
            d[ch]=d.get(ch,0)+1 
        maxc=0
        maxv=0 
        for val in d:
            if val in v:
                maxv=max(maxv,d[val])
            else:
                maxc=max(maxc,d[val])
        return maxc+maxv

                

        