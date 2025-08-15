#Sum of First N Numbers

def sum_of_first_n(i,n,sum=0):
    if i>n:
        return sum
    return sum_of_first_n(i+1,n,sum=sum+i)


n = int(input())
print(sum_of_first_n(1,n))