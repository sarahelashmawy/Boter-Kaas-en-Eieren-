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

def main():
  print("\n" 
  "Boter, kaas en eieren! \n")

  #main start menu
  print(" \n"
  "Start menu \n"
  "1. Speel \n"
  "2. Train \n")
  
  y = input("Kies van de genoemde opties: ")
  
  while True:
    if y == "1":
      games()
    elif y == "2":
      training()
    else:
      print("\n"
      "Input is fout. Voer een geldig keuze in.\n")
      y = input("Kies van de genoemde opties: ")
  
def games():
#menu van welke spellen 
  print("\n"
  "1. 2 spelers \n"
  "2. Makkelijke level \n"
  "3. Moeilijke level \n"
  "4. Onmogelijke level \n"
  "5. Terug naar het start menu \n")

  x = input("Kies van de genoemde opties: ")
  
  while True:
    if x == "1": 
      print ("2 spelers \n")
      start()
    elif x == "2":
      print("Makkelijke level")
      start(player_o=my_random_agent)
    elif x == "3":
      print("Moeilijke Level")
      start(player_o=my_agent)
    elif x == "4":
      print("Onmogelijke level")
    elif x == "5":
      main()
    else:
      print("\n"
      "Input is fout. Voer een geldig keuze in.\n")
      x = input("Kies van de genoemde opties: ")
  

def training():
# menu van grafiek en training 
  print("\n"
  "1. Train je tegenstander \n"
  "2. Bekijk de validatie grafiek \n"
  "3. Terug naar het start menu \n")
  
  z = input("Kies van de genoemde opties: ")
    
  while True:
    if z == "1":
      print("Tegenstander trainen \n")
    elif z == "2":
      print("Validatie grafiek \n")
    elif z == "3":
      main()
    else:
      print("\n"
      "Input is fout. Voer een geldig keuze in.\n")
      z = input("Kies van de genoemde opties: ")
  
main()

