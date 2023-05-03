
"""6.numbers in square-3
given a number N write a program to print a square of N rows using numbers starting from 1 (note there is a space after every Number)
input
4
output
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16"""

n = int(input("Enter number : "))
c = 1
for i in range(n):
    for j in range(n):
        print(c,end=" ")
        c+=1
    print(" ")

