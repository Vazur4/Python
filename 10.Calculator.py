def add(a,b):
    return a + b

def menos(a,b):
    return  a -b 

def multy(a,b):
    return a * b

def divide(a,b):
    return a/b

def calc(op,a,b):

    result = 0
    if operator in "+":
        result = add(a,b)
    elif operator in "-":
        result = menos(a,b)
    elif operator in "*":
        result = multy(a,b)
    elif operator in "/":
        result = divide(a,b)

    return result
    
    
    

operation = {
    "+" : sum,
    "-" : menos,
    "*" : multy,
    "/" : divide,

}

select = ""
op = False

while not op:
    a = int(input("What's  the first number?: "))
    op2 =  False
    while not op2:   
    
    
        print("+\n-\n*\n/")
        operator = input("Pick an operator: ")
        b  = int(input("What's the next number?: "))

        result = operation[operator](a,b)

        print(f"{a} {operator} {b} = {result}")
        select = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ")
        if select in "y":
            a = result
            op2 =False
        else:
            op2 = True
