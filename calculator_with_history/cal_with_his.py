HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE,'r')
    lines = file.readlines()
    if len(lines) == 0 :
        print("No History found")
    else :
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE,'w')
    file.close()
    print("History is cleared")

def save_to_history(equation, result):
    file = open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result)+ "\n")
    file.close()

def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3 :
        print("Invald input , input should be (number opreator number)")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result =  num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0 :
            result =  num1 / num2
        else:
            return
    else:
        print("Invalid operator!!")
        return
    
    if int(result) == result :
        result = int(result)
        print("RESULT :", result)
        save_to_history(user_input,result)

def main():
    print("---SIMPLE CALCULATOR (HISTORY , CLEAR , EXIT)---")
    while True:
        user_input = input("Enter calculation ( eg . 3 + 4 , 1 * 7) or commands (history , clear , exit) : ").strip().lower()
        if user_input == 'exit':
            print("Thank you , bye bye")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else :
            calculator(user_input)

main()




        


       
    

    