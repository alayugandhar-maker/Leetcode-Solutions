class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in nums:
            if i%2==0:
                lst.append(0)
            else:
                lst.append(1)
        return sorted(lst)
        