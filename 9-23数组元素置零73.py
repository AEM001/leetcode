from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0]) if m else 0

        # 标记第一列是否需要置零（避免被第一行/第一列的标记相互覆盖）
        col0 = False

        # 第一趟：用第一行和第一列作为标记位
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 第二趟：从底向上，根据标记置零，避免过早覆盖标记
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0:
                matrix[i][0] = 0