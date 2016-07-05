import random
x=random.randint(0,1000)
y=eval(input("Enter a number between 0 and 1000: "))
counter = 0
while counter < 4 and x != y:
    if x > y:
        print("Sorry your number was too small")
    if x < y:
        print("Sorry your number was too large")
    print("You have ", 4 - counter," tries left")
    counter = counter + 1
    y=eval(input("Enter another number between 0 and 1000: "))


if x == y:
    print("Congrats you win!")

if counter == 4:
    import os
    os.system("c:\\windows\\system32\\shutdown.exe -r")
    print("THE NUMBER WAS OBVIOUSLY ", x,"!!!!!!!!!")
    print("YOU FAIL!!!! COMPUTER NOW RESTARTING!!!!")

