class Solution:
    def minimizedStringLength(self, s: str) -> int:
        d={}
        for ch in s:
            d[ch]=d.get(ch,0)+1
        return len(d)
        