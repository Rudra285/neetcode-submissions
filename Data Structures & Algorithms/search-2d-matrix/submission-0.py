class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in range(len(matrix)):
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                m -= 1
                for n in range(len(matrix[m])):
                    if matrix[m][n] == target:
                        return True
            elif m == len(matrix) - 1:
                for n in range(len(matrix[m])):
                    if matrix[m][n] == target:
                        return True
        return False