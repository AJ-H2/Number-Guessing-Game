import random
import csv 
import os
from datetime import datetime

difficulty_levels = {
	'easy': 10,
	'medium': 100,
	'hard': 1000
}

def get_username():
	while True:
		try:
			username = input("Please enter your username: ").strip()
			if len(username) < 2:
				print("Your username must be at least 2 characters.")
				continue
			if len(username) > 20:
				print("Your username cannot be greater than 20 characters.")
				continue
			if not username[0].isalpha():
				print("Your username must start with a letter.")
				continue
			if not username.replace("_", "").isalnum():
				print("Your username can only contain letters, numbers, and underscores.")
				continue
			return username
		except:
			print("There was an issue creating your username.")

def get_difficulty(username="friend"):
	while True:
		try:
			difficulty = input(f"Would you like to play on easy, medium, or hard difficulty {username}? ").lower()
			if difficulty not in difficulty_levels:
				print(f"Please select a valid difficulty.")
				continue
			return {
				'difficulty': difficulty,
				'max_range': difficulty_levels[difficulty]
			}
		except:
			print("Please select a valid difficulty.")

def get_guess(max_range = difficulty_levels['medium']):
	while True:
		try:
			guess = int(input(f"Guess a number between 1 and {max_range}: "))
			return guess
		except:
			print("Please select a valid number.")

def play_game(user='', attempts = 10):
	user = get_username() if not user.strip() else user
	difficulty = get_difficulty(user)

	random_number = random.randint(1, difficulty['max_range'])
	guesses = 0

	while True:
		attempts -= 1
		guesses += 1
		guess = get_guess(difficulty['max_range'])
		if guess == random_number:
			print(f'You got it in {guesses} guesses! You had {attempts} attempts left.')
			save_game(user, attempts, guesses, difficulty)
			break
		elif attempts <= 0:
			print("Sorry, you're out of attempts.")
			break
		elif guess < random_number:
			print(f"Too low! You have {attempts} attempts left.")
			continue
		elif guess > random_number:
			print(f"Too high! You have {attempts} attempts left.")
			continue

	play_again(user, 10)

def play_again(user='', attempts=10):
	if input("Would you like to play again (yes/no)?").lower() == 'Yes'.lower(): 
		play_game(user, attempts)
	else: 
		print("See you next time!")

def save_game(user, attempts, guesses, difficulty):
	date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	filename = 'results.csv'
	file_exists = os.path.exists(filename)

	with open('results.csv', 'a', newline="") as file:
		writer = csv.writer(file)

		if not file_exists:
			writer.writerow([
				"username",
				"attempts_left",
				"guesses",
				"difficulty",
				"datetime"
			])

		writer.writerow([
			user,
			attempts,
			guesses,
			difficulty['difficulty'],
			datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		])

	print("You're score has been recorded.")


play_game('', 10)
