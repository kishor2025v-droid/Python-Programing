def addition():
    ch1, ch2 = input("enter two values separated by space\n").split()
    print(int(ch1) + int(ch2))

def multiply():
    ch1, ch2 = input("enter two values separated by space\n").split()
    print(int(ch1) * int(ch2))

print ("hello Python") 
print (1+1)
ch = input("enter value: 1 for addition and 2 for multiplication\n ")
if(ch == "1"):
    addition()
elif (ch == "2"):
    multiply()