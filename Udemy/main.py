import random
lives = 6
word_list = ["integer", "boolean", "camel"]

#Todo .1 :- Randomly choose  word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# Todo.4 :- Create s "placeholder" with the same number of blanks as the chosen_word.
placeholder = ""
w_len = len(chosen_word)
for pos in range(w_len):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""
    for letter in chosen_word:
        if letter ==  guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True
            print("You Loose.")

    if "_" not in display:
        game_over = True
        print("You win.")
    print("Left lives : ", lives)