class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        permu=0
        for i in s:
            permu+=abs(s.index(i)-t.index(i))
        return permu

        