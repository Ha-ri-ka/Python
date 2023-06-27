import os
def clear_screen(): #courtesy chatgpt no idea how or why this works
    os.system('cls' if os.name == 'nt' else 'clear')

def addition(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

def PrintOperators():
    print("Operators available:")
    for key in functionality.keys():
        print(key)

def GetResult(num1,op,num2):
    for key in functionality.keys():
        if key==op:
            result=functionality[key](num1,num2)
    return result    

functionality={
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":division
    }
def calculator():
    clear_screen()
    n1=float(input("Enter num1:"))
    PrintOperators()
    op=input("Choose operator:")
    n2=float(input("Enter num2:"))

    res=GetResult(n1,op,n2)
    print(f"{n1} {op} {n2} = {res}")

    choice=input("Do you wish to work on the result? (yes/no)  ").lower()
    iter=0
    while choice=='yes':
        clear_screen()
        iter+=1    
        if iter==1:
            num1=res
        else:
            num1=result
        print(f"num1:{num1}")
        PrintOperators()
        oper=input("Choose operator:")
        num2=float(input("Enter num2:"))
        result=GetResult(num1,oper,num2)
        print(f"{num1} {oper} {num2} = {result}")
        choice=input("Do you wish to work on the result? (yes/no)\n").lower()
    if choice=='no':
        if input("Do you want to start a new calculation? (yes/no) ").lower()=='yes':
            calculator()
        else:
            quit()
calculator()
