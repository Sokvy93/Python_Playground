from IPython.display import clear_output

def display_board(board):
  
  #to clear the output so it does not show the entire history of all the print funtions or print statements
  print('\n'*100)
  
  print(board[7]+'|'+board[8]+'|'+board[9])
  
  print(board[4]+'|'+board[5]+'|'+board[6])
  
  print(board[1]+'|'+board[2]+'|'+board[3])
  
  
  
#To write a function that can take in a player input and assign their markers as 'X' or 'O'.
#Think about using while loops to continually ask until you get a correct answer.

def player_input():
  
  marker = ''
  
  #KEEP AKSING PLAYER 1 TO CHOOSE X OR O 
  
  while marker != 'X' and marker != 'O':
    marker = input('Player 1, choose X or O: ')
  
  #ASSIGN PLAYER 2, THE OPPOSIT MARKER
  player1 = marker
  
  if player1 == 'X':
    player2 == 'O'
  else:
    player2 == 'X'
  
  return (player1,player2)

#Set it as a tuple so it will show which player has which marker later on. 
player1_marker, player2_marker = player_input()


