class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        total = len(matrix) * len(matrix[0])
        start = 0
        end = total - 1

        while start <= end:
            mid_index = start + (end - start)//2
            val = mid_index // len(matrix[0])
            mid = matrix[val][mid_index % len(matrix[0])]

            if mid == target:
                return True
            elif mid > target:
                end = mid_index - 1
            else:
                start = mid_index + 1
        return False