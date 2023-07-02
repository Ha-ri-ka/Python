import time
import CoffeeArt
import os
def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')

milk=500
coffee=500
water=1000
money=0
products={'latte':{'milk':150,'coffee':24,'water':200,'cost':30},
          'espresso':{'milk':0,'coffee':18,'water':50,'cost':20},
          'capuccino':{'milk':100,'coffee':24,'water':250,'cost':50}}

def report():
    print("\nMachine report")
    print(f"milk={milk}ml\ncoffee={coffee}g\nwater={water}ml\nmoney= ₹{money}")

def Transaction(choice):
    GivenMoney=0
    print("Please make payment.")
    notes=[int(note) for note in input("Enter your notes separated by spaces: ").split()]
    GivenMoney=sum(notes)
    if GivenMoney==products[choice]['cost']:
        return 'success'
    if GivenMoney>products[choice]['cost']:
        change=GivenMoney-products[choice]['cost']
        print(f"Here is your change:₹{change}")
        return 'success'
    else:
        print("Insufficient money given.\nMoney refunded.")
        return 'failed'

def CheckResources(choice):
    if milk<products[choice]['milk']:
        return 'no'
    if coffee<products[choice]['coffee']:
        return 'no'
    if water<products[choice]['water']:
        return 'no'
    return 'yes'

def Serve(choice):
    global milk
    global water
    global coffee
    global money
    display="BREWING"
    for i in display:
        print(i,end=' ')
        time.sleep(0.7)
    milk=milk-products[choice]['milk']
    coffee=coffee-products[choice]['coffee']
    water=water-products[choice]['water']
    money=money+products[choice]['cost']
    print(f"\nEnjoy your {choice}!!")
    print(CoffeeArt.cup)
    time.sleep(2)
    clear_screen()

choice='run'
while(choice!='off'):
    print(CoffeeArt.machine)    
    ch=input("\nEspresso:₹20-->E\nlatte:₹30-->L\ncapuccino:₹50-->C\nWhat would you like to have?  ").upper()
    if ch=='E': choice='espresso'
    if ch=='L': choice='latte'
    if ch=='C': choice='capuccino'
    if choice=='off':
        break
    if choice=='report':
        report()
    else:
        available=CheckResources(choice)        
        if(available=='yes'):
            status=Transaction(choice)
            if status=='success':
                Serve(choice)
            else:
                time.sleep(2)
                clear_screen()
        else:
            print(f"Sorry,{choice} is unavailable.")
            time.sleep(2)
            clear_screen()
print("POWER OFF")
