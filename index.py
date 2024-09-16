
row_col  = 20
import random
import math
import os

words_to_guess= [

        { 
            "hint": "The word is a verb",
            "word":'Walk' 
        },

        {
            "hint":"It is used to heat up food",
            "word":"Microwave"
        },
        {
            "hint":"A music genre",
            "word":"Jazz"
        },
        {
            "hint":"Someone who made a career in music",
            "word":"Musician"
        },
        {
            "hint":"An italian dish",
            "word":"Pizza"
        },
        {
            "hint":"a soft breeze",
            "word":"Zephyr"
        },
        {
            "hint":"Automated music playing device",
            "word":"Jukebox"
        },
        
]


random_word =  math.floor(random.random() * len(words_to_guess))
guesed_words = []

hangman_ui = [
    {
        "display": False,
        "Type":"Rope",
        "x":[1, 2, 3, 4],
        "y": [9, 9, 9, 9]
    },
    {
        "display": False,
        "Type":"Head",
        "x":[5, 5, 6, 6, 7, 7, 8, 8 ],
        "y": [8, 10, 6, 12, 6, 12, 8, 10]
    },

    {
        "display": False,
        "Type":"Body",
        "x":[9, 10, 11, 12, 13],
        "y": [9, 9, 9, 9, 9]
    },
    {
        "display": False,
        "Type":"Hands",
        "x":[11, 11, 11, 11, 11, 11],
        "y": [5, 6, 7, 11, 12, 13]
    },
    {
        "display": False,
        "Type":"Feet",
        "x":[14, 14, 15, 15, 16, 16, 17, 17],
        "y": [8, 10, 7, 11, 6, 12, 5, 13]
    },
]



'Draw a grid with x as rows and y as columns '
def Draw(word, hangman_ui):
    for x in range(row_col):
        for y in range(row_col):
            print_str = True

            "this draws the grid borders"
            if x == 0 or x == row_col - 1 or y == 0 or y == row_col - 1 :
                print("#", end='')
                continue
                
        
            for item in hangman_ui:
                if item["display"] == True:
                    for i in range(len(item["x"])):
                        if x == item["x"][i] and y == item["y"][i]:
                            print("#", end='')
                            print_str = False

            if print_str == False:
                continue
                
            
            print(" ", end='')
            
        print()



    'draw the interface that shows how many letters the word has'
    print("Hint:", word[1] )

    for i in range(len(word[0])):
        if guesed_words[i] == True:
            print(word[0][i], end='')
            print("  ", end='')
        else:
            print("___", end='')
            print(' ', end='')





def Choose_random_word():
    choosen_word = words_to_guess[random_word]

    for x in range(len(choosen_word["word"])):
        guesed_words.append(False)

    return [choosen_word["word"], choosen_word["hint"]]
    



def Hangman():
    word = Choose_random_word()
    is_game_running = True

    while is_game_running:
        os.system('cls' if os.name == 'nt' else 'clear')
        Draw(word, hangman_ui)
        
        print()
        print()
        print()
        print()

        if all(guesed_words):
            is_game_running = False

            

        letter = input("Guess the next letter of the word: ")
        if len(letter) <= 0 or len(letter) > 1:
            continue

        sum  = []
        for item in hangman_ui:
            sum.append(item["display"])

        if all(sum):
            is_game_running = False



        'if all the letters in the word has been guessed corretly terminate the game'
        if letter.lower() in word[0].lower():
            for i in range(len(word[0])):
                if letter.lower() == word[0][i].lower():
                    guesed_words[i] = True
        else:
            for item in hangman_ui:
                if item["display"] == False:
                    item["display"] = True
                    break
        

        

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Game Over!!!")

Hangman()






    
