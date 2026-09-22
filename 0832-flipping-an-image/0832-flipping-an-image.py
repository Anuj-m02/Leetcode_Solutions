class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        
        n = len(image)
        new_mat = []

        for row in image :
            new_row = row[::-1]
            new_mat.append(new_row)
        
        for i in range(n):
            for j in range(n) :
                new_mat[i][j] = 1 - new_mat[i][j]
        
        return new_mat
