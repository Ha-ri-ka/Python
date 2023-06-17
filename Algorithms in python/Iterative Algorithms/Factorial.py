def IterativeFactorial(n):
    p=1
    for i in range (n):
        p=p*n
        n=n-1
    return p

num=int(input("enter the number:"))
if num<0:
    print("factorial of negative numbers cannot be computed.")
    quit()
print(f"{num}!={IterativeFactorial(num)}")
