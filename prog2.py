# 2 print the prime number from M to N M=2 N=10

m = int(input("Enter number: "))
n = int(input("Enter number : "))
prime = " "
for i in range (m,n+1):
    count = 0
    for j  in range (2,i):
        if i % j == 0:
            count  += 1
    if count == 0:
        prime = prime +str(i)+" "

if len(prime) > 0:
    print(prime)
else:
    print("no prime number")
