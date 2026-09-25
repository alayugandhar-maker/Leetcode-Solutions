class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        m=list(m)
        for ch in r:
            if ch in m:
                m.remove(ch)
            else:
                return False 
        return True
        