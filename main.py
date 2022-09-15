import random
from bke import EvaluationAgent, OptimalEvaluationAgent, can_win, start

#twee tegenstanders
start()

#dom speler 
class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    return random.randint(1,500)

my_random_agent = MyRandomAgent()
start(player_o=my_random_agent)

#ietjes slimmer speler
class MijnSpeler(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = 1
    if can_win(board, opponent_symbol):
      getal = getal - 1000
      return getal

mijn_speler = MijnSpeler()
start(plyer_o=mijn-speler)

class MedAgent(OptimalEvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    

  














