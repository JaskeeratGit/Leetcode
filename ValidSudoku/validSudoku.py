def containsDuplicate(l1: List[str]) -> bool:
        freqDict = {}
        for i in l1:
            if i in freqDict and i != '.':
                return True
            else:
                freqDict[i] = 1
        return False

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        indSquare = [[] for x in range(9)]
        cols = [[] for x in range(9)]
            
        for i in range(len(board)):
            if containsDuplicate(board[i]):
                return False
            for j in range(len(board)):
                cols[j].append(board[i][j])
                if i < 3:
                    if j < 3:
                        indSquare[0].append(board[i][j])
                    elif 2 <= j < 6:
                        indSquare[1].append(board[i][j])
                    elif 5 <= j < 9:
                        indSquare[2].append(board[i][j])
                if 3 <= i < 6:
                    if j < 3:
                        indSquare[3].append(board[i][j])
                    elif 3 <= j < 6:
                        indSquare[4].append(board[i][j])
                    elif 5 <= j < 9:
                        indSquare[5].append(board[i][j])
                if 6 <= i < 9:
                    if j < 3:
                        indSquare[6].append(board[i][j])
                    elif 3 <= j < 6:
                        indSquare[7].append(board[i][j])
                    elif 5 <= j < 9:
                        indSquare[8].append(board[i][j])
        for i in cols:
            if containsDuplicate(i):
                return False
        for i in indSquare:
            if containsDuplicate(i):
                return False
        return True
