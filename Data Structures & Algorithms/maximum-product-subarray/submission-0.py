class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ##currMax and currMin is because of the -negative nuber and n is the max/min number 
        #could be n itself
        res =max(nums)
        currMax, currMin = 1,1
        for n in nums:
            if n==0:
                currMax, currMin = 1, 1
                continue
            tmp = currMax*n
            currMax = max(currMax *n, currMin*n, n)
            currMin = min(tmp, currMin*n, n)
            res = max(res, currMax, currMin)
        
        return res

