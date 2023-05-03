# 3.shuffle the string using any explam

string = input("enter string  ")
shuffle_string = " "
for index in range (len(string)):
    n = int(input("enter number :"))
    shuffle_string += string[n]
print(shuffle_string)

