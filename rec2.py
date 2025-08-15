#Factorial of a number

def factorial(i,n,fact=1):
    if i>n:
        return fact
    return factorial(i+1,n,fact*i)

n = int(input())
print(factorial(1,n))

