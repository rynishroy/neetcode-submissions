class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Handle cases where k is greater than the array length
        k = k % n 
        
        # 1. Reverse the entire array
        self.reverse(nums, 0, n - 1)
        # 2. Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        # 3. Reverse the rest of the elements
        self.reverse(nums, k, n - 1)
        
    def reverse(self, nums: list[int], start: int, end: int) -> None:
        # Correctly utilize the passed boundaries
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        