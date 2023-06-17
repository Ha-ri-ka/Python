import random

length=int(input("Enter the length you'd like for your password:"))
spl=int(input("Enter number of special characters you'd like to include:"))
nums=int(input("Enter number of digits you'd like to include:"))
#create a list of ALL special symbols available in ascii chart.
All_Special_Symbols=[]
for i in range(33,48):
    All_Special_Symbols.append(chr(i))
for i in range(58,65):
    All_Special_Symbols.append(chr(i))
for i in range(91,97):
    All_Special_Symbols.append(chr(i))

#create a list of all upper and lower alphabets
All_Alphabets=[]
for i in range (65,91):
    All_Alphabets.append(chr(i))
for i in range (97,123):
    All_Alphabets.append(chr(i))

numbers=[]
letters=[]
symbols=[]

for i in range (spl):
    symbols.append(random.choice(All_Special_Symbols))

for i in range (nums):
    numbers.append(str(random.randint(0,9)))

for i in range (length-spl-nums):
    letters.append(random.choice(All_Alphabets))


pwd=symbols+numbers+letters
pwd = random.sample(pwd, length)  
#random.shuffle(pwd)
password=""
for i in range (length):
    password+=pwd[i]
print("Your password is\n"+password)
