# 1.print prime number from 1 to N


n = int(input("Enter Number :"))

for i in range(1, n + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i, "is a prime number")
