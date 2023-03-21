# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

plays = {}

def player(prev_play, opponent_history=[]):
  global plays
  n = 5

  if prev_play in ["R", "P", "S"]:
    opponent_history.append(prev_play)

  # default to R
  guess = "R"

  # if there are more than n elements in opponent_history, set prev to the last n elements the opponent previously played
  # add 1 to n each turn
  if len(opponent_history) > n:
    n += 1
    prev = "".join(opponent_history[-n:])

    # if the opponent has played the last n + 1 moves more than once, add 1 to that specific combination
    # otherwise, assume it has only played it once
    if "".join(opponent_history[-(n + 1):]) in plays.keys():
      plays["".join(opponent_history[-(n + 1):])] += 1
    else:
      plays["".join(opponent_history[-(n + 1):])] = 1

    possible = [prev + "R", prev + "P", prev + "S"]

    
    for i in possible:
      if not i in plays.keys():
        plays[i] = 0

    predict = max(possible, key=lambda key: plays[key])

    if predict[-1] == "P":
      guess = "S"
    if predict[-1] == "R":
      guess = "P"
    if predict[-1] == "S":
      guess = "R"


  return guess

  # opponent_history.append(prev_play)

  # guess = "R"
  # if len(opponent_history) > 2:
    # guess = opponent_history[-2]
    
  # return guess

  # Determine the pattern (But how?)
  # Counter it
  
  # Quincy
  # Gets a counter
  # Adds 1 each turn
  # Plays the (counter % 5)th element in [R, R, P, P, S]

  # Mr. Ugesh
  # Gets the most frequently played element in the opponents last 10 moves
  # Plays the move that beats it

  # Kris
  # Beats the previous play from the opponent
  # If it's the first

  # Abbey
  # Has counters of all possible two-move combinations
  # Keeps track of the opponent's previous plays
  # If there are none, it assumes the previous play was R
  # Gets the last two of the opponent's plays
  # Has 3 guesses based on what the opponent last played

# I got stuck here for a long time
# I resorted to looking for archived forums and being inspired by the solution there
# Thank you to Mikw on https://forum.freecodecamp.org/t/machine-learning-with-python-projects-rock-paper-scissors/412794/3