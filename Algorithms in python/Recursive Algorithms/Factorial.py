def RecursiveFactorial(n):
    if n==1 or n==0:
        return 1
    return RecursiveFactorial(n-1) * n

num=int(input("enter the number:"))
if num<0:
    print("factorial of negative numbers cannot be computed.")
    quit()
print(f"{num}!={RecursiveFactorial(num)}")
