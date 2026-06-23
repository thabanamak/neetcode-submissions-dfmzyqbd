class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows = len(image)
        cols = len(image[0])
        original = image[sr][sc]
        if original == color:
            return image


        def dfs(r,c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != original):
                return

            image[r][c] = color

            for dr, dc in directions:
                dfs(r+dr,c+dc)


        dfs(sr,sc)
        return image

        