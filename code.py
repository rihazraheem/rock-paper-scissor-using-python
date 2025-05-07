
import random

# Print game rules
print('Rules of ROCK PAPER SCISSORS game:\n'
      + "rock beats scissors \n"
      + "scissors beats paper \n"
      + "paper beats rock \n"
      +"tie if same \n")

while True:

    print("Enter your choice \n 1) Rock \n 2) Paper \n 3) Scissors \n")

    # Take the input from user
    
    user_choice = int(input("Enter your choice 1,2 or 3: "))

    # Looping if the user enters invalid input
    
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input('Enter a valid choice please ☺: '))

    # Initialize value of user_choosed variable corresponding to the choosen value
    
    if user_choice == 1:
        user_choosed = 'Rock'
    elif user_choice == 2:
        user_choosed = 'Paper'
    else:
        user_choosed = 'Scissors'

    # Print user choice
    
    print('User choice is:', user_choosed)
    print("Now it's Computer's Turn to choose:")

    # Computer chooses randomly any number among 1, 2, and 3
    
    computer_choice = random.randint(1, 3)

    # Initialize value of comp_choice_name variable corresponding to the choice value
    
    if computer_choice == 1:
        computer_choosed = 'Rock'
    elif computer_choice == 2:
        computer_choosed = 'Paper'
    else:
        computer_choosed = 'Scissors'

    print("Computer choice is:", computer_choosed)
    print('The game is between',user_choosed, 'vs', computer_choosed)

    # Determine the winner
    
    if user_choice == computer_choice:
        result = "DRAW"
    elif (user_choice == 1 and computer_choice == 2) or (computer_choice == 1 and user_choice == 2):
        result = 'Paper'
    elif (user_choice == 1 and computer_choice == 3) or (computer_choice == 1 and user_choice == 3):
        result = 'Rock'
    elif (user_choice == 2 and computer_choice == 3) or (computer_choice == 2 and user_choice == 3):
        result = 'Scissors'

    # Print the result
    
    if result == "DRAW":
        print("It's a tie!")
    elif result == user_choosed:
        print(user_choosed,'wins \n' "User wins!")
    else:
        print("Computer wins!")

    # Ask if the user wants to play again
    
    print("Do you want to play again? (Y/N)")
    answer = input()
    if answer == 'n':
        break

# After coming out of the while loop, print thanks for playing
        
print("Thanks for playing!")
