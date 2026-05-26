class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        #row iteration
        for row in board:
            seen_row = set() 
            for cell in row:
                if cell == ".":
                    continue
                if cell in seen_row:
                    return False 
                seen_row.add(cell) 
        #col iteration
        for col in range(9):
            seen_col = set()
            for row in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue 
                if cell in seen_col:
                    return False 
                seen_col.add(cell)
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for row in range(box_row * 3, box_row * 3 + 3):
                    for col in range(box_col * 3, box_col * 3 + 3):
                        cell = board[row][col]
                        if cell == ".":
                            continue
                        if cell in seen:
                            return False 
                        seen.add(cell)
        return True
                
            
        
        