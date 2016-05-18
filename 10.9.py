def deviation(mean, list1):
    sd = 0
    for i in range(0, len(list1)):
        sd += (list1[i] - mean)**2
    return (sd/(len(list1) - 1))**.5
def mean(list1):
    total = 0
    for i in range(0,len(list1)):
        total += list1[i]
    mean = total/len(list1)
    return mean

data = input('Enter numbers: ')
data = data.split(" ")
for i in range(0,len(data)):
    data[i] = float(data[i])
mean = mean(data)
deviation = deviation(mean, data)
print("The mean is "+format(mean, ".2f"))
print("The standard deviation is "+format(deviation, ".5f"))
