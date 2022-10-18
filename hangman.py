from random import choice

random_word = ['elephant', 'luxury', 'subway', 'transcript', 'stronghold','jawbreaker', 'whiskey']

alaphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def computer_random_choice(word):
    random_word = choice(word)
    return random_word

    
        
def ask_a_letter():

    user_choice = input("Guess a letter. ").lower()
    while user_choice not in alaphabet:
        print('Choose a valid letter!')
        user_choice = input("Try again. Guess a letter. ")
        print(user_choice)
    return user_choice


def check_letter_in_word(word):
    lives = 6
    score = 0
    wrong_letters = []
    computer_choice = [x.lower() for x in word]
    temp_string = ""
    x = True
    correct_letters = []


    print("   _________   ")
    print("   |        O")
    print("   |       \|/")
    print("   |        |")
    print("   |       / \  ")
    print("   |   ")
    print("___|___")
    print(" ")
    print("Welcome to Hangman! You have 6 tries to guess the correct word! Good luck!")
    print("Here is your word below:")
    print(f"There are {len(word)} letters in the word")
    print('')
    reveal = "_"*len(word)
    print(reveal)
  
    while x == True:
        # dashes_for_word(word, letter_guess=None)
        user_choice = ask_a_letter()
        
        if user_choice in wrong_letters or user_choice in correct_letters:
            print('already guessed that letter, try another one')
            
        elif user_choice in computer_choice:
            word = [x for x in word]
            # reveal = "_"*len(word)
            temp_string = ""
            correct_letters.append(user_choice)
            # reveal2 = "_"*len(word)
            
    # checker = reveal[0] + "_" + "_" + "_" + "_"
    # letters = []
            
            guesses = {}
            for i, v in enumerate(word):
                guesses[v] = '_'
                if v == user_choice:
                        temp_string += user_choice
                        score += 1
                else:
                    temp_string +=reveal[i]
            
            
            reveal = temp_string
            print(reveal)
        elif user_choice not in wrong_letters:
            wrong_letters.append(user_choice)
            print(f'Wrong letter list: {wrong_letters}')
            print(f'Remaining lives is: {lives - 1}')
            lives -= 1

        if lives == 0:
            print(f'Game over! You have {lives} remaining!')
            break


        if score == len(word):
            print(f"You won! Good job you guessed the correct word!")
            break
        else:
            continue
            
    
def word_revealer(word, letter):

    show = []
    for i, v in enumerate(word):
        if letter == v:
            dashes = v.replace('__', v)
            show.append(dashes)
            print(show)

def dashes_for_word_test(word):

    word = [x for x in word]
    #     # print("_")
    # print(letters)
    letters = []
    word_count = 0 
    spaces = 0
    guesses = {}
    while word_count < len(word) + 1 and spaces < len(word):
        
        for i, v in enumerate(word):
            dashes = v.replace(v, '__')
            letters.append(dashes)
            guesses[v] = '_'
            spaces += 1
        for w, x in enumerate(word):


            letter_guess = ask_a_letter()
            print(letters)
            # print(i)
            if letter_guess == x:
                letters.insert(w, letter_guess)
                letters.pop()
                word_count += 1


        # print(i, v)

    print(letters) 
    print(guesses)  

    



the_word = computer_random_choice(random_word)


def dashes_for_word_test2(word, letter):
    word = [x for x in word]
    reveal = "_"*len(word)
    # reveal2 = "_"*len(word)
    temp_string = ""
    # checker = reveal[0] + "_" + "_" + "_" + "_"
    # letters = []
    guesses = {}
    for i, v in enumerate(word):
        guesses[v] = '_'
        if v == letter:
            temp_string += letter
            
        else:
            temp_string +=reveal[i]
            

    # print(temp_string)
    # print(reveal)
    reveal = temp_string
    # reveal2 = checker

    print(reveal)
    print([guesses, reveal])
    # print(reveal2)
    # print(len(reveal))
      
        # if letter == v:
        #     letters.append(v)

        #     #not sure yet about the append part here! 
            
        # else:
        #     dashes = v.replace(v, '__')
        #     letters.append([dashes, i, v])
        # # print(i,v)
            
    # print(letters)
    # print(guesses)
    return reveal





check_letter_in_word(the_word)


        

     
       