from collections import OrderedDict
import numpy as np
def SortDictionary(subjects):
    keys = list(subjects.keys())
    values = list(subjects.values())
    sorted_values_indices = np.argsort(values)[::-1]
    sorted_dict = {keys[i]: values[i] for i in sorted_values_indices}
    return sorted_dict

def check(r1,r2,r3,r4,r5):
    if (r1<0 or r2<0 or r3<0 or r4<0 or r5<0):
        return -1
    if (r1>5 or r2>5 or r3>5 or r4>5 or r5>5):
        return -1
    return 1

def PrintSubjects(n,subjects):
    count = 0
    for key, value in subjects.items():
        print(f"\033[1m{count+1}.{key} with {value} stars\033[0m")
        count += 1
        if count == n:
            break
print("Welcome to CHOICE HELPER!🤓\nI will help you choose a subject to work on,based on how your ratings for it in different criterias.📚📖📝")
subs=input("Enter your subjects seperated by a single space:\n").split(" ")
if (len(subs)==1 or len(subs)==0):
    print(f"you should study {subs[0]}")    
    quit()
subjects={}
for i in subs:
    subjects[i]=0
print("⭐⭐ Rate your subjects for each the questions out of 5.You may even use decimal rating!⭐⭐")
for i in subjects.keys():
    print("🟣 Please give the ratings for "+i.upper()+".")
    r1=float(input("Amount of homework/assignments that need to be done for the subject:"))
    r2=float(input("Importance of this subject towards your grades/goals:"))
    r3=float(input("Personal opinion about how well you know the subject:"))
    r4=float(input("Amount of time you've spent on the subject already:"))
    r5=float(input("interest in the subject at this point of time:"))
    if(check(r1,r2,r3,r4,r5)==-1):
       print("❌Please enter a rating that is between 0 and 5.❌")
       quit()
    subjects[i]=r1+r2+r3-r4+r5
Sorted_Subjects=SortDictionary(subjects)
if len(subs)>=3:
    print("\n✨✨✨The top 3 subjects that you could work on based on your ratings are✨✨✨")
    PrintSubjects(3,Sorted_Subjects)
    print("💖 HAPPY STUDYING!! 💖")
else:
    print(f"\n✨✨✨The subject you could work on based on your ratings is✨✨✨")
    PrintSubjects(1,Sorted_Subjects)
    print("💖 HAPPY STUDYING!! 💖")
