import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def WinOrLoose(ch1,ch2):
    if ch1==ch2:
        return -1
    if ch1=="R":
        if ch2=="P": return 2
        else: return 1
    if ch1=="P":
        if ch2=="R": return 1
        else: return 2
    if ch1=="S":
        if ch2=="R": return 2
        else: return 1

def display(choice):
    if choice=="R":
        print(rock)
    elif choice=="P":
        print(paper)
    elif choice=="S":
        print(scissors)
        
print("Welcome to rock paper scissors! It's you against python. Let's see who wins 😈")
rounds=int(input("how many rounds would you like to play?   "))
count=1
user=auto=0
while(count<=rounds):
    print(f"🏁🏁🏁ROUND {count}🏁🏁🏁")
    og_choice=input("Enter R for rock,P for papers and S for scissors.\n")
    choice=og_choice.upper()
    auto_choice=random.choice(["R","P","S"])
    print("\033[1mYOU PLAYED:\033[0m")
    display(choice)
    print("\033[1mPYTHON PLAYED:\033[0m")
    display(auto_choice)
    outcome=WinOrLoose(choice,auto_choice)
    if outcome==1: 
        user+=1
        print(f"You win round {count}!")        
    elif outcome==2: 
        auto+=1
        print(f"Python wins round {count}!")        
    elif outcome==-1:
        count-=1
        print("PLAY AGAIN")        
    count+=1    
    
if rounds>1:
    if user>auto:
        print(f"\033[1m🎉🎊🥳YOU WON {user} ROUNDS! YOU WIN!🎉🎊🥳\033[0m")
        print('''
            _\|/^
             (_oo /
            /-|--/
            \ |
              /--i
             /   L
             L''')
    elif auto>user:
        print(f"\033[1mPYTHON WON {auto} ROUNDS! PYTHON WINS!YOU LOOSE!!\033[0m")
        print('''
                          .-=-.          .--.
              __        .'     '.       /  " )
      _     .'  '.     /   .-.   \     /  .-'\\
     ( \   / .-.  \   /   /   \   \   /  /    ^
      \ `-` /   \  `-'   /     \   `-`  /
       `-.-`     '.____.'       `.____.'
            ''')
    else:
        print("\033[1mITS A DRAW!\033[0m")
else:
    if user>auto:
        print(f"\033[1m🎉🎊🥳YOU WIN!🎉🎊🥳\033[0m")
        print('''
            _\|/^
             (_oo /
            /-|--/
            \ |
              /--i
             /   L
             L''')
    elif auto>user:
        print(f"\033[1mPYTHON WINS!YOU LOOSE!!\033[0m")
        print('''
                          .-=-.          .--.
              __        .'     '.       /  " )
      _     .'  '.     /   .-.   \     /  .-'\\
     ( \   / .-.  \   /   /   \   \   /  /    ^
      \ `-` /   \  `-'   /     \   `-`  /
       `-.-`     '.____.'       `.____.'
            ''')
