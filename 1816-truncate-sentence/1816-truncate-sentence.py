class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=s.split()
        s1=" "

        for i in range(k):
            s1=s1+' '+s[i]
        s1=s1.strip()
        return s1
        