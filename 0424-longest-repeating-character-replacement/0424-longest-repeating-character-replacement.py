class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        l,r,maxlen,maxf=0,0,0,0 
        lst=[0]*(26)
        while r<n:
            lst[ord(s[r])-ord('A')]+=1 
            maxf=max(maxf,lst[ord(s[r])-ord('A')])

            if (r-l+1)-maxf>k:
                lst[ord(s[l])-ord('A')]-=1
                '''maxf=0
                for i in range(25):
                    maxf=max(maxf,lst[i])'''
                l+=1 
            if (r-l+1)-maxf<=k:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen


        