class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lst=[]
        for i in range(1,n+1):
            lst.append(i)
        lst1=[]
        s=set(nums)
        for i in lst:
            if i not in s:
                lst1.append(i)
        return lst1
        