import random
from bke import EvaluationAgent, MLAgent, RandomAgent, train_and_plot, is_winner, opponent, train, load, save, start


def main():
  print("\n" 
  "Boter, kaas en eieren! \n")

#main start menu
  print(" \n"
  "Start menu \n"
  "1. Spelen \n"
  "2. Trainen en valideren \n")
  
  y = input("Kies van de genoemde opties: ")
  
  while True:
    if y == "1":
      games()
    elif y == "2":
      train_and_plot(
        agent=my_agent,
        validation_agent=random_agent,
        iterations=50,
        trainings=500,
        validations=1000)
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
  "4. Terug naar het start menu \n")

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
      main()
    else:
      print("\n"
      "Input is fout. Voer een geldig keuze in.\n")
      x = input("Kies van de genoemde opties: ")
  

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

my_agent = load('MyAgent_6000')
my_agent.learning = True

random.seed(1)
random_agent = RandomAgent()


main()

