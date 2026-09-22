# class Solution:
#     def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        
#         n = len(image)
#         new_mat = []

#         for row in image :
#             new_row = row[::-1]
#             new_mat.append(new_row)
        
#         for i in range(n):
#             for j in range(n) :
#                 new_mat[i][j] = 1 - new_mat[i][j]
        
#         return new_mat

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            
            while left <= right:
                if left == right:
                    # Middle element in an odd-length row just needs to be inverted
                    row[left] = 1 - row[left]
                else:
                    # Swap and invert elements simultaneously
                    row[left], row[right] = 1 - row[right], 1 - row[left]
                
                left += 1
                right -= 1

        return image