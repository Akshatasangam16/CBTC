import random
options=("rock", "paper", "scissor")
player=None
computer = random.choice(options)
player = input("enter your choice from (rock, paper, scissor): ")
print(f"Player: {player}")
print(f"Computer: {computer}")
if ((computer=="rock" and player=="paper")or(player=="rock" and computer=="paper")):
    print("paper wins")
elif ((computer=="rock" and player=="scissor")or(player=="rock" and computer=="scissor")):
    print("rock wins")
elif ((computer=="paper" and player=="scissor")or(player=="paper" and computer=="scissor")):
    print("scissor wins")
else:
    print("its a tie")
