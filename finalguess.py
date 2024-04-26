import random

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            num = int(input(prompt))
            if num < min_val or num > max_val:
                print("Number must be between", min_val, "and", max_val)
                continue
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    num1 = 1 
    num2 = 100 
    num3 = random.randint(num1, num2)
    tries = 1 
    
    while True:
        numIn = get_valid_input("Guess a number between " + str(num1) + " and " + str(num2) + ": ", num1, num2)
        if numIn > num3:
            print("Your guess is too high. Try again.")
            num2 = numIn - 1
        elif numIn < num3:
            print("Your guess is too low. Try again.")
            num1 = numIn + 1
        else:
            print("\nCongratulations! You guessed", numIn)
            print("It took you", tries, "tries.")
            return tries
        tries += 1 

def main():
    wins = 0
    total_tries = 0
    
    while True:
        tries = play_game()
        total_tries += tries
        wins += 1
        print("Total wins:", wins)
        print("Total tries:", total_tries)
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Goodbye!")
            break
main()