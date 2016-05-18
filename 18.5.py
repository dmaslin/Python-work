from math import sqrt
from stack import Stack

stk = Stack()

number = 2  # A number to be tested for primeness
count = 0
# Repeatedly find prime numbers
while number <= 10000000000:
    # Assume the number is prime
    isPrime = True  # Is the current number prime?
    # Test if number is prime
    for divisor in range(2, int(sqrt(number)) + 1): 
        # If true, number is not prime
        if number % divisor == 0:
            isPrime = False  # Set isPrime to false          
            break  # Exit the for loop

    # Print the prime number and increase the count
    if isPrime:
        count += 1
        stk.push(number)
    if count == 50:
        break
        
    # Check if the next number is prime
    number += 1

print("The first fifty primes are as follows:")
for i in range(50):
    if i%10 == 0:
        print("")
    print(format(stk.pop(), "5.0f"), end = " ")
