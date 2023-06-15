print("YOOOOO tip calcy right hereeeee")
tot=float(input("how much was your total? "))
tip_percent=float(input("how much % would you like to tip? "))
tip=(tip_percent/100)*tot
ppl=int(input("how many people are splitting this? "))
choice=int(input("are ya'll splitting equally?(1 for yes,0 for no):"))
if choice==1:
    final=round((tot+tip)/ppl,2)    
    print(f"each person pays {final}")
elif choice==0:
    for i in range (ppl):
        person_i_amount=int(input(f"enter amount for person {i+1}:"))
        person_i_pays=round(person_i_amount+(tip/ppl),2)
        print(f"person {i+1} pays {person_i_pays}")

