from bke import MLAgent, start, can_win

class MijnSpeler(MLAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = 1 
    if can_win(board, opponent_symbol):
      getal = getal - 1000
      return getal
      
    if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
  


	class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward