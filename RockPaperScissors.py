player1_decision =int(input("Enter rock, paper or scissors: "))
player2_decision =int(input("Enter rock, paper or scissors: "))

if (player1_decision == player2_decision):
    print("Tie")
elif (player1_decision == rock and player2_decision==scissors):
    print("Player1 Wins")
elif (player1_decision == scissors and player2_decision==paper):
    print("Player1 Wins")
elif (player1_decision == paper and player2_decision==rock):
    print("Player1 Wins")


elif (player2_decision== rock and player1_decision==scissors):
    print("Player2 Wins")
elif (player2_decision== scissor and player1_decision==paper):
    print("Player2 Wins")
elif (player2_decision== paper and player1_decision==rock):
    print("Player2 Wins")
