from random import choice

random_word = ['elephant', 'luxury', 'subway', 'transcript', 'stronghold','jawbreaker', 'whiskey']

alaphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def computer_random_choice(word):
    random_word = choice(word)
    return random_word


def dashes_for_word(word, letter_guess):

    word = [x for x in word]
    #     # print("_")
    # print(letters)
    letters = []

    for i, v in enumerate(word):
        
        dashes = v.replace(v, '__')
        letters.append(dashes)
        # print(i)
        if letter_guess == v:
            letters.insert(i, letter_guess)
            letters.pop()

        # print(i, v)
            

    


    print(letters )
    # print(list(zip(letters,word)))

 


    
        
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
    correct_letters = []
    final_word = []
  
    while lives >= 0 | score <= len(word) + 1:
        dashes_for_word(word, letter_guess=None)
        user_choice = ask_a_letter()
        
        if user_choice in wrong_letters:
            print('already guessed that letter, try another one')
            
        elif user_choice in computer_choice:
                print("Yes")
                letters = dashes_for_word_test2(word, user_choice)
                final_word.append(letters)
                correct_letters.append(user_choice)
                print(score)
                print(final_word)
                score += 1
        elif user_choice not in wrong_letters:
            wrong_letters.append(user_choice)
            print(f'Wrong letter list: {wrong_letters}')
            print(f'Remaining lives is: {lives}')
            lives -= 1

        if lives == 0:
            print(f'Game over! You have {lives} remaining!')
            break

        if score == len(word):
            print(f"You won! Good job you guessed the correct word!")
            break

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
    while word_count < len(word) + 1 and spaces < len(word):
        
        for i, v in enumerate(word):
            dashes = v.replace(v, '__')
            letters.append(dashes)
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

    print(letters )   

    






# the_word = computer_random_choice(random_word)

# dashes_for_word('whiskey', 'h')

# ask_a_letter()

#check_letter_in_word('whiskey')

# word_revealer('whiskey', 'y')



def dashes_for_word_test2(word, letter):
    word = [x for x in word]
    #     # print("_")
    # print(letters)
    letters = []
    word_count = 0 
    spaces = 0
    for i, v in enumerate(word):
        if letter == v:
            letters.append(v)
            
        else:
            dashes = v.replace(v, '__')
            letters.append(dashes)
        print(i,v)
            

    print(letters)
    return letters


#dashes_for_word_test2('whiskey', "h")


check_letter_in_word('whiskey')
        

     
       