import art
import random
from game_data import data
from replit import clear

def roll_item():
  return random.choice(data)

def describe_item(item):
  """
  Returns a string containing item's name, description, and country
  """
  return f"{item['name']}, a {item['description']}, from {item['country']}"

def get_higher_followed_item(item_a, item_b):
  """
  Returns "a" if item_a has higher follower count and "b" otherwise
  """
  if item_a['follower_count'] > item_b['follower_count']:
    higher_follower_item = "a"
  else:
    higher_follower_item = "b"
  return higher_follower_item


def higher_lower(score=0, game_over=False):
  
  print(art.logo)
  
  #Keep score from previous rounds. Game over if wrong in previous round
  if score > 0 and not game_over:
    print(f"You're right! Current score: {score}\n")
  if game_over:
    print(f"Sorry, that's wrong. Your final score: {score}")
    return
    
  #Choose 2 items and reroll if duplicates
  item_a = roll_item()
  item_b = roll_item()
  while item_b == item_a:
    item_b = roll_item()

  #Get item with higher follower count
  higher_follower_item = get_higher_followed_item(item_a, item_b)

  #Describe items to player
  print("A: " + describe_item(item_a))
  print(art.vs + "\n")
  print("B: " + describe_item(item_b))
  print("")

  #Player guess
  player_guess = input("Which of the above has more followers? a/b: ").lower()
  if player_guess == higher_follower_item:
    clear()
    higher_lower(score+1)
  else:
    clear()
    higher_lower(score, True)

higher_lower()