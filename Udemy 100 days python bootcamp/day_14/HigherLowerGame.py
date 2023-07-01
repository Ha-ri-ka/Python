import Data
import art
import random
import os
def clear_screen(): #courtesy chatgpt no idea how or why this works
    os.system('cls' if os.name == 'nt' else 'clear')

def round():
    guess=answer='x'
    score=0
    while(guess==answer):
        compare=random.choices(Data.data,k=2)
        print(f"score={score}")
        print("Guess who has higher followers!")
        print(f"A-->{compare[0]['name']},{compare[0]['description'],{compare[0]['country']}}")
        print(art.vs)
        print(f"B-->{compare[1]['name']},{compare[1]['description'],{compare[1]['country']}}")
        if(compare[1]['follower_count']>compare[0]['follower_count']): answer='B'
        else: answer='A'
        guess=input("Guess (A/B)  ").upper()
        if guess==answer:
            score=score+1
            clear_screen()
            print("CORRECT!!")
            print(f"{compare[0]['name']}-->{compare[0]['follower_count']} million followers")
            print(f"{compare[1]['name']}-->{compare[1]['follower_count']} million followers")            
        else:
            print("WRONG")
            print(f"Final score={score}")
            print(f"{compare[0]['name']}-->{compare[0]['follower_count']} million followers")
            print(f"{compare[1]['name']}-->{compare[1]['follower_count']} million followers")
            return score

print(art.logo)
choice='yes'
while(choice=='yes'):
    sc=round()
    choice=input("Continue to next round?(yes/no)  ").lower()
    clear_screen()
print(f"Final score is {sc}.\nGOODBYE!!")
