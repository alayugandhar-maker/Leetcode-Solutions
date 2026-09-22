class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        lst=[0]
        lst[0]=pref[0]
        for i in range(1,len(pref)):
            lst.append(pref[i]^pref[i-1])
        return lst

