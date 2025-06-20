import random

easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("Welcome to the password guessing game")
print("Choose a difficulty level: easy, medium or hard : ")

level = input("Enter the difficulty : ").strip().lower()
if level == 'easy':
    secret = random.choice(easy_words)
elif level == 'medium':
    secret = random.choice(medium_words)
elif level == 'hard':
    secret = random.choice(hard_words)
else :
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password")

while True:
    guess = input("Enter your guess: ").strip().lower()
    attempts += 1
    if guess == secret:
        print(f"Congratulations! you guess the right!!! you guess in {attempts} attempts")
        break
    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else :
            hint += '_'
    print("HINT=", hint)
print("GAME OVER")






