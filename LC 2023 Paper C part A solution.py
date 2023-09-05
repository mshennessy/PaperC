# Question 16(a)
# Examination Number:
from random import randint

# Function start
def guess_game(max_guesses_allowed,diff_level): #two values are passed in to function
    guess_count = 0
    user_guess = 0
    upper_limit = 5  # Default value is 5 (will be updated if user enters H)
    # (vi) Set up an empty list which we'll add to and check for duplicates
    guess_list = []
    # (v)
    if diff_level == 'H':
        # reset upper_limit
        upper_limit = 100
    secret_number = randint(1, upper_limit) # (iii)
    print(secret_number)    # For testing
    while (user_guess != secret_number) and (guess_count < max_guesses_allowed):
        user_guess = int(input("Enter your guess: "))
        # Check whether this number is already in the list (before we append it!)
        if user_guess in guess_list:
            print("You already guessed this number")
        # Could make the next line an else, ie don't append duplicates    
        guess_list.append(user_guess)
        
        guess_count += 1 #Increase guess_count by 1
        if user_guess == secret_number:
            print("Congratulations! You win!")
            # (i)
            print("You took", guess_count,"guesses.")
        # (ii)
        elif user_guess > secret_number:
            print("Sorry! Your guess was too high")
        else:
            print("Sorry! Your guess was too low")
#Function end (end of indentation)

# Main body of code - not indented
print("Welcome to the guessing game!")
# (iv)
num_guesses = int(input("Enter the maximum number of guesses allowed:"))
# (v)
level = input("Enter the difficulty E(asy) or H(ard):")

# Call the function and pass it two values
guess_game(num_guesses, level)







