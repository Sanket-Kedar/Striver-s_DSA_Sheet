# Perfect Number

num = int(input())

if num==1:
    print("Not a perfect number")
sum=1
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        sum += i + num//i
if sum==num:
    print("Perfect number")
else:
    print("Not a perfect number")
