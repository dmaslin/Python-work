from math import sqrt
class PrimeIterator:
    def __init__(self):
        self.number = 2# Current two consecutive fibonacci number
    def __next__(self):
        while True:
            # Assume the number is prime
            isPrime = True  # Is the current number prime?
            # Test if number is prime
            for divisor in range(2, int(sqrt(self.number)) + 1): 
                # If true, number is not prime
                if self.number % divisor == 0:
                    isPrime = False  # Set isPrime to false          
                    break  # Exit the for loop

            # Print the prime number and increase the count
            
            if isPrime:
                self.prime = self.number
                self.number +=1
                return self.prime
            self.number +=1

    def __iter__(self):
        return self
    
def main():
    iterator = PrimeIterator()
    i = 0
    prime = []
    while i < 1000:
        prime.append(next(iterator))
        i +=1
    for i in range(len(prime)):
        if i % 10 == 0:
            print("")
        print(format(prime[i], "5.0f"), end = " ")
        

main()
