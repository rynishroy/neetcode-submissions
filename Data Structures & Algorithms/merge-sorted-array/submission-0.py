class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1
        p2 = n - 1
        insert = m + n - 1

        # Merge elements starting from the back
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[insert] = nums1[p1]
                p1 -= 1
            else:
                nums1[insert] = nums2[p2]
                p2 -= 1
            insert -= 1

        # If elements remain in nums2, copy them over
        # (If elements remain in nums1, they are already in their correct places)
        while p2 >= 0:
            nums1[insert] = nums2[p2]
            p2 -= 1
            insert -= 1


        