def main():
    s = input("Enter a string: ").strip()
    reverseDisplay(s);

def reverseDisplay(value):
    for i in range(1, len(value)+1):
        reverseDisplayHelper(value, i)

def reverseDisplayHelper(value, helper):
    print(value[len(value) - helper], end = "")
main()
