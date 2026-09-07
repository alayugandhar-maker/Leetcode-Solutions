class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        for j in range(1,len(nums)):
            if nums[i]==nums[j]:
                nums[i]=nums[i]*2
                nums[j]=0
            i+=1 
        lst1=[]
        lst2=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                lst1.append(nums[i])
            else:
                lst2.append(nums[i])
        return lst1+lst2
        