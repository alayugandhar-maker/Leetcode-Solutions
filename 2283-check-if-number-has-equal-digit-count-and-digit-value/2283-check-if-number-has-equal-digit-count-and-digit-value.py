class Solution:
    def digitCount(self, num: str) -> bool:
        nums=list(num)
        valid=True
        for i in range(0,len(nums)):
            if int(nums[i])!=nums.count(str(i)):
                valid=False
        return valid


        