class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        count=set()
        for i in nums1:
            count.add(i)
        for i in nums2:
            if i in count:
                return i
        return -1
        
        