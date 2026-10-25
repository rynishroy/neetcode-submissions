class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # Use l < r because we always compare m with m + 1
        while l < r:
            m = l + (r - l) // 2
            
            # If the right neighbor is greater, a peak must be on the right side
            if nums[m] < nums[m+1]:
                l = m + 1
            # Otherwise, the current element or something to its left is a peak
            else:
                r = m
                
        return l