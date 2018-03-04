import math as m

# Print menu and input user command
def menuprint():
    """
    Documentations
    """
    print("Options:")
    print("Enter '+' to add two numbers")
    print("Enter '-' to substract two numbers")
    print("Enter '*' to multiply two numbers")
    print("Enter '/' to devide two numbers")
    print("Enter 'q' to end the program")
    user_input=input(": ")
    return user_input 

def fadd(num1,num2):
    result=num1+num2
    return result

def fsub(num1,num2):
    result=num1-num2
    return result

def fmul(num1,num2):
    result=num1*num2
    return result

def fdiv(num1,num2):
    result=num1/num2
    return result

# main
avail_oper=['+','-','*','/','q']
names_oper=["add","substract","multipy","devide"]

# print(m.sqrt(25)) 

while True:
    idx_oper=0
    user_input=menuprint()

    if user_input not in avail_oper:
        print("Unknown input") 
        continue

    idx_oper=avail_oper.index(user_input)

    if user_input=="q":
        break

    print(idx_oper)
    print(names_oper[idx_oper])

    num1=float(input("Enter a number 1: "))
    num2=float(input("Enter a number 2: "))
    
    if user_input=="+":
        operation=fadd
    elif user_input=="-":
        operation=fsub
    elif user_input=="*":
        operation=fmul
    elif user_input=="/":
        operation=fdiv
    
    print("Answer : "+str(operation(num1,num2)))
