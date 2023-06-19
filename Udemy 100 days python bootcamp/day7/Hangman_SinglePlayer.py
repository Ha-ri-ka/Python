import random
import os
import art
from word_list import words

def clear_screen(): #courtesy chatgpt no idea how or why this works
    os.system('cls' if os.name == 'nt' else 'clear')

def DisplayGuesses(display):
    for i in display:
        print(i,end=" ")

word_to_guess=random.choice(words)

display=[]
for i in range (len(word_to_guess)):
    display.append("__")
print("YOUR WORD IS:")
DisplayGuesses(display)

guessed_letters=[]
wrong_guess=0
while (wrong_guess!=8):
    character_guessed=input("Guess a letter!\n").lower()
    clear_screen()
    if character_guessed not in guessed_letters:
        guessed_letters.append(character_guessed)
    else:
        print(f"You've already guessed {character_guessed}")
    if character_guessed in word_to_guess:
        for i in range (len(word_to_guess)):
            if word_to_guess[i]==character_guessed:
                display[i]=character_guessed                
        art.HangManArt(wrong_guess)
        DisplayGuesses(display)
    else:
        print("WRONG GUESS")
        wrong_guess+=1
        art.HangManArt(wrong_guess)
        DisplayGuesses(display)
    if display==list(word_to_guess):
        print("\nYOU WON OMG CONGRATS!! HANGMAN IS FREE! HE'S A MAN NOW!!")
        art.HangManArt(9)
        quit()
    print("\nGuessed letters:",end=" ")
    print(guessed_letters)
if(wrong_guess==8):
    print("❌HANG THE MAN!❌")
    print("The word was "+word_to_guess)
    print("better luck next time!!")
