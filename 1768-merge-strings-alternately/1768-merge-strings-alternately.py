class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        n=min(len(word1),len(word2))
        for i in range(min(len(word1),len(word2))):
            s+=word1[i]
            s+=word2[i]
        ans=word1[n:] or word2[n:]
        return s+ans
        

        