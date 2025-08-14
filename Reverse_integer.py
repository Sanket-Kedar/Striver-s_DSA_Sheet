x = int(input())
sum = 0
temp = abs(x)
while temp>0:
    rem = temp % 10
    sum = sum*10 + rem
    temp = temp // 10
if x<0:
    print(-sum)
else:
    print(sum)



#using string

x = int(input())
sign = -1 if x<0 else 1
ans = int(str(abs(x))[::-1])
print(ans * sign)