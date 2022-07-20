# imports the main part of the project to determine what side the coin flips on
import random


headscount = 0
tailscount = 0


heads = 1 # 1 represents heads
tails = 0 # 0 represents tails

# assigns the variable coin with the number 1 or 0
for coins in range(100000): # you can change the number in the range() to change the amount of times it flips the coins
  coins = random.randint(0,1)
  
# if it flipped head it will add 1 point to the headscount
  if coins == heads:
    headscount = headscount + 1
    
# if it flipped tails it will add 1 point to the tailscount    
  elif coins == tails:
    tailscount = tailscount + 1

# tells you how many times it has flipped either heads or tails
print("Amount of times flipped heads:", headscount)
print("Amount of times flipped tails:", tailscount)
