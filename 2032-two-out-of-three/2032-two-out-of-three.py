class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        lst=list(set(nums1+nums2+nums3)) 
        lst1=[]
        for i in lst:
            if (i in nums1 and i in nums2) or (i in nums2 and i in nums3) or (i in nums1 and i in nums3) :
                lst1.append(i)
        return lst1
        