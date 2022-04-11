#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string


#DECLARE VARIABLES
#getting alphabet
alphabet = list(string.ascii_lowercase)

#getting vowels
vowels = ['a','e','i','o','u']

#getting consonants from alphabert
consonant = []
for i in alphabet:
    if i not in vowels:
        consonant.append(i)
consonants = consonant
        
#to keep track of round wins      
player_1 = 0
player_2 = 0
player_3 = 0

#1st round banks
bank1 = 0
bank2 = 0
bank3 = 0

#2nd round banks
sum_bank1 = 0
sum_bank2 = 0
sum_bank3 = 0

#create wheel of fortune
wheel = list(range(100,901,50))
wheel_addition = ['BANKRUPT', 'LOSE TURN']
wheel.extend(wheel_addition)
random.shuffle(wheel)
wheel_option = wheel


#create random word
word_list = open(r'words.txt')
random_word = random.choice(word_list.readlines()).lower()
#clean white spaces from random word
word = random_word.strip()


#create display
display = ''
for i in word:
    display+='_'


#function for player 1
def player1_round1(num, num1):
    
    global guess, display, bank1, player_1
    
    #creating variable to spin wheel of fortune
    condition1 = False
    while condition1 is False:
        spin_wheel = input('Please enter "spin" to spin the wheel: ')
        print()
        if not spin_wheel.isalpha():
            print('That was not text input. Please enter "spin" to start')
        elif spin_wheel != 'spin':
            print('You did not enter "spin". Please enter "spin" to start')
        else:
            condition1 = True
    
    #run ans assign wheel result after to variable
    spin_result = random.choice(wheel_option)
    
    #displaying wheel result
    if spin_result == 'BANKRUPT':
        print(f'Wheel landed on {spin_result}')
    elif spin_result == "LOSE TURN":
        print(f'Wheel landed on {spin_result}')
    else:
        print(f'Wheel landed on {spin_result}. To bank this amount, you need to guess the right letter or word')
    
    
    #MAIN CODE TO IDENTIFY WIN OR LOSE IN A SINGLE TURN
    condition2 = False
    condition3 = False
    while condition2 is False:
        if spin_result == 'BANKRUPT': #if bankrupt, player losses bank and turn
            bank1 = 0 
            condition2 = True
        elif spin_result == 'LOSE TURN': #if LOSE TURN, player loses turn
            print('Sorry you lost your turn now')
            condition2 = True
        else:                           #if money, player keps playing
            
            while condition3 is False:
                guess = input('Please enter your guess (letter or word): ')  #player guesses latter or word
                if not guess.isalpha():
                    print('That was not a letter or word. Please try again') #input checl
                elif len(guess) == 1:                                        #if guess is letter
                    if guess in vowels:
                        print('Please guess a consonant, not a vowel')       #avoiding vowel letter guess
                    else:
                        if guess in word:                                    #if letter in word
                            word_index = [index for index, i in enumerate(word) if i == guess]   #getting index of letter in word that matches guess
                            display = ''.join(guess if index in word_index else i for index, i in enumerate(display))   #replacing display index with index of word that matches guess
                            print(f'Target word: {display}') #print display
                            bank1+=spin_result   #adding money to bank
                            if display == word:  #check if display-word is all guessed and matches the target word 
                                player_1+=1  #if ward is fully guessed, player received 1 score
                                print(display)
                                condition3 = True
                                condition2 = True
                            else:             #word is not fully guessed yet
                                condition4 = False
                                while condition4 is False:
                                    vowel_pur = input('Would you like to purchase vowel? Y/N').upper()   #ask if want to purchase vowel
                                    if not vowel_pur.isalpha():
                                        print('That was not a valid input. Please try again') #check input
                                    elif vowel_pur == 'Y':  #yes, wants a vowel
                                        condition5 = False 
                                        while condition5 is False:
                                            if bank1 >= 250:  #check if enough money to purchase vowel
                                                condition6 = False
                                                while condition6 is False:
                                                    vowel_guess = input('Please guess your vowel: ')  #guesses vowel
                                                    if not vowel_guess.isalpha():
                                                        print('That was not a vowel. Plesae guess a vowel') #input check
                                                    elif vowel_guess in consonants:  
                                                        print('That was a consonant. Please guess a vowel')  #avoid consonant guess
                                                    else:
                                                        if vowel_guess in word:            #check if vowel in target word
                                                            word_vowel_index = [index for index, i in enumerate(word) if i == vowel_guess] #getting index of word that matches vowel guess
                                                            display = ''.join(vowel_guess if index in word_vowel_index else i for index, i in enumerate(display))  #replacing display index with index of word that matches vowel guess
                                                            bank1-=250                    #substracting vowel price from player's guess
                                                            print(display)           #printing updated display
                                                            condition7 = False
                                                            while condition7 is False:
                                                                word_guess = input('Do you want to guess the word? Y/N').upper()     #checking if wants to guess the full word
                                                                if not word_guess.isalpha():
                                                                    print('That was not a valid input. Please try again')     #check input
                                                                elif word_guess == 'Y':          #if wants to guess
                                                                    condition8 = False
                                                                    while condition8 is False:
                                                                        word_guess_final = input('Guess your word: ')       #input for word guess
                                                                        if not word_guess_final.isalpha():
                                                                            print('That was not alphabetic word. Please only use alpha charachters')     #input check
                                                                        elif word_guess_final == word:            #if guessed word matches target word, round ends
                                                                            print('Great guess, you won!!!')
                                                                            player_1+=1             #if word guessed corectly, player receives 1 score
                                                                            print(f'The ward you guessed is {word}')
                                                                            condition8 = True
                                                                            condition7 = True
                                                                            condition6 = True
                                                                            condition5 = True
                                                                            condition4 = True
                                                                            condition3 = True
                                                                            condition2 = True
                                                                        else:
                                                                            print("Sorry, that was wrong word. You lose your turn. Now it's next player's turn")   #word didn't match
                                                                            condition8 = True
                                                                            condition7 = True
                                                                            condition6 = True
                                                                            condition5 = True
                                                                            condition4 = True
                                                                            condition3 = True
                                                                            condition2 = True
                                                                elif len(word_guess) > 1:
                                                                    print('That was not a valid answer. Please input Y/N')
                                                                else:
                                                                    print("You used your turn. Now it's next player's turn")   #if doesn't want to guess the word, loses turn
                                                                    condition7 = True
                                                                    condition6 = True
                                                                    condition5 = True
                                                                    condition4 = True
                                                                    condition3 = True
                                                                    condition2 = True
                                                        else:
                                                            print("Sorry, that vowel doesn't exist in target word. You lose your turn. Now it's next player's turn")    #guessed wrong vowel. loses turn
                                                            condition6 = True
                                                            condition5 = True
                                                            condition4 = True
                                                            condition3 = True
                                                            condition2 = True
                                            else:
                                                print(f"Sorry, you need at least 250 in you bank to buy vowel. You have only {bank1} in your bank")    #doesn't have enough money in bank to purchase vowel
                                                condition9 = False
                                                while condition9 is False:
                                                    word_guess = input('Do you want to guess the word? Y/N').upper()    #if not enough money to buy vowel, check if want's to guess the word
                                                    if not word_guess.isalpha():
                                                        print('That was not a valid input. Please try again')  #input check
                                                    elif word_guess == 'Y':    #if wishes to guess the word
                                                        condition10 = False
                                                        while condition10 is False:
                                                            word_guess_final = input('Guess your word: ')   #guessing the word
                                                            if not word_guess_final.isalpha():
                                                                print('That was not alphabetic word. Please only use alpha charachters')     #input check
                                                            elif word_guess_final == word:      #if guee mathces the target word, round ends
                                                                print('Great guess, you won!!!')
                                                                player_1+=1                #player recevies 1 score if guesses the word
                                                                print(f'The ward you guessed is {word}')
                                                                condition10 = True
                                                                condition9 = True
                                                                condition5 = True
                                                                condition4 = True 
                                                                condition3 = True
                                                                condition2 = True
                                                            else:
                                                                print("You used your turn. Now it's next player's turn")     #loses turn, if did not guess corect word
                                                                condition10 = True
                                                                condition9 = True
                                                                condition5 = True
                                                                condition4 = True 
                                                                condition3 = True
                                                                condition2 = True
                                                    else:
                                                        print("You used your turn. Now it's next player's turn")    #doesn't want to guess the word, losses turn
                                                        condition9 = True
                                                        condition5 = True
                                                        condition4 = True
                                                        condition3 = True
                                                        condition2 = True
                                    else:                                    #if doesn't want to purchase vowel
                                        condition9 = False
                                        while condition9 is False:
                                            word_guess = input('Do you want to guess the word? Y/N').upper()     #check if wants to guess the target word
                                            if not word_guess.isalpha():
                                                print('That was not a valid input. Please try again')    #input check
                                            elif word_guess == 'Y':      #yes, wants to guess the word
                                                condition10 = False
                                                while condition10 is False:
                                                    word_guess_final = input('Guess your word: ')    #word guess input
                                                    if not word_guess_final.isalpha():
                                                        print('That was not alphabetic word. Please only use alpha charachters')   #input check
                                                    elif word_guess_final == word:            #if guessed word matches target word, round ends
                                                        print('Great guess, you won!!!')
                                                        player_1+=1       #player receives 1 score ig guesses target word correctly
                                                        print(f'The ward you guessed is {word}')
                                                        condition10 = True
                                                        condition9 = True
                                                        condition8 = True
                                                        condition7 = True
                                                        condition5 = True
                                                        condition4 = True 
                                                        condition3 = True
                                                        condition2 = True
                                                    else:
                                                        print('That was wrong word. You lose your turn now')
                                                        condition10 = True
                                                        condition9 = True
                                                        condition8 = True
                                                        condition7 = True
                                                        condition5 = True
                                                        condition4 = True 
                                                        condition3 = True
                                                        condition2 = True
                                            else:
                                                print("You used your turn. Now it's next player's turn")    #if doesn't want to guess the word, losses turn
                                                condition10 = True
                                                condition9 = True
                                                condition8 = True
                                                condition7 = True
                                                condition5 = True
                                                condition4 = True 
                                                condition3 = True
                                                condition2 = True
                                                
                        else:              #if letter guessed is not in word, loses turn
                            print("Your guess is wrong. Next player get's the turn")
                            condition3 = True
                            condition2 = True
                
                elif len(guess) > 1:     #if guess is a word
                    if guess == word:     #if guess matches target word, round ends
                        bank1+=spin_result
                        player_1+=1         #player receives 1 score
                        print('Phenomenal guess, great job. You won!!!')
                        print(f'The ward you guessed is {word}')
                        condition3 = True
                        condition2 = True
                    else:     #if word guess is wrong, losses turn
                        print('That was wrong guess. You lose your turn')
                        condition3 = True
                        condition2 = True                
                else:   #if guess is empty entry
                    print('That was empty entry. Please try again')
    return bank1, player_1
                    
                    
#function for player 2 
def player2_round1(num, num1):
    
    global guess, display, bank2, player_2
    
    #creating variable to spin wheel of fortune
    condition1 = False
    while condition1 is False:
        spin_wheel = input('Please enter "spin" to spin the wheel: ')
        print()
        if not spin_wheel.isalpha():
            print('That was not text input. Please enter "spin" to start')
        elif spin_wheel != 'spin':
            print('You did not enter "spin". Please enter "spin" to start')
        else:
            condition1 = True
    
    #run ans assign wheel result after to variable
    spin_result = random.choice(wheel_option)
    
    #displaying wheel result
    if spin_result == 'BANKRUPT':
        print(f'Wheel landed on {spin_result}')
    elif spin_result == "LOSE TURN":
        print(f'Wheel landed on {spin_result}')
    else:
        print(f'Wheel landed on {spin_result}. To bank this amount, you need to guess the right letter or word')
    
    
    #MAIN CODE TO IDENTIFY WIN OR LOSE IN A SINGLE TURN
    condition2 = False
    condition3 = False
    while condition2 is False:
        if spin_result == 'BANKRUPT': #if bankrupt, player losses bank and turn
            bank2 = 0 
            condition2 = True
        elif spin_result == 'LOSE TURN': #if LOSE TURN, player loses turn
            print('Sorry you lost your turn now')
            condition2 = True
        else:                           #if money, player keps playing
            
            while condition3 is False:
                guess = input('Please enter your guess (letter or word): ')  #player guesses latter or word
                if not guess.isalpha():
                    print('That was not a letter or word. Please try again') #input checl
                elif len(guess) == 1:                                        #if guess is letter
                    if guess in vowels:
                        print('Please guess a consonant, not a vowel')       #avoiding vowel letter guess
                    else:
                        if guess in word:                                    #if letter in word
                            word_index = [index for index, i in enumerate(word) if i == guess]   #getting index of letter in word that matches guess
                            display = ''.join(guess if index in word_index else i for index, i in enumerate(display))   #replacing display index with index of word that matches guess
                            print(f'Target word: {display}') #print display
                            bank2+=spin_result   #adding money to bank
                            if display == word:  #check if display-word is all guessed and matches the target word 
                                player_2+=1  #if ward is fully guessed, player received 1 score
                                print(display)
                                condition3 = True
                                condition2 = True
                            else:             #word is not fully guessed yet
                                condition4 = False
                                while condition4 is False:
                                    vowel_pur = input('Would you like to purchase vowel? Y/N').upper()   #ask if want to purchase vowel
                                    if not vowel_pur.isalpha():
                                        print('That was not a valid input. Please try again') #check input
                                    elif vowel_pur == 'Y':  #yes, wants a vowel
                                        condition5 = False 
                                        while condition5 is False:
                                            if bank2 >= 250:  #check if enough money to purchase vowel
                                                condition6 = False
                                                while condition6 is False:
                                                    vowel_guess = input('Please guess your vowel: ')  #guesses vowel
                                                    if not vowel_guess.isalpha():
                                                        print('That was not a vowel. Plesae guess a vowel') #input check
                                                    elif vowel_guess in consonants:  
                                                        print('That was a consonant. Please guess a vowel')  #avoid consonant guess
                                                    else:
                                                        if vowel_guess in word:            #check if vowel in target word
                                                            word_vowel_index = [index for index, i in enumerate(word) if i == vowel_guess] #getting index of word that matches vowel guess
                                                            display = ''.join(vowel_guess if index in word_vowel_index else i for index, i in enumerate(display))  #replacing display index with index of word that matches vowel guess
                                                            bank2-=250                    #substracting vowel price from player's guess
                                                            print(display)           #printing updated display
                                                            condition7 = False
                                                            while condition7 is False:
                                                                word_guess = input('Do you want to guess the word? Y/N').upper()     #checking if wants to guess the full word
                                                                if not word_guess.isalpha():
                                                                    print('That was not a valid input. Please try again')     #check input
                                                                elif word_guess == 'Y':          #if wants to guess
                                                                    condition8 = False
                                                                    while condition8 is False:
                                                                        word_guess_final = input('Guess your word: ')       #input for word guess
                                                                        if not word_guess_final.isalpha():
                                                                            print('That was not alphabetic word. Please only use alpha charachters')     #input check
                                                                        elif word_guess_final == word:            #if guessed word matches target word, round ends
                                                                            print('Great guess, you won!!!')
                                                                            player_2+=1             #if word guessed corectly, player receives 1 score
                                                                            print(f'The ward you guessed is {word}')
                                                                            condition8 = True
                                                                            condition7 = True
                                                                            condition6 = True
                                                                            condition5 = True
                                                                            condition4 = True
                                                                            condition3 = True
                                                                            condition2 = True
                                                                        else:
                                                                            print("Sorry, that was wrong word. You lose your turn. Now it's next player's turn")   #word didn't match
                                                                            condition8 = True
                                                                            condition7 = True
                                                                            condition6 = True
                                                                            condition5 = True
                                                                            condition4 = True
                                                                            condition3 = True
                                                                            condition2 = True
                                                                elif len(word_guess) > 1:
                                                                    print('That was not a valid answer. Please input Y/N')
                                                                else:
                                                                    print("You used your turn. Now it's next player's turn")   #if doesn't want to guess the word, loses turn
                                                                    condition7 = True
                                                                    condition6 = True
                                                                    condition5 = True
                                                                    condition4 = True
                                                                    condition3 = True
                                                                    condition2 = True
                                                        else:
                                                            print("Sorry, that vowel doesn't exist in target word. You lose your turn. Now it's next player's turn")    #guessed wrong vowel. loses turn
                                                            condition6 = True
                                                            condition5 = True
                                                            condition4 = True
                                                            condition3 = True
                                                            condition2 = True
                                            else:
                                                print(f"Sorry, you need at least 250 in you bank to buy vowel. You have only {bank2} in your bank")    #doesn't have enough money in bank to purchase vowel
                                                condition9 = False
                                                while condition9 is False:
                                                    word_guess = input('Do you want to guess the word? Y/N').upper()    #if not enough money to buy vowel, check if want's to guess the word
                                                    if not word_guess.isalpha():
                                                        print('That was not a valid input. Please try again')  #input check
                                                    elif word_guess == 'Y':    #if wishes to guess the word
                                                        condition10 = False
                                                        while condition10 is False:
                                                            word_guess_final = input('Guess your word: ')   #guessing the word
                                                            if not word_guess_final.isalpha():
                                                                print('That was not alphabetic word. Please only use alpha charachters')     #input check
                                                            elif word_guess_final == word:      #if guee mathces the target word, round ends
                                                                print('Great guess, you won!!!')
                                                                player_2+=1                #player recevies 1 score if guesses the word
                                                                print(f'The ward you guessed is {word}')
                                                                condition10 = True
                                                                condition9 = True
                                                                condition5 = True
                                                                condition4 = True 
                                                                condition3 = True
                                                                condition2 = True
                                                            else:
                                                                print("You used your turn. Now it's next player's turn")     #loses turn, if did not guess corect word
                                                                condition10 = True
                                                                condition9 = True
                                                                condition5 = True
                                                                condition4 = True 
                                                                condition3 = True
                                                                condition2 = True
                                                    else:
                                                        print("You used your turn. Now it's next player's turn")    #doesn't want to guess the word, losses turn
                                                        condition9 = True
                                                        condition5 = True
                                                        condition4 = True
                                                        condition3 = True
                                                        condition2 = True
                                    else:                                    #if doesn't want to purchase vowel
                                        condition9 = False
                                        while condition9 is False:
                                            word_guess = input('Do you want to guess the word? Y/N').upper()     #check if wants to guess the target word
                                            if not word_guess.isalpha():
                                                print('That was not a valid input. Please try again')    #input check
                                            elif word_guess == 'Y':      #yes, wants to guess the word
                                                condition10 = False
                                                while condition10 is False:
                                                    word_guess_final = input('Guess your word: ')    #word guess input
                                                    if not word_guess_final.isalpha():
                                                        print('That was not alphabetic word. Please only use alpha charachters')   #input check
                                                    elif word_guess_final == word:            #if guessed word matches target word, round ends
                                                        print('Great guess, you won!!!')
                                                        player_2+=1       #player receives 1 score ig guesses target word correctly
                                                        print(f'The ward you guessed is {word}')
                                                        condition10 = True
                                                        condition9 = True
                                                        condition8 = True
                                                        condition7 = True
                                                        condition5 = True
                                                        condition4 = True 
                                                        condition3 = True
                                                        condition2 = True
                                                    else:
                                                        print('That was wrong word. You lose your turn now')
                                                        condition10 = True
                                                        condition9 = True
                                                        condition8 = True
                                                        condition7 = True
                                                        condition5 = True
                                                        condition4 = True 
                                                        condition3 = True
                                                        condition2 = True
                                            else:
                                                print("You used your turn. Now it's next player's turn")    #if doesn't want to guess the word, losses turn
                                                condition10 = True
                                                condition9 = True
                                                condition8 = True
                                                condition7 = True
                                                condition5 = True
                                                condition4 = True 
                                                condition3 = True
                                                condition2 = True
                                                
                        else:              #if letter guessed is not in word, loses turn
                            print("Your guess is wrong. Next player get's the turn")
                            condition3 = True
                            condition2 = True
                
                elif len(guess) > 1:     #if guess is a word
                    if guess == word:     #if guess matches target word, round ends
                        bank2+=spin_result
                        player_2+=1         #player receives 1 score
                        print('Phenomenal guess, great job. You won!!!')
                        print(f'The ward you guessed is {word}')
                        condition3 = True
                        condition2 = True
                    else:     #if word guess is wrong, losses turn
                        print('That was wrong guess. You lose your turn')
                        condition3 = True
                        condition2 = True                
                else:   #if guess is empty entry
                    print('That was empty entry. Please try again')
    return bank2, player_2
                    
                    
#create function to identify round winner. Game starts when player spins the wheel. 
def player3_round1(num, num1):
    
    global guess, display, bank3, player_3
    
    #creating variable to spin wheel of fortune
    condition1 = False
    while condition1 is False:
        spin_wheel = input('Please enter "spin" to spin the wheel: ')
        print()
        if not spin_wheel.isalpha():
            print('That was not text input. Please enter "spin" to start')
        elif spin_wheel != 'spin':
            print('You did not enter "spin". Please enter "spin" to start')
        else:
            condition1 = True
    
    #run ans assign wheel result after to variable
    spin_result = random.choice(wheel_option)
    
    #displaying wheel result
    if spin_result == 'BANKRUPT':
        print(f'Wheel landed on {spin_result}')
    elif spin_result == "LOSE TURN":
        print(f'Wheel landed on {spin_result}')
    else:
        print(f'Wheel landed on {spin_result}. To bank this amount, you need to guess the right letter or word')
    
    
    #MAIN CODE TO IDENTIFY WIN OR LOSE IN A SINGLE TURN
    condition2 = False
    condition3 = False
    while condition2 is False:
        if spin_result == 'BANKRUPT': #if bankrupt, player losses bank and turn
            bank3 = 0 
            condition2 = True
        elif spin_result == 'LOSE TURN': #if LOSE TURN, player loses turn
            print('Sorry you lost your turn now')
            condition2 = True
        else:                           #if money, player keps playing
            
            while condition3 is False:
                guess = input('Please enter your guess (letter or word): ')  #player guesses latter or word
                if not guess.isalpha():
                    print('That was not a letter or word. Please try again') #input checl
                elif len(guess) == 1:                                        #if guess is letter
                    if guess in vowels:
                        print('Please guess a consonant, not a vowel')       #avoiding vowel letter guess
                    else:
                        if guess in word:                                    #if letter in word
                            word_index = [index for index, i in enumerate(word) if i == guess]   #getting index of letter in word that matches guess
                            display = ''.join(guess if index in word_index else i for index, i in enumerate(display))   #replacing display index with index of word that matches guess
                            print(f'Target word: {display}') #print display
                            bank3+=spin_result   #adding money to bank
                            if display == word:  #check if display-word is all guessed and matches the target word 
                                player_3+=1  #if ward is fully guessed, player received 1 score
                                print(display)
                                condition3 = True
                                condition2 = True
                            else:             #word is not fully guessed yet
                                condition4 = False
                                while condition4 is False:
                                    vowel_pur = input('Would you like to purchase vowel? Y/N').upper()   #ask if want to purchase vowel
                                    if not vowel_pur.isalpha():
                                        print('That was not a valid input. Please try again') #check input
                                    elif vowel_pur == 'Y':  #yes, wants a vowel
                                        condition5 = False 
                                        while condition5 is False:
                                            if bank3 >= 250:  #check if enough money to purchase vowel
                                                condition6 = False
                                                while condition6 is False:
                                                    vowel_guess = input('Please guess your vowel: ')  #guesses vowel
                                                    if not vowel_guess.isalpha():
                                                        print('That was not a vowel. Plesae guess a vowel') #input check
                                                    elif vowel_guess in consonants:  
                                                        print('That was a consonant. Please guess a vowel')  #avoid consonant guess
                                                    else:
                                                        if vowel_guess in word:            #check if vowel in target word
                                                            word_vowel_index = [index for index, i in enumerate(word) if i == vowel_guess] #getting index of word that matches vowel guess
                                                            display = ''.join(vowel_guess if index in word_vowel_index else i for index, i in enumerate(display))  #replacing display index with index of word that matches vowel guess
                                                            bank3-=250                    #substracting vowel price from player's guess
                                                            print(display)           #printing updated display
                                                            condition7 = False
                                                            while condition7 is False:
                                                                word_guess = input('Do you want to guess the word? Y/N').upper()     #checking if wants to guess the full word
                                                                if not word_guess.isalpha():
                                                                    print('That was not a valid input. Please try again')     #check input
                                                                elif word_guess == 'Y':          #if wants to guess
                                                                    condition8 = False
                                                                    while condition8 is False:
                                                                        word_guess_final = input('Guess your word: ')       #input for word guess
                                                                        if not word_guess_final.isalpha():
                                                                            print('That was not alphabetic word. Please only use alpha charachters')     #input check
                                                                        elif word_guess_final == word:            #if guessed word matches target word, round ends
                                                                            print('Great guess, you won!!!')
                                                                            player_3+=1             #if word guessed corectly, player receives 1 score
                                                                            print(f'The ward you guessed is {word}')
                                                                            condition8 = True
                                                                            condition7 = True
                                                                            condition6 = True
                                                                            condition5 = True
                                                                            condition4 = True
                                                                            condition3 = True
                                                                            condition2 = True
                                                                        else:
                                                                            print("Sorry, that was wrong word. You lose your turn. Now it's next player's turn")   #word didn't match
                                                                            condition8 = True
                                                                            condition7 = True
                                                                            condition6 = True
                                                                            condition5 = True
                                                                            condition4 = True
                                                                            condition3 = True
                                                                            condition2 = True
                                                                elif len(word_guess) > 1:
                                                                    print('That was not a valid answer. Please input Y/N')
                                                                else:
                                                                    print("You used your turn. Now it's next player's turn")   #if doesn't want to guess the word, loses turn
                                                                    condition7 = True
                                                                    condition6 = True
                                                                    condition5 = True
                                                                    condition4 = True
                                                                    condition3 = True
                                                                    condition2 = True
                                                        else:
                                                            print("Sorry, that vowel doesn't exist in target word. You lose your turn. Now it's next player's turn")    #guessed wrong vowel. loses turn
                                                            condition6 = True
                                                            condition5 = True
                                                            condition4 = True
                                                            condition3 = True
                                                            condition2 = True
                                            else:
                                                print(f"Sorry, you need at least 250 in you bank to buy vowel. You have only {bank3} in your bank")    #doesn't have enough money in bank to purchase vowel
                                                condition9 = False
                                                while condition9 is False:
                                                    word_guess = input('Do you want to guess the word? Y/N').upper()    #if not enough money to buy vowel, check if want's to guess the word
                                                    if not word_guess.isalpha():
                                                        print('That was not a valid input. Please try again')  #input check
                                                    elif word_guess == 'Y':    #if wishes to guess the word
                                                        condition10 = False
                                                        while condition10 is False:
                                                            word_guess_final = input('Guess your word: ')   #guessing the word
                                                            if not word_guess_final.isalpha():
                                                                print('That was not alphabetic word. Please only use alpha charachters')     #input check
                                                            elif word_guess_final == word:      #if guee mathces the target word, round ends
                                                                print('Great guess, you won!!!')
                                                                player_3+=1                #player recevies 1 score if guesses the word
                                                                print(f'The ward you guessed is {word}')
                                                                condition10 = True
                                                                condition9 = True
                                                                condition5 = True
                                                                condition4 = True 
                                                                condition3 = True
                                                                condition2 = True
                                                            else:
                                                                print("You used your turn. Now it's next player's turn")     #loses turn, if did not guess corect word
                                                                condition10 = True
                                                                condition9 = True
                                                                condition5 = True
                                                                condition4 = True 
                                                                condition3 = True
                                                                condition2 = True
                                                    else:
                                                        print("You used your turn. Now it's next player's turn")    #doesn't want to guess the word, losses turn
                                                        condition9 = True
                                                        condition5 = True
                                                        condition4 = True
                                                        condition3 = True
                                                        condition2 = True
                                    else:                                    #if doesn't want to purchase vowel
                                        condition9 = False
                                        while condition9 is False:
                                            word_guess = input('Do you want to guess the word? Y/N').upper()     #check if wants to guess the target word
                                            if not word_guess.isalpha():
                                                print('That was not a valid input. Please try again')    #input check
                                            elif word_guess == 'Y':      #yes, wants to guess the word
                                                condition10 = False
                                                while condition10 is False:
                                                    word_guess_final = input('Guess your word: ')    #word guess input
                                                    if not word_guess_final.isalpha():
                                                        print('That was not alphabetic word. Please only use alpha charachters')   #input check
                                                    elif word_guess_final == word:            #if guessed word matches target word, round ends
                                                        print('Great guess, you won!!!')
                                                        player_3+=1       #player receives 1 score ig guesses target word correctly
                                                        print(f'The ward you guessed is {word}')
                                                        condition10 = True
                                                        condition9 = True
                                                        condition8 = True
                                                        condition7 = True
                                                        condition5 = True
                                                        condition4 = True 
                                                        condition3 = True
                                                        condition2 = True
                                                    else:
                                                        print('That was wrong word. You lose your turn now')
                                                        condition10 = True
                                                        condition9 = True
                                                        condition8 = True
                                                        condition7 = True
                                                        condition5 = True
                                                        condition4 = True 
                                                        condition3 = True
                                                        condition2 = True
                                            else:
                                                print("You used your turn. Now it's next player's turn")    #if doesn't want to guess the word, losses turn
                                                condition10 = True
                                                condition9 = True
                                                condition8 = True
                                                condition7 = True
                                                condition5 = True
                                                condition4 = True 
                                                condition3 = True
                                                condition2 = True
                                                
                        else:              #if letter guessed is not in word, loses turn
                            print("Your guess is wrong. Next player get's the turn")
                            condition3 = True
                            condition2 = True
                
                elif len(guess) > 1:     #if guess is a word
                    if guess == word:     #if guess matches target word, round ends
                        bank3+=spin_result
                        player_3+=1         #player receives 1 score
                        print('Phenomenal guess, great job. You won!!!')
                        print(f'The ward you guessed is {word}')
                        condition3 = True
                        condition2 = True
                    else:     #if word guess is wrong, losses turn
                        print('That was wrong guess. You lose your turn')
                        condition3 = True
                        condition2 = True                
                else:   #if guess is empty entry
                    print('That was empty entry. Please try again')
    return bank3, player_3
                    
                    
#function for player 1
def player1_round2(num, num1):
    
    global guess, display, sum_bank1, player_1
    
    #creating variable to spin wheel of fortune
    condition1 = False
    while condition1 is False:
        spin_wheel = input('Please enter "spin" to spin the wheel: ')
        print()
        if not spin_wheel.isalpha():
            print('That was not text input. Please enter "spin" to start')
        elif spin_wheel != 'spin':
            print('You did not enter "spin". Please enter "spin" to start')
        else:
            condition1 = True
    
    #run ans assign wheel result after to variable
    spin_result = random.choice(wheel_option)
    
    #displaying wheel result
    if spin_result == 'BANKRUPT':
        print(f'Wheel landed on {spin_result}')
    elif spin_result == "LOSE TURN":
        print(f'Wheel landed on {spin_result}')
    else:
        print(f'Wheel landed on {spin_result}. To bank this amount, you need to guess the right letter or word')
    
    
    #MAIN CODE TO IDENTIFY WIN OR LOSE IN A SINGLE TURN
    condition2 = False
    condition3 = False
    while condition2 is False:
        if spin_result == 'BANKRUPT': #if bankrupt, player losses bank and turn
            sum_bank1 = 0 
            condition2 = True
        elif spin_result == 'LOSE TURN': #if LOSE TURN, player loses turn
            print('Sorry you lost your turn now')
            condition2 = True
        else:                           #if money, player keps playing
            
            while condition3 is False:
                guess = input('Please enter your guess (letter or word): ')  #player guesses latter or word
                if not guess.isalpha():
                    print('That was not a letter or word. Please try again') #input checl
                elif len(guess) == 1:                                        #if guess is letter
                    if guess in vowels:
                        print('Please guess a consonant, not a vowel')       #avoiding vowel letter guess
                    else:
                        if guess in word:                                    #if letter in word
                            word_index = [index for index, i in enumerate(word) if i == guess]   #getting index of letter in word that matches guess
                            display = ''.join(guess if index in word_index else i for index, i in enumerate(display))   #replacing display index with index of word that matches guess
                            print(f'Target word: {display}') #print display
                            sum_bank1+=spin_result   #adding money to bank
                            if display == word:  #check if display-word is all guessed and matches the target word 
                                player_1+=1  #if ward is fully guessed, player received 1 score
                                print(display)
                                condition3 = True
                                condition2 = True
                            else:             #word is not fully guessed yet
                                condition4 = False
                                while condition4 is False:
                                    vowel_pur = input('Would you like to purchase vowel? Y/N').upper()   #ask if want to purchase vowel
                                    if not vowel_pur.isalpha():
                                        print('That was not a valid input. Please try again') #check input
                                    elif vowel_pur == 'Y':  #yes, wants a vowel
                                        condition5 = False 
                                        while condition5 is False:
                                            if sum_bank1 >= 250:  #check if enough money to purchase vowel
                                                condition6 = False
                                                while condition6 is False:
                                                    vowel_guess = input('Please guess your vowel: ')  #guesses vowel
                                                    if not vowel_guess.isalpha():
                                                        print('That was not a vowel. Plesae guess a vowel') #input check
                                                    elif vowel_guess in consonants:  
                                                        print('That was a consonant. Please guess a vowel')  #avoid consonant guess
                                                    else:
                                                        if vowel_guess in word:            #check if vowel in target word
                                                            word_vowel_index = [index for index, i in enumerate(word) if i == vowel_guess] #getting index of word that matches vowel guess
                                                            display = ''.join(vowel_guess if index in word_vowel_index else i for index, i in enumerate(display))  #replacing display index with index of word that matches vowel guess
                                                            sum_bank1-=250                    #substracting vowel price from player's guess
                                                            print(display)           #printing updated display
                                                            condition7 = False
                                                            while condition7 is False:
                                                                word_guess = input('Do you want to guess the word? Y/N').upper()     #checking if wants to guess the full word
                                                                if not word_guess.isalpha():
                                                                    print('That was not a valid input. Please try again')     #check input
                                                                elif word_guess == 'Y':          #if wants to guess
                                                                    condition8 = False
                                                                    while condition8 is False:
                                                                        word_guess_final = input('Guess your word: ')       #input for word guess
                                                                        if not word_guess_final.isalpha():
                                                                            print('That was not alphabetic word. Please only use alpha charachters')     #input check
                                                                        elif word_guess_final == word:            #if guessed word matches target word, round ends
                                                                            print('Great guess, you won!!!')
                                                                            player_1+=1             #if word guessed corectly, player receives 1 score
                                                                            print(f'The ward you guessed is {word}')
                                                                            condition8 = True
                                                                            condition7 = True
                                                                            condition6 = True
                                                                            condition5 = True
                                                                            condition4 = True
                                                                            condition3 = True
                                                                            condition2 = True
                                                                        else:
                                                                            print("Sorry, that was wrong word. You lose your turn. Now it's next player's turn")   #word didn't match
                                                                            condition8 = True
                                                                            condition7 = True
                                                                            condition6 = True
                                                                            condition5 = True
                                                                            condition4 = True
                                                                            condition3 = True
                                                                            condition2 = True
                                                                elif len(word_guess) > 1:
                                                                    print('That was not a valid answer. Please input Y/N')
                                                                else:
                                                                    print("You used your turn. Now it's next player's turn")   #if doesn't want to guess the word, loses turn
                                                                    condition7 = True
                                                                    condition6 = True
                                                                    condition5 = True
                                                                    condition4 = True
                                                                    condition3 = True
                                                                    condition2 = True
                                                        else:
                                                            print("Sorry, that vowel doesn't exist in target word. You lose your turn. Now it's next player's turn")    #guessed wrong vowel. loses turn
                                                            condition6 = True
                                                            condition5 = True
                                                            condition4 = True
                                                            condition3 = True
                                                            condition2 = True
                                            else:
                                                print(f"Sorry, you need at least 250 in you bank to buy vowel. You have only {sum_bank1} in your bank")    #doesn't have enough money in bank to purchase vowel
                                                condition9 = False
                                                while condition9 is False:
                                                    word_guess = input('Do you want to guess the word? Y/N').upper()    #if not enough money to buy vowel, check if want's to guess the word
                                                    if not word_guess.isalpha():
                                                        print('That was not a valid input. Please try again')  #input check
                                                    elif word_guess == 'Y':    #if wishes to guess the word
                                                        condition10 = False
                                                        while condition10 is False:
                                                            word_guess_final = input('Guess your word: ')   #guessing the word
                                                            if not word_guess_final.isalpha():
                                                                print('That was not alphabetic word. Please only use alpha charachters')     #input check
                                                            elif word_guess_final == word:      #if guee mathces the target word, round ends
                                                                print('Great guess, you won!!!')
                                                                player_1+=1                #player recevies 1 score if guesses the word
                                                                print(f'The ward you guessed is {word}')
                                                                condition10 = True
                                                                condition9 = True
                                                                condition5 = True
                                                                condition4 = True 
                                                                condition3 = True
                                                                condition2 = True
                                                            else:
                                                                print("You used your turn. Now it's next player's turn")     #loses turn, if did not guess corect word
                                                                condition10 = True
                                                                condition9 = True
                                                                condition5 = True
                                                                condition4 = True 
                                                                condition3 = True
                                                                condition2 = True
                                                    else:
                                                        print("You used your turn. Now it's next player's turn")    #doesn't want to guess the word, losses turn
                                                        condition9 = True
                                                        condition5 = True
                                                        condition4 = True
                                                        condition3 = True
                                                        condition2 = True
                                    else:                                    #if doesn't want to purchase vowel
                                        condition9 = False
                                        while condition9 is False:
                                            word_guess = input('Do you want to guess the word? Y/N').upper()     #check if wants to guess the target word
                                            if not word_guess.isalpha():
                                                print('That was not a valid input. Please try again')    #input check
                                            elif word_guess == 'Y':      #yes, wants to guess the word
                                                condition10 = False
                                                while condition10 is False:
                                                    word_guess_final = input('Guess your word: ')    #word guess input
                                                    if not word_guess_final.isalpha():
                                                        print('That was not alphabetic word. Please only use alpha charachters')   #input check
                                                    elif word_guess_final == word:            #if guessed word matches target word, round ends
                                                        print('Great guess, you won!!!')
                                                        player_1+=1       #player receives 1 score ig guesses target word correctly
                                                        print(f'The ward you guessed is {word}')
                                                        condition10 = True
                                                        condition9 = True
                                                        condition8 = True
                                                        condition7 = True
                                                        condition5 = True
                                                        condition4 = True 
                                                        condition3 = True
                                                        condition2 = True
                                                    else:
                                                        print('That was wrong word. You lose your turn now')
                                                        condition10 = True
                                                        condition9 = True
                                                        condition8 = True
                                                        condition7 = True
                                                        condition5 = True
                                                        condition4 = True 
                                                        condition3 = True
                                                        condition2 = True
                                            else:
                                                print("You used your turn. Now it's next player's turn")    #if doesn't want to guess the word, losses turn
                                                condition10 = True
                                                condition9 = True
                                                condition8 = True
                                                condition7 = True
                                                condition5 = True
                                                condition4 = True 
                                                condition3 = True
                                                condition2 = True
                                                
                        else:              #if letter guessed is not in word, loses turn
                            print("Your guess is wrong. Next player get's the turn")
                            condition3 = True
                            condition2 = True
                
                elif len(guess) > 1:     #if guess is a word
                    if guess == word:     #if guess matches target word, round ends
                        sum_bank1+=spin_result
                        player_1+=1         #player receives 1 score
                        print('Phenomenal guess, great job. You won!!!')
                        print(f'The ward you guessed is {word}')
                        condition3 = True
                        condition2 = True
                    else:     #if word guess is wrong, losses turn
                        print('That was wrong guess. You lose your turn')
                        condition3 = True
                        condition2 = True                
                else:   #if guess is empty entry
                    print('That was empty entry. Please try again')
    return sum_bank1, player_1
                    
                    
#function for player 1
def player2_round2(num, num1):
    
    global guess, display, sum_bank2, player_2
    
    #creating variable to spin wheel of fortune
    condition1 = False
    while condition1 is False:
        spin_wheel = input('Please enter "spin" to spin the wheel: ')
        print()
        if not spin_wheel.isalpha():
            print('That was not text input. Please enter "spin" to start')
        elif spin_wheel != 'spin':
            print('You did not enter "spin". Please enter "spin" to start')
        else:
            condition1 = True
    
    #run ans assign wheel result after to variable
    spin_result = random.choice(wheel_option)
    
    #displaying wheel result
    if spin_result == 'BANKRUPT':
        print(f'Wheel landed on {spin_result}')
    elif spin_result == "LOSE TURN":
        print(f'Wheel landed on {spin_result}')
    else:
        print(f'Wheel landed on {spin_result}. To bank this amount, you need to guess the right letter or word')
    
    
    #MAIN CODE TO IDENTIFY WIN OR LOSE IN A SINGLE TURN
    condition2 = False
    condition3 = False
    while condition2 is False:
        if spin_result == 'BANKRUPT': #if bankrupt, player losses bank and turn
            sum_bank2 = 0 
            condition2 = True
        elif spin_result == 'LOSE TURN': #if LOSE TURN, player loses turn
            print('Sorry you lost your turn now')
            condition2 = True
        else:                           #if money, player keps playing
            
            while condition3 is False:
                guess = input('Please enter your guess (letter or word): ')  #player guesses latter or word
                if not guess.isalpha():
                    print('That was not a letter or word. Please try again') #input checl
                elif len(guess) == 1:                                        #if guess is letter
                    if guess in vowels:
                        print('Please guess a consonant, not a vowel')       #avoiding vowel letter guess
                    else:
                        if guess in word:                                    #if letter in word
                            word_index = [index for index, i in enumerate(word) if i == guess]   #getting index of letter in word that matches guess
                            display = ''.join(guess if index in word_index else i for index, i in enumerate(display))   #replacing display index with index of word that matches guess
                            print(f'Target word: {display}') #print display
                            sum_bank2+=spin_result   #adding money to bank
                            if display == word:  #check if display-word is all guessed and matches the target word 
                                player_2+=1  #if ward is fully guessed, player received 1 score
                                print(display)
                                condition3 = True
                                condition2 = True
                            else:             #word is not fully guessed yet
                                condition4 = False
                                while condition4 is False:
                                    vowel_pur = input('Would you like to purchase vowel? Y/N').upper()   #ask if want to purchase vowel
                                    if not vowel_pur.isalpha():
                                        print('That was not a valid input. Please try again') #check input
                                    elif vowel_pur == 'Y':  #yes, wants a vowel
                                        condition5 = False 
                                        while condition5 is False:
                                            if sum_bank2 >= 250:  #check if enough money to purchase vowel
                                                condition6 = False
                                                while condition6 is False:
                                                    vowel_guess = input('Please guess your vowel: ')  #guesses vowel
                                                    if not vowel_guess.isalpha():
                                                        print('That was not a vowel. Plesae guess a vowel') #input check
                                                    elif vowel_guess in consonants:  
                                                        print('That was a consonant. Please guess a vowel')  #avoid consonant guess
                                                    else:
                                                        if vowel_guess in word:            #check if vowel in target word
                                                            word_vowel_index = [index for index, i in enumerate(word) if i == vowel_guess] #getting index of word that matches vowel guess
                                                            display = ''.join(vowel_guess if index in word_vowel_index else i for index, i in enumerate(display))  #replacing display index with index of word that matches vowel guess
                                                            sum_bank2-=250                    #substracting vowel price from player's guess
                                                            print(display)           #printing updated display
                                                            condition7 = False
                                                            while condition7 is False:
                                                                word_guess = input('Do you want to guess the word? Y/N').upper()     #checking if wants to guess the full word
                                                                if not word_guess.isalpha():
                                                                    print('That was not a valid input. Please try again')     #check input
                                                                elif word_guess == 'Y':          #if wants to guess
                                                                    condition8 = False
                                                                    while condition8 is False:
                                                                        word_guess_final = input('Guess your word: ')       #input for word guess
                                                                        if not word_guess_final.isalpha():
                                                                            print('That was not alphabetic word. Please only use alpha charachters')     #input check
                                                                        elif word_guess_final == word:            #if guessed word matches target word, round ends
                                                                            print('Great guess, you won!!!')
                                                                            player_2+=1             #if word guessed corectly, player receives 1 score
                                                                            print(f'The ward you guessed is {word}')
                                                                            condition8 = True
                                                                            condition7 = True
                                                                            condition6 = True
                                                                            condition5 = True
                                                                            condition4 = True
                                                                            condition3 = True
                                                                            condition2 = True
                                                                        else:
                                                                            print("Sorry, that was wrong word. You lose your turn. Now it's next player's turn")   #word didn't match
                                                                            condition8 = True
                                                                            condition7 = True
                                                                            condition6 = True
                                                                            condition5 = True
                                                                            condition4 = True
                                                                            condition3 = True
                                                                            condition2 = True
                                                                elif len(word_guess) > 1:
                                                                    print('That was not a valid answer. Please input Y/N')
                                                                else:
                                                                    print("You used your turn. Now it's next player's turn")   #if doesn't want to guess the word, loses turn
                                                                    condition7 = True
                                                                    condition6 = True
                                                                    condition5 = True
                                                                    condition4 = True
                                                                    condition3 = True
                                                                    condition2 = True
                                                        else:
                                                            print("Sorry, that vowel doesn't exist in target word. You lose your turn. Now it's next player's turn")    #guessed wrong vowel. loses turn
                                                            condition6 = True
                                                            condition5 = True
                                                            condition4 = True
                                                            condition3 = True
                                                            condition2 = True
                                            else:
                                                print(f"Sorry, you need at least 250 in you bank to buy vowel. You have only {sum_bank2} in your bank")    #doesn't have enough money in bank to purchase vowel
                                                condition9 = False
                                                while condition9 is False:
                                                    word_guess = input('Do you want to guess the word? Y/N').upper()    #if not enough money to buy vowel, check if want's to guess the word
                                                    if not word_guess.isalpha():
                                                        print('That was not a valid input. Please try again')  #input check
                                                    elif word_guess == 'Y':    #if wishes to guess the word
                                                        condition10 = False
                                                        while condition10 is False:
                                                            word_guess_final = input('Guess your word: ')   #guessing the word
                                                            if not word_guess_final.isalpha():
                                                                print('That was not alphabetic word. Please only use alpha charachters')     #input check
                                                            elif word_guess_final == word:      #if guee mathces the target word, round ends
                                                                print('Great guess, you won!!!')
                                                                player_2+=1                #player recevies 1 score if guesses the word
                                                                print(f'The ward you guessed is {word}')
                                                                condition10 = True
                                                                condition9 = True
                                                                condition5 = True
                                                                condition4 = True 
                                                                condition3 = True
                                                                condition2 = True
                                                            else:
                                                                print("You used your turn. Now it's next player's turn")     #loses turn, if did not guess corect word
                                                                condition10 = True
                                                                condition9 = True
                                                                condition5 = True
                                                                condition4 = True 
                                                                condition3 = True
                                                                condition2 = True
                                                    else:
                                                        print("You used your turn. Now it's next player's turn")    #doesn't want to guess the word, losses turn
                                                        condition9 = True
                                                        condition5 = True
                                                        condition4 = True
                                                        condition3 = True
                                                        condition2 = True
                                    else:                                    #if doesn't want to purchase vowel
                                        condition9 = False
                                        while condition9 is False:
                                            word_guess = input('Do you want to guess the word? Y/N').upper()     #check if wants to guess the target word
                                            if not word_guess.isalpha():
                                                print('That was not a valid input. Please try again')    #input check
                                            elif word_guess == 'Y':      #yes, wants to guess the word
                                                condition10 = False
                                                while condition10 is False:
                                                    word_guess_final = input('Guess your word: ')    #word guess input
                                                    if not word_guess_final.isalpha():
                                                        print('That was not alphabetic word. Please only use alpha charachters')   #input check
                                                    elif word_guess_final == word:            #if guessed word matches target word, round ends
                                                        print('Great guess, you won!!!')
                                                        player_2+=1       #player receives 1 score if guesses target word correctly
                                                        print(f'The ward you guessed is {word}')
                                                        condition10 = True
                                                        condition9 = True
                                                        condition8 = True
                                                        condition7 = True
                                                        condition5 = True
                                                        condition4 = True 
                                                        condition3 = True
                                                        condition2 = True
                                                    else:
                                                        print('That was wrong word. You lose your turn now')
                                                        condition10 = True
                                                        condition9 = True
                                                        condition8 = True
                                                        condition7 = True
                                                        condition5 = True
                                                        condition4 = True 
                                                        condition3 = True
                                                        condition2 = True
                                            else:
                                                print("You used your turn. Now it's next player's turn")    #if doesn't want to guess the word, losses turn
                                                condition10 = True
                                                condition9 = True
                                                condition8 = True
                                                condition7 = True
                                                condition5 = True
                                                condition4 = True 
                                                condition3 = True
                                                condition2 = True
                                                
                        else:              #if letter guessed is not in word, loses turn
                            print("Your guess is wrong. Next player get's the turn")
                            condition3 = True
                            condition2 = True
                
                elif len(guess) > 1:     #if guess is a word
                    if guess == word:     #if guess matches target word, round ends
                        sum_bank2+=spin_result
                        player_2+=1         #player receives 1 score
                        print('Phenomenal guess, great job. You won!!!')
                        print(f'The ward you guessed is {word}')
                        condition3 = True
                        condition2 = True
                    else:     #if word guess is wrong, losses turn
                        print('That was wrong guess. You lose your turn')
                        condition3 = True
                        condition2 = True                
                else:   #if guess is empty entry
                    print('That was empty entry. Please try again')
    return sum_bank2, player_2
                          
                          
#function for player 1
def player3_round2(num, num1):
    
    global guess, display, sum_bank3, player_3
    
    #creating variable to spin wheel of fortune
    condition1 = False
    while condition1 is False:
        spin_wheel = input('Please enter "spin" to spin the wheel: ')
        print()
        if not spin_wheel.isalpha():
            print('That was not text input. Please enter "spin" to start')
        elif spin_wheel != 'spin':
            print('You did not enter "spin". Please enter "spin" to start')
        else:
            condition1 = True
    
    #run ans assign wheel result after to variable
    spin_result = random.choice(wheel_option)
    
    #displaying wheel result
    if spin_result == 'BANKRUPT':
        print(f'Wheel landed on {spin_result}')
    elif spin_result == "LOSE TURN":
        print(f'Wheel landed on {spin_result}')
    else:
        print(f'Wheel landed on {spin_result}. To bank this amount, you need to guess the right letter or word')
    
    
    #MAIN CODE TO IDENTIFY WIN OR LOSE IN A SINGLE TURN
    condition2 = False
    condition3 = False
    while condition2 is False:
        if spin_result == 'BANKRUPT': #if bankrupt, player losses bank and turn
            sum_bank3 = 0 
            condition2 = True
        elif spin_result == 'LOSE TURN': #if LOSE TURN, player loses turn
            print('Sorry you lost your turn now')
            condition2 = True
        else:                           #if money, player keps playing
            
            while condition3 is False:
                guess = input('Please enter your guess (letter or word): ')  #player guesses latter or word
                if not guess.isalpha():
                    print('That was not a letter or word. Please try again') #input checl
                elif len(guess) == 1:                                        #if guess is letter
                    if guess in vowels:
                        print('Please guess a consonant, not a vowel')       #avoiding vowel letter guess
                    else:
                        if guess in word:                                    #if letter in word
                            word_index = [index for index, i in enumerate(word) if i == guess]   #getting index of letter in word that matches guess
                            display = ''.join(guess if index in word_index else i for index, i in enumerate(display))   #replacing display index with index of word that matches guess
                            print(f'Target word: {display}') #print display
                            sum_bank3+=spin_result   #adding money to bank
                            if display == word:  #check if display-word is all guessed and matches the target word 
                                player_3+=1  #if ward is fully guessed, player received 1 score
                                print(display)
                                condition3 = True
                                condition2 = True
                            else:             #word is not fully guessed yet
                                condition4 = False
                                while condition4 is False:
                                    vowel_pur = input('Would you like to purchase vowel? Y/N').upper()   #ask if want to purchase vowel
                                    if not vowel_pur.isalpha():
                                        print('That was not a valid input. Please try again') #check input
                                    elif vowel_pur == 'Y':  #yes, wants a vowel
                                        condition5 = False 
                                        while condition5 is False:
                                            if sum_bank3 >= 250:  #check if enough money to purchase vowel
                                                condition6 = False
                                                while condition6 is False:
                                                    vowel_guess = input('Please guess your vowel: ')  #guesses vowel
                                                    if not vowel_guess.isalpha():
                                                        print('That was not a vowel. Plesae guess a vowel') #input check
                                                    elif vowel_guess in consonants:  
                                                        print('That was a consonant. Please guess a vowel')  #avoid consonant guess
                                                    else:
                                                        if vowel_guess in word:            #check if vowel in target word
                                                            word_vowel_index = [index for index, i in enumerate(word) if i == vowel_guess] #getting index of word that matches vowel guess
                                                            display = ''.join(vowel_guess if index in word_vowel_index else i for index, i in enumerate(display))  #replacing display index with index of word that matches vowel guess
                                                            sum_bank3-=250                    #substracting vowel price from player's guess
                                                            print(display)           #printing updated display
                                                            condition7 = False
                                                            while condition7 is False:
                                                                word_guess = input('Do you want to guess the word? Y/N').upper()     #checking if wants to guess the full word
                                                                if not word_guess.isalpha():
                                                                    print('That was not a valid input. Please try again')     #check input
                                                                elif word_guess == 'Y':          #if wants to guess
                                                                    condition8 = False
                                                                    while condition8 is False:
                                                                        word_guess_final = input('Guess your word": ')       #input for word guess
                                                                        if not word_guess_final.isalpha():
                                                                            print('That was not alphabetic word. Please only use alpha charachters')     #input check
                                                                        elif word_guess_final == word:            #if guessed word matches target word, round ends
                                                                            print('Great guess, you won!!!')
                                                                            player_3+=1             #if word guessed corectly, player receives 1 score
                                                                            print(f'The ward you guessed is {word}')
                                                                            condition8 = True
                                                                            condition7 = True
                                                                            condition6 = True
                                                                            condition5 = True
                                                                            condition4 = True
                                                                            condition3 = True
                                                                            condition2 = True
                                                                        else:
                                                                            print("Sorry, that was wrong word. You lose your turn. Now it's next player's turn")   #word didn't match
                                                                            condition8 = True
                                                                            condition7 = True
                                                                            condition6 = True
                                                                            condition5 = True
                                                                            condition4 = True
                                                                            condition3 = True
                                                                            condition2 = True
                                                                elif len(word_guess) > 1:
                                                                    print('That was not a valid answer. Please input Y/N')
                                                                else:
                                                                    print("You used your turn. Now it's next player's turn")   #if doesn't want to guess the word, loses turn
                                                                    condition7 = True
                                                                    condition6 = True
                                                                    condition5 = True
                                                                    condition4 = True
                                                                    condition3 = True
                                                                    condition2 = True
                                                        else:
                                                            print("Sorry, that vowel doesn't exist in target word. You lose your turn. Now it's next player's turn")    #guessed wrong vowel. loses turn
                                                            condition6 = True
                                                            condition5 = True
                                                            condition4 = True
                                                            condition3 = True
                                                            condition2 = True
                                            else:
                                                print(f"Sorry, you need at least 250 in you bank to buy vowel. You have only {sum_bank3} in your bank")    #doesn't have enough money in bank to purchase vowel
                                                condition9 = False
                                                while condition9 is False:
                                                    word_guess = input('Do you want to guess the word? Y/N').upper()    #if not enough money to buy vowel, check if want's to guess the word
                                                    if not word_guess.isalpha():
                                                        print('That was not a valid input. Please try again')  #input check
                                                    elif word_guess == 'Y':    #if wishes to guess the word
                                                        condition10 = False
                                                        while condition10 is False:
                                                            word_guess_final = input('Guess your word: ')   #guessing the word
                                                            if not word_guess_final.isalpha():
                                                                print('That was not alphabetic word. Please only use alpha charachters')     #input check
                                                            elif word_guess_final == word:      #if guee mathces the target word, round ends
                                                                print('Great guess, you won!!!')
                                                                player_3+=1                #player recevies 1 score if guesses the word
                                                                print(f'The ward you guessed is {word}')
                                                                condition10 = True
                                                                condition9 = True
                                                                condition5 = True
                                                                condition4 = True 
                                                                condition3 = True
                                                                condition2 = True
                                                            else:
                                                                print("You used your turn. Now it's next player's turn")     #loses turn, if did not guess corect word
                                                                condition10 = True
                                                                condition9 = True
                                                                condition5 = True
                                                                condition4 = True 
                                                                condition3 = True
                                                                condition2 = True
                                                    else:
                                                        print("You used your turn. Now it's next player's turn")    #doesn't want to guess the word, losses turn
                                                        condition9 = True
                                                        condition5 = True
                                                        condition4 = True
                                                        condition3 = True
                                                        condition2 = True
                                    else:                                    #if doesn't want to purchase vowel
                                        condition9 = False
                                        while condition9 is False:
                                            word_guess = input('Do you want to guess the word? Y/N').upper()     #check if wants to guess the target word
                                            if not word_guess.isalpha():
                                                print('That was not a valid input. Please try again')    #input check
                                            elif word_guess == 'Y':      #yes, wants to guess the word
                                                condition10 = False
                                                while condition10 is False:
                                                    word_guess_final = input('Guess your word: ')    #word guess input
                                                    if not word_guess_final.isalpha():
                                                        print('That was not alphabetic word. Please only use alpha charachters')   #input check
                                                    elif word_guess_final == word:            #if guessed word matches target word, round ends
                                                        print('Great guess, you won!!!')
                                                        player_3+=1       #player receives 1 score ig guesses target word correctly
                                                        print(f'The ward you guessed is {word}')
                                                        condition10 = True
                                                        condition9 = True
                                                        condition8 = True
                                                        condition7 = True
                                                        condition5 = True
                                                        condition4 = True 
                                                        condition3 = True
                                                        condition2 = True
                                                    else:
                                                        print('That was wrong word. You lose your turn now')
                                                        condition10 = True
                                                        condition9 = True
                                                        condition8 = True
                                                        condition7 = True
                                                        condition5 = True
                                                        condition4 = True 
                                                        condition3 = True
                                                        condition2 = True
                                            else:
                                                print("You used your turn. Now it's next player's turn")    #if doesn't want to guess the word, losses turn
                                                condition9 = True
                                                condition8 = True
                                                condition7 = True
                                                condition5 = True
                                                condition4 = True 
                                                condition3 = True
                                                condition2 = True
                                                
                        else:              #if letter guessed is not in word, loses turn
                            print("Your guess is wrong. Next player get's the turn")
                            condition3 = True
                            condition2 = True
                
                elif len(guess) > 1:     #if guess is a word
                    if guess == word:     #if guess matches target word, round ends
                        sum_bank3+=spin_result
                        player_3+=1         #player receives 1 score
                        print('Phenomenal guess, great job. You won!!!')
                        print(f'The ward you guessed is {word}')
                        condition3 = True
                        condition2 = True
                    else:     #if word guess is wrong, losses turn
                        print('That was wrong guess. You lose your turn')
                        condition3 = True
                        condition2 = True                
                else:   #if guess is empty entry
                    print('That was empty entry. Please try again')
    return sum_bank3, player_3
                
                    
#CREATING GAME LOGIC-----------------------------------------------------------------------------------------------

#Print game header and welcome message
print('WELCOME TO WHEEL OF FORTUNE GAME')
print('================================')
print()


#create a loop to run round 1
condition11 = False
while condition11 is False:    
    print(f'Current bank amounts: player 1:{bank1}, player 2:{bank2}, player 3:{bank3}')
    print('Player 1 takes the turn')
    print(f'Current display: {display}')
    player1_round1(0, 0)
    if player_1 != 1:
        print(f'Current bank amounts: player 1:{bank1}, player 2:{bank2}, player 3:{bank3}')
        print('Player 2 takes the turn')
        print(f'Current display: {display}')
        player2_round1(0, 0)
        if player_2 != 1:
            print(f'Current bank amounts: player 1:{bank1}, player 2:{bank2}, player 3:{bank3}')
            print('Player 3 takes the turn')
            print(f'Current display: {display}')
            player3_round1(0, 0)
            if player_3 != 1:
                continue
            else:
                print('Player 3 won this round')
                print(f'Current bank amounts: player 1:{bank1}, player 2:{bank2}, player 3:{bank3}')
                condition11 = True
        else:
            print('Player 2 won this round')
            print(f'Current bank amounts: player 1:{bank1}, player 2:{bank2}, player 3:{bank3}')
            condition11 = True
    else:
        print('Player 1 won this round')
        print(f'Current bank amounts: player 1:{bank1}, player 2:{bank2}, player 3:{bank3}')
        condition11 = True

#resetting random word
word_list = open(r'words.txt')
random_word = random.choice(word_list.readlines()).lower()
#clean white spaces from random word
word = random_word.strip()
 
#resetting display       
display = ''
for i in word:
    display+='_'
print()            
print('WELCOME TO ROUND TWO')
print('====================')
player_1_1 = player_1
player_2_2 = player_2
player_3_3 = player_3
condition12 = False
while condition12 is False:
    print(f'Current bank amounts: player 1:{sum_bank1}, player 2:{sum_bank2}, player 3:{sum_bank3}')
    print('Player 1 takes the turn')
    print(f'Current display: {display}')
    player1_round2(0, 0)
    if player_1 != (player_1_1+1):
        print(f'Current bank amounts: player 1:{sum_bank1}, player 2:{sum_bank2}, player 3:{sum_bank3}')
        print('Player 2 takes the turn')
        print(f'Current display: {display}')
        player2_round2(0, 0)
        if player_2 != (player_2_2+1):
            print(f'Current bank amounts: player 1:{sum_bank1}, player 2:{sum_bank2}, player 3:{sum_bank3}')
            print('Player 3 takes the turn')
            print(f'Current display: {display}')
            player3_round2(0, 0)
            if player_3 != (player_3_3+1):
                continue
            else:
                print('Player 3 won this round')
                print(f'Current bank amounts: player 1:{sum_bank1}, player 2:{sum_bank2}, player 3:{sum_bank3}')
                condition12 = True
        else:
            print('Player 2 won this round')
            print(f'Current bank amounts: player 1:{sum_bank1}, player 2:{sum_bank2}, player 3:{sum_bank3}')
            condition12 = True
    else:
        print('Player 1 won this round')
        print(f'Current bank amounts: player 1:{sum_bank1}, player 2:{sum_bank2}, player 3:{sum_bank3}')
        condition12 = True
                          
bank_player1 = bank1+sum_bank1
bank_player2 = bank2+sum_bank2
bank_player3 = bank3+sum_bank3
highest_bank = max(bank_player1, bank_player2, bank_player3)

if bank_player1 == highest_bank:
    print(f'Player 1 with bank amount of {highest_bank} wins both rounds and goes to round 3')
elif bank_player2 == highest_bank:
    print(f'Player 2 with bank amount of {highest_bank} wins both rounds and goes to round 3')
elif bank_player3 == highest_bank:
    print(f'Player 3 with bank amount of {highest_bank} wins both rounds and goes to round 3')
    
    
#ROUND 3

#resetting random word
word_list = open(r'words.txt')
random_word = random.choice(word_list.readlines()).lower()
#clean white spaces from random word
word = random_word.strip()

print()
print('WELCOME TO ROUND 3')
print('==================')

#list of pre approved letters to reveal if matched
letters_list = ['r','s','t','n','l','e']

#resetting display       
display = ''
for i in word:
    display+='_'

#revealing pre approved letters in display
for i in word:
    if i in letters_list:
        indexes = [index for index, x in enumerate(word) if x == i]
        display = ''.join(i if index in indexes else char for index, char in enumerate(display))
        
print(f'This is your current dispay: {display} with (R,S,T,N,L,E) matched letters revealed')
print()

#create variable to store player guesses
player_guesses = []

#geting first consonant-guess
condition13 = False
while condition13 is False:
    consonant1 = input('Please guess your 1st consonant: ')
    consonant2 = input('Please guess your 2st consonant: ')
    consonant3 = input('Please guess your 3st consonant: ')
    if (consonant1 and consonant2 and consonant3) in consonants:
        player_guesses.append(consonant1)
        player_guesses.append(consonant2)
        player_guesses.append(consonant3)
        condition13 = True
    else:
        print('Not all your guesses were consonants, please guess 3 consonants')
        
condition14 = False
while condition14 is False:
    vowel1 = input('Please guess your vowel: ')
    if vowel1 in vowels:
        player_guesses.append(vowel1)
        condition14 = True
    else:
        print('That was not a vowel. Please guess a vowel')
        
#revealing pre approved letters in display
for i in word:
    if i in player_guesses:
        indexes = [index for index, x in enumerate(word) if x == i]
        display = ''.join(i if index in indexes else char for index, char in enumerate(display))
print()        
print(f'This is your display after revealing your matched guesses {display}')
print()
      
final_guess = input('Please make your final word guess: ')
if final_guess == word:
    print()
    print(f'Congratulation, you won!!! You guessed correct word: {word}')
    print(f'You will take home you bank amount of {highest_bank} and round 3 prize, which is: Chevrolett Camaro')
else:
    print()
    print('Sorry, that was wrong asnwer. You lost')
    print(f'You will take home only your bank amount of {highest_bank} today')


# In[ ]:





# In[ ]:





# In[ ]:




