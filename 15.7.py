class fibb():
    def __init__(self):
        self.counter = 0
        index = eval(input("Enter an index for a Fibonacci number: "))
        f = self.fib(index)
        # Find and display the Fibonacci number
        print("The number of times the fib module is called is ", str(self.counter))

    # The function for finding the Fibonacci number 
    def fib(self, index):
        self.counter +=1
        if index == 0: # Base case
            return 0
        elif index == 1: # Base case
            return 1
        else:  # Reduction and recursive calls
            return self.fib(index - 1) + self.fib(index - 2)

fibb() # Call the main function
