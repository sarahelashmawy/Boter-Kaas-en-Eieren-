import random
from bke import EvaluationAgent, MLAgent, RandomAgent, train_and_plot, is_winner, opponent, train, load, save, start

class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    return random.randint(1,500)


class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward


my_random_agent = MyRandomAgent()
  
my_agent = MyAgent(alpha=0.9, epsilon=0.2)
my_agent = load('MyAgent_6000')
my_agent.learning = True
  
random.seed(1)
random_agent = RandomAgent()

  
def main():
  print("\n" 
  "Boter, kaas en eieren! \n")

#main start menu
  print(" \n"
  "Start menu \n"
  "1. Spelen \n"
  "2. Trainen en valideren \n")
  
  y = input("Kies van de genoemde opties: ")
  
  if y == "1":
    menu()
  elif y == "2":
    while True:
      train_and_plot(
        agent=my_agent,
        validation_agent=random_agent,
        iterations=50,
        trainings=500,
        validations=1000)
  else:
    print("\n"
          "Input is fout. Voer een geldig keuze in.\n")
    main()



def menu():
#menu van welke spellen 
  print("\n"
  "1. 2 spelers \n"
  "2. Makkelijke level \n"
  "3. Moeilijke level \n"
  "4. Terug naar het start menu \n")

  x = input("Kies van de genoemde opties: ")
  
  if x == "1": 
    while True:
      print ("2 spelers \n")
      start()
    
      print("Wil je opnieuw spelen? \n"
          "1. Ja \n"
          "2. Nee \n"
          "3. Terug naar menu. \n")
      z = input("Keuze: ")
      if z == "1":
        continue  
      elif z == "2":
        print("Doei!")
        break 
      elif z =="3":
        menu()  
    
  elif x == "2":
    while True:
      print("Makkelijke level")
      start(player_o=my_random_agent)

      print("Wil je opnieuw spelen? \n"
          "1. Ja \n"
          "2. Nee \n"
          "3. Terug naar menu. \n")
      z = input("Keuze: ")
      if z == "1":
        continue  
      elif z == "2":
        print("Doei!")
        break
      elif z =="3":
        menu()
      
  elif x == "3":
    while True:
      print("Moeilijke Level")
      start(player_o=my_agent)

      print("Wil je opnieuw spelen? \n"
          "1. Ja \n"
          "2. Nee \n"
          "3. Terug naar menu. \n")
      z = input("Keuze: ")
      
      if z == "1":
        continue  
      elif z == "2":
        print("Doei!")
        break
      elif z =="3":
        menu()  
  
  elif x == "4":
    main()
  else:
    print("\n"
    "Input is fout. Voer een geldig keuze in.\n")
    menu()
  
main()

