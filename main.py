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
my_agent = load("MyAgent_3000")

my_agent.learning = True


print(" \n"
"Start menu \n"
"1. Play \n"
"2. Train \n")

while True:
    y = input("Selection: ")

    if y == "1" or y == "2":
      break
    else:
      print("Input incorrect. Please enter a valid choice.\n")
  

if y =="1" or y ==" 1":
  print("\n"
  "1. 2 players \n"
  "2. Easy level \n"
  "3. Hard level \n"
  "4. Impossible level \n")

  while True:
    x = input("selection:")

    if x == "1" or x == "2" or x == "3" or x == "4":
      break
    else:
      print("Input incorrect. Please enter a valid choice.\n")
  
  
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
  elif x == "4" or x == " 4": 
    print("Imposssible level")

elif y =="2" or y ==" 2":
  print("\n"
  "1. Train your opponent \n"
  "2. View validation graph\n")
  
  while True:
    z = input("selection:")
    
    if z == "1" or z == "2":
      break
    else:
      print("Input incorrect. Please enter a valid choice.\n")
  
  



