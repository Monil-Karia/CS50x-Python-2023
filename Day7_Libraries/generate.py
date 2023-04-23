import random 

#[] represents thatt they are in the list 
coin = random.choice(["Heads" , "tails"])

print(f"Printing heads or tails : {coin}")

number = random.randint(1,10)
print(f"Printing any random number between 1-10 : {number}") 

cards = ["King" , "Queen" , "Jack" ]
random.shuffle(cards)
print(f"We are printing the List cards having jack , king and queen in it : {cards}")