class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1 
        lst=[]
        for val in d.values():
            lst.append(val)
        a=max(lst)
        count=0
        for i in nums:
            if nums.count(i)==a:
                count+=1
        return count