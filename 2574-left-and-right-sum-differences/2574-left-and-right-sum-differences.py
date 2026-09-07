class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        lst1 = []
        lst2 = []

        for i in range(n):
            s = sum(nums[0:i])
            lst1.append(s)

        for i in range(n):
            s = sum(nums[i+1:n])
            lst2.append(s)

        lst3 = []

        for i in range(n):
            ans = abs(lst1[i] - lst2[i])
            lst3.append(ans)

        return lst3