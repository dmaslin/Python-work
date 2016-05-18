def decimalToBinary(num):
    return str(bin(num)[2:])

num = eval(input("Enter a number: "))

print(str(num)+" is "+decimalToBinary(num)+" in binary")
