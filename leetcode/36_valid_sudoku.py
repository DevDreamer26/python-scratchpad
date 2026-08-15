from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True



# example_list =[
#     [1,2,3],
#     [1,3,2],
#     [2,3,1],
#     [2,1,3],
#     [3,1,2],
#     [3,2,1]
# ]


# Using nested loops:
# output =[]

# for i in example_list:
#     total = 0
#     for j in i:
#         total += j
#     output.append(total)
    
# print(output)

# Using sum() in built

# for i in example_list:
#     output.append(sum(i))

# print(output)
        