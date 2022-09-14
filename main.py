import random 
from bke import EvaluationAgent, start

class MyRandomagent (EvaluationAgent):
  def evaluate(self, board, my_symbol, oppponent_symbol): 
    return random.randint(1,500)

my_random_agent = MyRandomagent()
start(player_o=my_random_agent, player_x=my_random_agent)