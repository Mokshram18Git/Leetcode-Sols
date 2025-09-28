class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """


        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]


        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row[i]:
                    return False
                else:
                    row[i].add(board[i][j])

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in col[j]:
                    return False
                else:
                    col[j].add(board[i][j])


        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == '.':
                    continue
                box_index = 3*(i//3)+j//3
                if board[i][j] in box[box_index]:
                    return False
                else:
                    box[box_index].add(board[i][j])

        return True

    