import random
import os
import art

def clear_screen(): #courtesy chatgpt no idea how or why this works
    os.system('cls' if os.name == 'nt' else 'clear')

def DisplayGuesses(display):
    for i in display:
        print(i,end=" ")

def DisplayHints(hints):
    if (len(hints)==1) and hints[0]=="done":
        return
    print("\nHINTS",end=":")
    for i in hints:
        if i=="done":
            continue
        print(i,end="    ")

print("✨✨ WELCOME TO MULTIPLAYER HANGMAN! ✨✨")
print("There are 2 roles for the players: The givers and the guessers. Players keep alternating their roles between the two.")
print("Givers enter a word and some hints for the word, Guessers try to guess the word given.")
print("🏁🏁 GAME STARTS NOW! 🏁🏁")

word_to_guess=input("Givers enter the word you want guessers to guess.\n")
print("Enter some hints about the word.Enter 'done' when you've given all the hints.")
hints=[]
h=""
while(h!="done"):
    h=input()
    hints.append(h)        
clear_screen()

display=[]
for i in range (len(word_to_guess)):
    display.append("__")
print("YOUR WORD IS:")
DisplayGuesses(display)

guessed_letters=[]
wrong_guess=0
while (wrong_guess!=8):
    DisplayHints(hints)
    character_guessed=input("\nGuess a letter!\n").lower()
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
        print("\nGUESSERS WIN!! HANGMAN IS FREE! HE'S A MAN NOW!!")
        art.HangManArt(9)
        quit()
    print("\nGuessed letters:",end=" ")
    print(guessed_letters)
if(wrong_guess==8):
    print("❌HANG THE MAN!❌")
    print("🎊🎊 GIVERS WIN! 🎊🎊")
    print("The word was "+word_to_guess)
