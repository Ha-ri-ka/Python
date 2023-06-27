import os
def clear_screen(): #courtesy chatgpt no idea how or why this works
    os.system('cls' if os.name == 'nt' else 'clear')

def FindHighestBidder(bid_dict):
    highest=0
    for key,value in bid_dict.items():
        if value>highest:
            highest=value
            bidder=key
    return bidder 

Bidders_and_Bids={}
choice="yes"
while(choice=="yes"):
    key=input("Enter name of bidder:")
    Bidders_and_Bids[key]=int(input("Enter Bid:"))
    choice=input("Are there more bidders?").lower()
    clear_screen()
winner=FindHighestBidder(Bidders_and_Bids)
print(f"{winner} bags the highest bid at {Bidders_and_Bids[winner]} rupees!")
