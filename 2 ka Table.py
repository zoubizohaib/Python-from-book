Value = int(input("Pleae enter a number : "))
MaxItration  = int(input("How many reading do you want to get : "))

for n in range(1, (MaxItration+1)):
    Ans = Value*n
    print(str(Value) + " X " + str(n) + " = " + str(Ans))