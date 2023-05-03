"""8. solid half diamond
given an integer N, write a program to print the solid half diamond pattern in (2*N-1) rows and N columns similar to the pattern shown below

input
5
output
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*"""

n = int(input("enter number : "))
for i in range (1,n+1):
    print("* " * i)
    if i == n:
        for j in range (n-1,0,-1):
            print("* " * j)