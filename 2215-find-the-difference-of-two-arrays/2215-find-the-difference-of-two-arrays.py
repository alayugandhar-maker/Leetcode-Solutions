class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        lst1=[]
        lst2=[]
        for i in nums1:
            if i not in nums2 and i not in lst1:
                lst1.append(i)
        for i in nums2:
            if i not in nums1 and i not in lst2:
                lst2.append(i)
        return [lst1,lst2]
        
        