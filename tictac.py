#My first python program /TICTACTOE

class TicTac:
    
    def __init__(self):
        self.board = []
      
    def create_board(self):
      for i in range(3):
        row = []
        for j in range(3):
          row.append('_')
        self.board.append(row)
   
    def fix_spot(self,row ,col , player):
      self.board[row][col] = player
   
   
    def check_win(self,player ):
      win = 0
      num = 3
   
      #Check rows
      for row in range(num):
        win = True
        for j in range(num):
          if self.board[row][j] != player:
            win = False
            break
        if win == True:
          return True
   
   
       #check cols
      for col in range(num):
        win = True
        for row in range(num):
         if self.board[row][col] != player :
            win = False
            break
        if win == True:
          return True
   
   
        #Check diagonals
        for i in range(num):
          win = True
          if self.board[i][i] != player or self.board[i][num-1-i] != player:
            win = False
            break
        if win == True:
          return True

    def check_full_board(self):
      for row in self.board:
        for col in row:
          if col == "_":
            return False
      return True
    def swap_player(self,player):
      if player == 'X':
        return 'O'
      else:
        return 'X'
   
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start_game(self):
      self.create_board()
      player = "X"
      while True:
          print('Player {} turn!'.format(player))
          
          self.show_board()

          row,col = map(int, input("Enter row and column numbers to fix spot: ").split())
          print()

          self.fix_spot(row-1,col-1,player)
 
          if self.check_win(player):
            print('Player {} win!'.format(player))
            break
          if self.check_full_board():
            print('Draw!')
            break
          player = self.swap_player(player)
      print()
      self.show_board()

#Starting game

tictac = TicTac()
tictac.start_game()










