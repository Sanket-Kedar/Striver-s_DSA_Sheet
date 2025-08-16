'''
* 
* * 
* * *
* * * *
* * * * *
* * * * * *
'''

n = int(input())

for row in range(n):
    for col in range(row+1):
        print('*', end=" ")
    print('\n')


'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
'''



for row in range(1,n+1):
    for col in range(1,row+1):
        print(col, end=" ")
    print('\n')



'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
'''


for row in range(1,n+1):
    for col in range(1,row+1):
        print(row, end=" ")
    print('\n')
