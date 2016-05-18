from stack import Stack
x = input("Please enter a postfix expression, please space in between characters: ").split()
stk = Stack()
s = ""
opperations = {"+", "-", "*", "/"}
for i in range(len(x)):
    if x[i] in opperations:
        s = s + str(stk.pop())
        s = s + x[i]
        s = s + str(stk.pop())
        s = s.split()
        s.reverse()
        s = "".join(s)
        s = eval(s)
        stk.push(str(s))
        s = ""
    else:
        stk.push(x[i])
s = stk.peek()
print("The answer is "+ s)
