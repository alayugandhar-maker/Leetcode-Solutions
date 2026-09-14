class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        n=len(nums)
        l,r=0,0
        add=0
        count=0

        while r<n:
            add+=nums[r]
            avg=0

            if r-l+1==k:
                avg=add/k

                if avg>=threshold:
                    count+=1 
                add-=nums[l]
                l+=1
            r+=1
        return count

        