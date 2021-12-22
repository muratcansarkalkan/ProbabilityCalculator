import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **colors):
  # Used double asterisk before colors, because we don't know how many arguments would be placed inside.
    self.contents = []
    # Empty list
    for x, y in colors.items():
      self.contents += y * [x]

      # adds y times of x
  # Randomly select num of balls, then remove them from contents. Return selected balls
  def draw(self, num):
    try:
      balls = random.sample(self.contents, num)
    except:
      balls = copy.deepcopy(self.contents)
    
    for n in balls:
      self.contents.remove(n)
    return balls
    # for n in range(num):
    # ball = random.choice(contents)

    # self.num = num_balls_drawn

hat = Hat(red=5, orange=4)
hat.draw(3)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls = hat_copy.draw(num_balls_drawn)

    #  balls match expec?
    eb_list = []
    for x, y in expected_balls.items():
      eb_list += y * [x]

    if contains_balls(eb_list, balls):
      M += 1

  probability = M / num_experiments
  return probability

def contains_balls(expected_balls, actual_balls):
  for b in expected_balls:
    if b in actual_balls:
      actual_balls.remove(b)
    else:
      return False
  return True
