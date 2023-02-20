from replit import clear


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operation={"+":add,
"-":subtract,
"*":multiply,
"/":divide,
}
def calculator():
    num1=float(input("Enter first no :  "))


    print("Which operation do you want to do??")
    for keys in operation:
        print(keys)
    want_do="y"
    while want_do=="y":
        ops=input("Pick operation :  ")
        num2=float(input("Enter next no :  "))
        ans= operation[ops](num1,num2)
        print(f" {num1} {ops} {num2} = {ans}")
        want_do=input(f"Enter y to continue and with {ans} or type n to to start new calculator")
        if want_do=="y":
            num1=ans
        else:
            clear()
            calculator()


calculator()