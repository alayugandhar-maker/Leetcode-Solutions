class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        lst1=[]
        lst2=[]
        lst3=[]
        for i in nums:
            if i<pivot:
                lst1.append(i)
            elif i==pivot:
                lst2.append(i)
            else:
                lst3.append(i)
        return lst1+lst2+lst3       