class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        row, col = len(board), len(board[0])
        visited = set()
        def dfs(r,c,word_index,visited):


            if r < 0 or c < 0 or r >= row or c >= col:
                return False 

            if (r,c) in visited or board[r][c] != word[word_index]:
                return False

            if word_index == len(word)-1:
                return True

            visited.add((r,c))
            for dr, dc in directions:
                if dfs(r+dr,c+dc, word_index +1, visited):
                    return True 

            visited.remove((r,c))
            return False

        for i in range(row):
            for j in range(col):
                if dfs(i,j,0,visited):
                    return True

        return False
                

            
        