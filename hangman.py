import random

print("Welcome to Hangman!")

words = ["hacker", "bounty", "random"]
secret_word = random.choice(words) # random.choice() picks a random item from a list
print("You get 5 guesses")
display_word = []
for letter in secret_word:
    display_word += "_"  # display_word.append("_")
print(display_word)

num = 0
game_over = False

while not game_over:
    guess = input("Guess a letter ").lower()
    for position in range(len(secret_word)): # range(5) -> [0, 1, 2, 3, 4]	
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word: # if guess is not in secret_word
        num += 1
        guesses_left = 5 - num
        print(f"You have {guesses_left} guesses left")
        if num >= 5:
            print("You Loser")
            game_over = True
    print(display_word)

    if "_" not in display_word: # if "_" is not in display_word
        print("You Win")
        game_over = True
