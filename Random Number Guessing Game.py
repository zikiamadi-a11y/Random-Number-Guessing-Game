import random
my_number=random.randint(0,50)
prompt=input("Welcome to my random number guessing game!: Press enter to start") 
range_of_numbers = input("Hint(My number is between 0 and 50): Press enter again")

def number_guess():
    guess = int(input("Guess my number: "))
    print("Your choice", guess)
    return guess
    
def guess_check(guess):
    while guess!= my_number:
        print("Wrong guess. Try again!")
        guess = int(input("Guess my number: "))
        if guess == my_number:
            print("You guessed correct. Hooray!")
        elif guess == my_number-3:
            print("So close! Try again.")
        elif guess == my_number+3:
            print("So close! Try again.")
        if guess == number_of_guesses:
            print("Game Over")
            

player_guess= number_guess()
check= guess_check(player_guess)
tries=number_of_guesses()

    
        
        