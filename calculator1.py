import os
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

operations_dicts={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division
}

def calculator():

    num1 = float(input("Enter the 1st number:"))
    for i in operations_dicts:
        print(i)

    continue_flag = True
    while continue_flag :

        symbol = input("Pick the operation you want to perform: ")

        num2 = float(input("Enter the 2nd number:"))

        calculate = operations_dicts[symbol]
        output = calculate(num1,num2)
        print(f"{num1} {symbol} {num2} = {output}")

        continues = input(f"Enter 'y' to continoue calculation with {output} or 'n' to start new calculation 'x' to exit :").lower()

        if continues == 'y' :
            num1 = output
        elif continues == 'n' :
            continue_flag = False
            calculator()
        else:
            continue_flag = False
            print("calculations are over")

calculator()



        
        






