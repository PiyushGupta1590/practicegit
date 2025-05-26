import random
import time

def light_game():
  print("Welcome to the Light Game!")
  print("Wait for the light to turn green, then press Enter as fast as you can!")
  print("If you press too early, you lose!")
  input("Press Enter to start...")

  # Random delay before the light turns green
  delay = random.uniform(2, 5)
  print("Get ready...")
  time.sleep(delay)

  print("GREEN LIGHT! Press Enter NOW!")
  start_time = time.time()

  # Wait for user input
  input()
  reaction_time = time.time() - start_time

  if reaction_time < 0.1:  # Pressed too early
    print("You pressed too early! You lose!")
  else:
    print(f"Your reaction time was {reaction_time:.3f} seconds!")
    if reaction_time < 0.3:
      print("Amazing reflexes!")
    elif reaction_time < 0.6:
      print("Good job!")
    else:
      print("You can do better!")

if __name__ == "__main__":
  light_game()