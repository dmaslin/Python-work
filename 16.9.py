from math import sqrt
def primeNumbers():
    number = 2  # A number to be tested for primeness
    count = 0
    goal = 10
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
        if number > goal:
            print("There are "+str(count - 1)+" prime numbers less than "+str(goal))
            goal = goal * 10
        
        # Check if the next number is prime
        number += 1
    print("There are "+str(count)+" prime numbers less than "+str(goal))
    
primeNumbers()
