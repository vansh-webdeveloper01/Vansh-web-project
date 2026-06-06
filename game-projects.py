import random

print("=============================================")
print("   WELCOME TO STONE, PAPER, SCISSORS!        ")
print("=============================================\n")

# 1. SETUP TOURNAMENT RULES (Using simple variables)
target_score = 0

# Loop until user enters a valid number greater than 0
while target_score <= 0:
    user_input = input("Enter the points needed to win the tournament (e.g., 3): ")
    
    if user_input.isdigit():
        target_score = int(user_input)
        if target_score <= 0:
            print("Please enter a number greater than 0.")
    else:
        print("Invalid input! Please enter a valid whole number.")

# Tracker/Flag variables
player_score = 0
computer_score = 0
round_number = 1

print(f"\nTournament started! First to reach {target_score} points wins the trophy.\n")
print("---------------------------------------------")

# 2. MAIN TOURNAMENT LOOP
# Runs continuously as long as NO ONE has reached the target score
while player_score < target_score and computer_score < target_score:
    print(f"\n--- ROUND {round_number} ---")
    print(f"Current Score -> Player: {player_score} | Computer: {computer_score}")
    
    # 3. INPUT VALIDATION LOOP
    player_choice = ""
    while player_choice != "stone" and player_choice != "paper" and player_choice != "scissors":
        player_choice = input("Choose your weapon (stone/paper/scissors): ").lower().strip()
        
        if player_choice != "stone" and player_choice != "paper" and player_choice != "scissors":
            print("Invalid choice! Please type 'stone', 'paper', or 'scissors'.")

    # 4. COMPUTER CHOICE GENERATION (Using simple conditional numbers)
    # 1 = Stone, 2 = Paper, 3 = Scissors
    random_num = random.randint(1, 3)
    computer_choice = ""
    
    if random_num == 1:
        computer_choice = "stone"
    elif random_num == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"

    print(f"Player chose   : {player_choice.upper()}")
    print(f"Computer chose : {computer_choice.upper()}")

    # 5. GAME LOGIC EVALUATION (Pure If-Elif-Else)
    if player_choice == computer_choice:
        print("It's a Tie for this round!")
        
    elif player_choice == "stone" and computer_choice == "scissors":
        print("Player wins this round!")
        player_score = player_score + 1
        
    elif player_choice == "paper" and computer_choice == "stone":
        print("Player wins this round!")
        player_score = player_score + 1
        
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player wins this round!")
        player_score = player_score + 1
        
    else:
        print("Computer wins this round!")
        computer_score = computer_score + 1
        
    round_number = round_number + 1
    print("---------------------------------------------")

# 6. TOURNAMENT CONCLUSION
print("\n=============================================")
print("               GAME OVER!                    ")
print("=============================================")

if player_score == target_score:
    print(f"******* Congratulations! You won the tournament by {player_score} to {computer_score}! *******")
else:
    print(f"******* The Computer won the tournament by {computer_score} to {player_score}. Better luck next time! *******")

print("=============================================")
print("Thank you for playing!")