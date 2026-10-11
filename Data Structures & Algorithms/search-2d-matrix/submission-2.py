class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        left, right = 0, (row*col) -1

        while (left<=right):
            mid = (left+right) //2
            mid_value =matrix[mid//col][mid%col]

            if mid_value == target:
                return True
            elif mid_value<target:
                left +=1
            else:
                right -=1
        return False
        