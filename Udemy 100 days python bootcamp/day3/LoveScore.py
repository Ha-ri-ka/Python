Og_name1=input("Enter the first name:")
Og_name2=input("Enter the second name:")
name1=Og_name1.upper()
name2=Og_name2.upper()
true_occurences=0
love_occurences=0
for i in range (len(name1)):
    if name1[i]=="T" or name1[i]=="R" or name1[i]=="U" or name1[i]=="E":
        true_occurences+=1
    if name1[i]=="L" or name1[i]=="O" or name1[i]=="V" or name1[i]=="E":
        love_occurences+=1
for i in range (len(name2)):
    if name2[i]=="T" or name2[i]=="R" or name2[i]=="U" or name2[i]=="E":
        true_occurences+=1
    if name2[i]=="L" or name2[i]=="O" or name2[i]=="V" or name2[i]=="E":
        love_occurences+=1

love_score=int(str(true_occurences)+str(love_occurences))
if love_score<=10 or love_score>=90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score>=40 and love_score<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.") 
