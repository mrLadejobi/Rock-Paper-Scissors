c1 = "rock"
c2 = "paper"
c3 = "scissors"
print("welcome to a game of rock, paper, scissors")

p1 = input("Player one, what is your choice: ")
p2 = input("Player two, what is your choice: ")

if p1 == "rock" and p2 == "scissors":
    print("player one wins with")
elif p1 == "scissors" and p2 == "rock":
    print(f"player two wins with")
elif p1 == "paper" and p2 == "scissors":
    print("player two wins")
elif p1 == "scissors" and p2 == "paper":
    print("player one wins ")
elif p1 == "paper" and p2 == "rock":
    print("player one wins")
elif p1 == "rock" and p2 == "paper":
    print("player two wins")
elif p1 == "rock" and p2 == "rock" or p1 == "paper" and p2 == "paper" or p1 == "scissors" and p2 == "scissors":
    print("It is a draw, go again")
else:
    print("Please enter a choice.")

