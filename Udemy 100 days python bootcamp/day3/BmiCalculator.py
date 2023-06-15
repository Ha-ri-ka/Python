height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi=weight/(height*height)
if bmi<=18.5:
    print(f"your bmi is {round(bmi)}, you are "+ "\033[1munderweight\033[0m") #prints the conclusion in bold
elif bmi<=25:
    print(f"your bmi is {round(bmi)}, you have a "+ "\033[1mnormal weight\033[0m")
elif bmi<=30:
    print(f"your bmi is {round(bmi)}, you are "+ "\033[1mslightly overweight\033[0m")
elif bmi<=35:
    print(f"your bmi is {round(bmi)}, you are "+ "\033[1mobese\033[0m")
else:
    print(f"your bmi is {round(bmi)}, you are "+ "\033[1mclinically obese\033[0m")
