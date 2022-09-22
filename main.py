import random
from bke import EvaluationAgent, MLAgent, is_winner, opponent, train, load, start

class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    return random.randint(1,500)

my_random_agent = MyRandomAgent()

class MyAgent(MLAgent):
 def evaluate(self, board):
   if is_winner(board, self.symbol):
     reward = 1 
   elif is_winner(board, opponent[self.symbol]):
     reward = -1
   else:
     reward = 0
   return reward

my_agent = MyAgent()



#start menu

print(" \n"
"Start menu \n"
"1. 2 spelers \n"
"2. Easy level \n"
"3. Hard level \n ")

x = input("selection:")
if x =="1" or x ==" 1": 
  print ("2 spelers"
  "\n")
  start()
  
elif x == "2" or x ==" 2":
  print("Easy level")
  start(player_o=my_random_agent)
    
elif x == "3" or x == " 3":
  print("Hard Level")
  start(player_o=my_agent)

else: 
  print("input incorrect")
