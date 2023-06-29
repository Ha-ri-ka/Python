import random
import BlackJackUtility
import os
def clear_screen(): #courtesy chatgpt no idea how or why this works
    os.system('cls' if os.name == 'nt' else 'clear')

deck=BlackJackUtility.deck

def DrawCard():
    '''Returns a random card from the deck and removes it from the deck.'''
    card=random.choice(deck)
    deck.remove(card)
    return card
    
def InitialTwo():
    '''Adds two cards to the dealer and the player's hands.'''
    for i in range(2):
        dealer.append(DrawCard())
        player.append(DrawCard())
    print(f"Dealer: {dealer[0]}")
    print(f"You: {player}  {CardValue(player)}")

def ClearRound(dealer,player):
    '''Adds the hands of the player and dealer back to the deck and clears both hands.'''
    deck.extend(dealer)
    deck.extend(player)
    dealer.clear()
    player.clear()

def CardValue(cards):
    '''Returns the value of cards in hand.'''
    value=0
    for i in cards:
        if i=='J' or i=='K' or i=='Q':
            value+=10
        elif i=='A':
            if(11+value>21): ace=1 
            else: ace=11
            value+=ace
        else:
            value+=i
    return value

def DoubleDown(dealer,player,bet,bankroll):
    print(f"bet={bet}")
    player.append(DrawCard())
    print(f"player: {player}   {CardValue(player)}")
    while(CardValue(dealer)<17):
                print("Dealer hits",end='  ')
                dealer.append(DrawCard())
                print(dealer)
    print(f"Dealer: {dealer}  {CardValue(dealer)}")
    if CardValue(dealer)>21:
                print("You win.")
                bankroll=bankroll+(2*bet)
                print(f"Balance:{bankroll}")
                ClearRound(dealer,player)
                return bankroll
    if(CardValue(dealer)>CardValue(player)): 
        print("You loose.")
        bankroll=bankroll-bet
        print(f"Balance:{bankroll}")
        ClearRound(dealer,player)
        return bankroll
    if(CardValue(player)>CardValue(dealer)): 
        print("You win.")
        bankroll=bankroll+(2*bet)
        print(f"Balance:{bankroll}")
        ClearRound(dealer,player)
        return bankroll
    else:
        print("Push")
        ClearRound(dealer,player)
        return bankroll


def round(bankroll):
    '''One round of BlackJack'''
    bet=int(input("Your bet: "))
    if (bet>bankroll):
        print("You cannot bet more than your available balance.")
        return bankroll
    InitialTwo()
    if CardValue(player)==21: 
        print("BLACKJACK")
        bankroll=bankroll+(1.5*bet)
        print(f"Balance:{bankroll}")
        ClearRound(dealer,player)
        return bankroll
    if (CardValue(player)==9 or CardValue(player)==11 or CardValue(player)==10):
            DblDwn=input("Double down? (yes/no)  ").lower()
            if DblDwn=='yes':
                bet+=bet 
                bankroll=DoubleDown(dealer=dealer,player=player,bet=bet,bankroll=bankroll)
                return bankroll                     
    choice=input("Hit  Stay\n").lower()        
    while(choice=='hit'):
        player.append(DrawCard())
        print(f"{player}   {CardValue(player)}")
        if (CardValue(player)==9 or CardValue(player)==11 or CardValue(player)==10):
            DblDwn=input("Double down? (yes/no)  ").lower()
            if DblDwn=='no':
                continue
            if DblDwn=='yes':
                bet+=bet 
                bankroll=DoubleDown(dealer=dealer,player=player,bet=bet,bankroll=bankroll)
                return bankroll   
        elif CardValue(player)>=21:
            break
        else: choice=input("choose\nHit  Stay\n").lower()
    if CardValue(player)==21:
            print("BLACKJACK")
            bankroll=bankroll+(1.5*bet)
            print(f"Balance:{bankroll}")
            ClearRound(dealer,player)
            return bankroll
    if CardValue(player)>21:
        print("You loose.")
        print(f"Dealer: {dealer}  {CardValue(dealer)}")
        bankroll=bankroll-bet
        print(f"Balance:{bankroll}")
        ClearRound(dealer,player)
        return bankroll
    if choice=='stay':
        while(CardValue(dealer)<17):
            print("Dealer hits",end='  ')
            dealer.append(DrawCard())
            print(dealer)
        print(f"Dealer: {dealer}  {CardValue(dealer)}")
        print(f"player: {player}  {CardValue(player)}")
        if CardValue(dealer)>21:
            print("You win.")
            bankroll=bankroll+(2*bet)
            print(f"Balance:{bankroll}")
            ClearRound(dealer,player)
            return bankroll
        if(CardValue(dealer)>CardValue(player)): 
            print("You loose.")
            bankroll=bankroll-bet
            print(f"Balance:{bankroll}")
            ClearRound(dealer,player)
            return bankroll
        if(CardValue(player)>CardValue(dealer)): 
            print("You win.")
            bankroll=bankroll+(2*bet)
            print(f"Balance:{bankroll}")
            ClearRound(dealer,player)
            return bankroll
        else:
            print("Push")
            ClearRound(dealer,player)
            return bankroll

def BlackJack(bankroll):    
    choice='yes'
    while(choice=='yes'):
        print(f"Balance={bankroll}")
        bankroll=round(bankroll)
        if bankroll==0:
            reload=input("You are out of balance. Would you like to reload? (yes/no)  ").lower()
            if reload=='yes':
                bankroll=int(input("Add reload amount:"))
            else:
                print("Sorry, you cannot continue with zero balance.\nGoodbye.")
                quit()
        choice=input("Continue to next round? (yes/no)\n").lower()
        clear_screen()
    print(f"Your final balance is {bankroll}.\nGoodbye.")

dealer=[]
player=[]
print("Welcome to Moon casino's BlackJack.\nHere's how we play\n")
print("BlackJack pays 3 to 2")
print("Dealer must draw to 16 and stand on all 17's")
print("Outscoring the dealer doubles your bet.")
print("Double down on 9, 10, and 11 to turn the tables.")
print("\nMay the cards be in your favour\n")
bankroll=int(input("Enter your bankroll: "))
BlackJack(bankroll)
