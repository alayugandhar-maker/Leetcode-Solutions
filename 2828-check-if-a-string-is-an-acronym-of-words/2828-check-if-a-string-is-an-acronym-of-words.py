class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words)!=len(s):
            return False
        valid=True
        for i in range(len(s)):
            ans=words[i]
            if s[i]!=ans[0]:
                valid=False
                break 
        return valid

        