Og_name1=input("Enter the first name:")
Og_name2=input("Enter the second name:")
Og_Combined=(Og_name1+Og_name2).upper()
true_occurences=Og_Combined.count("T")+Og_Combined.count("R")+Og_Combined.count("U")+Og_Combined.count("E")
love_occurences=Og_Combined.count("L")+Og_Combined.count("O")+Og_Combined.count("V")+Og_Combined.count("E")
love_score=int(str(true_occurences)+str(love_occurences))

if love_score<=10 or love_score>=90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score>=40 and love_score<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
