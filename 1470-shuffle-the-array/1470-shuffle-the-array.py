class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst1=[]
        for i in range(len(nums)//2):
            lst1.append(nums[i])
            lst1.append(nums[n+i])
        return lst1
