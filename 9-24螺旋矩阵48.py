from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Handle empty matrix
        if not matrix or not matrix[0]:
            return []

        res: List[int] = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:
            # Traverse from left to right along the top row
            for j in range(left, right + 1):
                res.append(matrix[top][j])

            # Traverse down along the right column
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])

            # If there is more than one row and more than one column remaining,
            # traverse the bottom row and the left column
            if top < bottom and left < right:
                # Traverse from right-1 to left along the bottom row
                for j in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][j])

                # Traverse up from bottom-1 to top+1 along the left column
                for i in range(bottom - 1, top, -1):
                    res.append(matrix[i][left])

            # Move the boundaries inward
            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return res