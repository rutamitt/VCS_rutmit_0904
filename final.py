import random
import hangman_picture

one_list = []
two_list = []
three_list = []
letter_list = []
random_word = []
level = int
hangmanpics = hangman_picture.hangmanpics
guess = str
y = ''
n = ''
h = ''

# Lygio pasirinkimas tarp 1-3
def game():
    del one_list[0:10000]
    del two_list[0:10000]
    del three_list[0:10000]
    del letter_list[0:10000]
    del random_word[0:10000]
    i = 0
    print ("Welcome to Hangerman! Before you start please enter your preferences:")
    print (
        "Level 1 - a word contains 4 or less letters, level 2 - between 5 and 8 letters & level 3 - more than 8 letters")
    level = int(input("Enter your level:"))
    if 1 <= level <= 3:
        pass
    else:
        print 'Level is not available. Please choose 1-3'  # KAIP PADARYTI, KAD LEISTU IS NAUJO IVEST
    if level == 1:
        use = one_list
    elif level == 2:
        use = two_list
    elif level == 3:
        use = three_list

    mistakes = int(input("Enter maximum number (1-6) of possible mistakes: "))

    if mistakes not in range(7):
        print "Error! Maximum number of possible mistakes is 6"
    words_file = open("words.txt", "r")

    for word in words_file.readlines():
        word_length = word.__len__()
        if word_length <= 5:  # kodel cia reikia rasyti penkis o ne keturis, ty visur plius vienas
            one_list.append(word.strip())
        elif 6 <= word_length <= 9:
            two_list.append(word.strip())
        elif word_length >= 10:
            three_list.append(word.strip())  # faile words yra enteriai kurie atsivaziuoja kaip \n, strip juos nuima

    for word in random.choice(use):
        for letter in word:
            random_word.append(letter)
    hidden_string = list("-" * (random_word.__len__()))

    while mistakes > letter_list.__len__():
        guess = raw_input("Guess a letter: ")
        if guess in random_word:
            print (guess, "Correct!")
            u = 0
            for h in random_word:
                if h == guess:
                    hidden_string[u] = guess
                    print(hidden_string)
                u += 1
        else:
            letter_list.append(guess)
            print ("Incorrect :(")
            print(hangmanpics[7 - mistakes + i])
            i += 1


def finish():
    print 'game is over, do you want to try again?'
    end = str(input("Press 'y' for yes or 'n' for no: "))
    if end == y:
        game()
    else:
        print 'bye!'

game()

finish()

