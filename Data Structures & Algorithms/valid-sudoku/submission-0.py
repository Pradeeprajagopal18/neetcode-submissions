class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)] #because 9 in the max as sudoku size 9 * 9
        colm = [set() for _ in range(9)] #because 9 in the max as sudoku size 9 * 9
        boxes = {} # empty dict
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                box = (r//3,c//3)
                if box not in boxes:
                    boxes[box] = set()
                
                if value in rows[r]:
                    return False
                if value in colm[c]:
                    return False
                if value in boxes[box]:
                    return False
                rows[r].add(value)
                colm[c].add(value)
                boxes[box].add(value)
        return True      