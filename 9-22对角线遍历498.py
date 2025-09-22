from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        row = len(mat)
        col = len(mat[0])
        res = []
        total = row * col
        row -= 1
        col -= 1
        x = 0
        y = 0
        L = 1
        for i in range(total):
            res.append(mat[x][y])
            
            if L:
                y+=1
                x-=1
                if y>col:
                    y-=1
                    x+=2
                    L=0
                elif x<0:
                    x+=1
                    L=0
            else:
                x+=1
                y-=1
                if x>row:
                    x-=1
                    y+=2
                    L=1
                elif y<0:
                    y+=1
                    L=1
        return res

   
