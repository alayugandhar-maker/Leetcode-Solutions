class Solution:
    def reversePrefix(self, s: str, ch: str) -> str:
        if ch not in s:
            return s
        s=list(s)
        l=0
        r=s.index(ch)
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1 
        return ''.join(s)
        