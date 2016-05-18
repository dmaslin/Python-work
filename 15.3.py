def gcd(m, n):
    if m%n == 0:
        print("The Greatest Common Demonimator is "+str(n))
    elif m%n != 0:
        gcd(n, m%n)

x, y = eval(input("Enter two numbers: "))
if x > y:
    gcd(y, x)
else:
    gcd(x, y)
