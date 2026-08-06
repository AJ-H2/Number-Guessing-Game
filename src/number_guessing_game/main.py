import random
import csv

# Variable Definitions
difficulties = {
	"easy": 10,
	"medium": 100,
	"hard": 1000
}

# Function Definitions
def validate_input(input):
	if type(input) == int:
		return input 
	else:
		print('Please enter a valid number.')

def get_difficulty(user):
	while True:
		try:
			user_selected_difficulty = input(f"Would you like to play on hard, medium, or easy difficulty {user}? ").lower()
		except ValueError:
			print("Please choose a valid difficulty.")
			continue

		if user_selected_difficulty not in difficulty:
			print("Please choose a valid difficulty mode.")
			continue
		else:
			return difficulties[user_selected_difficulty]

def get_user():
	user = str(input("Please enter your username: "))
	return user









# Program Start
user = get_user()
difficulty = get_difficulty(user)
secret_number = random.randint(1, difficulty)
attempts = 10
guesses = 0

while attempts: 
	try:
		guess = int(input(f"Guess a number between 1 and {difficulty}: "))
	except ValueError:
		print("Please enter a valid number.")
		continue

	attempts -= 1
	guesses += 1

	if guess == secret_number:
		print(f'You got it in {guesses} guesses! You had {attempts} attempts left!')
		break
	elif guess < secret_number:
		print(f'Too low! You have {attempts} attempts left.')
	elif guess > secret_number:
		print(f'Too high! You have {attempts} attempts left.')

	if attempts == 0 and guess != secret_number:
		print("You've exhausted your attempts!")
		play_again = input("Would you like to play again? Yes or No").lower()
		if play_again == 'yes':
			continue
		else:
			break


