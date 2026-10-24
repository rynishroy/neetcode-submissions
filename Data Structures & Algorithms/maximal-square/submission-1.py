class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_edge = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r ==0 or c == 0:
                    max_edge = max(max_edge, int(matrix[r][c]))
                elif matrix[r][c] == '1':
                    matrix[r][c] = 1+min(int(matrix[r-1][c]), int(matrix[r][c-1]), int(matrix[r-1][c-1]))
                    max_edge = max(max_edge, matrix[r][c])
        return max_edge**2

        