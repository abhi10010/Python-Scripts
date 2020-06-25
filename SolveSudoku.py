board = [
    [0,0,8,0,0,7,9,0,0],
    [0,4,2,0,0,5,0,0,0],
    [0,0,0,6,0,0,0,5,0],
    [0,0,3,0,0,6,8,0,1],
    [0,0,0,0,0,0,0,0,6],
    [9,0,0,0,7,0,0,0,0],
    [0,8,0,1,3,0,4,7,0],
    [0,0,0,0,9,0,0,0,0],
    [0,1,0,0,0,0,0,0,0]
]                                        # Enter Your Sudoku Board

def find_empty(board):                   # Find Empty Position
  
  for i in range(len(board)):
    
    for j in range(len(board)):
      if board[i][j] == 0:
        return i, j
  
  return None

def check_num(board, num, pos):         # Check if the number is in the valid position or not
  
  for i in range(len(board[0])):
    if board[pos[0]][i] == num and i != pos[1]:
      return False
  
  for i in range(len(board)):
    if board[i][pos[1]] == num and i != pos[0]:
      return False

  box_r = pos[0] // 3
  box_c = pos[1] // 3

  for i in range(box_r * 3, box_r * 3 + 3):
    
    for j in range(box_c * 3, box_c * 3 + 3):
      if board[i][j] == num and (i, j) != pos:
        return False
  
  return True

def solve_board(board):                  # Driver function to solve the board
  
  pos = find_empty(board)
  if not pos:
    return True
  
  else:
    row, col = pos

  for i in range(1,10):
    if check_num(board, i, (row, col)):
      board[row][col] = i
    
      if solve_board(board):
        return True
    
      board[row][col] = 0
  
  return False

def print_board(board):                   # Print the board
  
  for i in range(len(board)):
    if i%3 == 0 and i != 0:
      print('- - - - - - - - - - ')
    
    for j in range(len(board[0])):
      if j%3 == 0 and j != 0:
        print('|', end = '')

      if j == 8:
        print(board[i][j])
      
      else:
        print(str(board[i][j]) + " ", end="")


print_board(board)
solve_bo(board)
print("\n____________________\n\n")
print_board(board)
