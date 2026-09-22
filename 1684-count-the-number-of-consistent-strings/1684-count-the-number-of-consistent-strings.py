class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        a=set(allowed)
        for word in words:
            if all(ch in a for ch in word):
                count+=1 
        return count
            