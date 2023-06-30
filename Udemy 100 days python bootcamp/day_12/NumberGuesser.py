import random
import art 
import time
import os
def clear_screen(): #courtesy chatgpt no idea how or why this works
    os.system('cls' if os.name == 'nt' else 'clear')

def round():
    number=random.randint(1,100)
    level=input("Choose a difficulty level:(easy/hard) ").lower()
    if level=='easy':
        chances=10
    if level=='hard':
        chances=5
    elif level!='easy' and level!='hard':
        print("Invaid input.")
        return
    #print(f"debugger {number}")
    guess=int(input("Enter your guess!\n"))
    while (guess!=number):    
        chances=chances-1
        if chances==0:
            looser="LOOSER"
            for j in ("LOOSER"):
                print(j,end=' ')
                time.sleep(0.2)
            print(f"\nYou're out of chances :(\nThe number was {number}.\nBetter luck next time!")
            return
        print(f"{chances} chances left.")
        if guess>=number+10:
            print("Too high!")
        elif guess<=number-10:
            print("Too low!")
        elif guess>number:
            print("Go lower")
        elif guess<number:
            print("Go higher!")
        guess=int(input("Enter your guess!\n"))
    if guess==number:
        clear_screen()
        for i in range(3):
            print(art.winner)
            time.sleep(0.5)                
        return

greeting='Welcome to \033[1mNUMBER GUESSER!\033[0m'
for i in greeting:
    print(i,end='')
    time.sleep(0.05)
print("\nGuess the number that I'm thinking of correctly and WIN!")
choice='yes'
while(choice=='yes'):
    round()
    choice=input("Play another round? (yes/no)  ").lower()
    clear_screen()
print(art.goodbye)  
