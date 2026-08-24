class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        n , m = len(image) , len(image[0])
        
        dirs = [(1,0) , (0,1) , (-1,0), (0,-1)]

        orig_color = image[sr][sc]

        if orig_color == color :
            return image

        queue = deque([(sr , sc)])
        # image[sr][sc] = color

        while queue :
            curr_row , curr_col = queue.popleft()
            image[curr_row][curr_col] = color

            for dx , dy in dirs :
                new_row , new_col = curr_row + dx , curr_col + dy
                if 0 <= new_row < n and 0 <= new_col < m :
                    if image[new_row][new_col] == orig_color :
                        # image[new_row][new_col] = color
                        queue.append((new_row , new_col))
        
        return image

