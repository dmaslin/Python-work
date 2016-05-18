numbers = input('Enter integers between 1 and 100: ')
numbers = numbers.split(" ")
for x in range(0,len(numbers)):
    numbers[x] = int(numbers[x])
for i in range(1,101):
    if i in numbers:
        if numbers.count(i) > 1:
            print(str(i)+" occurs "+str(numbers.count(i))+" times")
        else:
            print(str(i)+" occurs "+str(numbers.count(i))+" time")
