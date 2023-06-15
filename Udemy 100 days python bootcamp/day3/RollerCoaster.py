print("ceck if you're eligible to have fun on the roller coster lol")
height=int(input("enter your height in cm:"))
if height>=120:
    print("YOU CAN HAVE FUN!!")
    choice=int(input("Do you want to take a picture on the ride? (1 for yes, 0 for no):"))    
    age=int(input("enter your age:"))
    if age<12:
        if choice==1:
            print("Child tickets are $5, $3 for picture. your total is $8")
        else:
            print("Child tickets are $5")
    elif age <=18:
            if choice==1:
                print("Teen tickets are $7, $3 for picture. your total is $10")
            else:
                print("teen tickets are $7")
    else:
        if choice==1:
            print("Adult tickets are $12, $3 for picture. your total is $15")
        else:
            print("Adult tickets are $12")
else:
    print("sorry, no roller coaster funsies for you :(")
