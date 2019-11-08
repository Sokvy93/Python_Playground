from IPython.display import clear_output

def display_board(board):
  
  #to clear the output so it does not show the entire history of all the print funtions or print statements
  print('\n'*100)
  
  print(board[7]+'|'+board[8]+'|'+board[9])
  print(board[4]+'|'+board[5]+'|'+board[6])
  print(board[1]+'|'+board[2]+'|'+board[3])
