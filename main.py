import random

word_list = ["testing", "solution", "one"]
chosen_word = random.choice(word_list)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"

print(placeholder)
game_over = False
lives = 6
while not game_over:
    guess = input("Choose a letter: ").lower()
    if not guess:
        continue

    is_right = False
    index = 0
    shown_list = list(placeholder)

    if guess in placeholder:
        print("Already found.")
        print(placeholder)
        continue

    for letter in chosen_word:
        if guess == letter:
            is_right = True
            shown_list[index] = letter

        index += 1

    placeholder = "".join(shown_list)
    if is_right:
        print(placeholder)
    else:
        lives -= 1

    if lives < 1:
        game_over = True
        print("You Loose")

    if "_" not in placeholder:
        game_over = True
        print("You win")
    else:
        print("Lives left: ", lives)




