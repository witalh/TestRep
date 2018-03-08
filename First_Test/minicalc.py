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

def flog(oper,num1,num2,rez):
    fname="calc.log"
    filelog=open(fname,"a")
    strlog=str(num1)+oper+str(num2)+"="+str(rez)
    #print(strlog)
    filelog.write(strlog+"\n")
    filelog.close
    return

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

    #num1=float(input("Enter a number 1: "))
    #num2=float(input("Enter a number 2: "))

    try:
        num1=input("Enter a number 1: ")
        num1=float(num1)
    except:
        print("'"+str(num1)+"' is not number. try again")
        continue

    try:
        num2=input("Enter a number 2: ")
        num2=float(num2)
    except:
        print("'"+str(num2)+"' is not number. try again")
        continue
    
    if user_input=="+":
        operation=fadd
    elif user_input=="-":
        operation=fsub
    elif user_input=="*":
        operation=fmul
    elif user_input=="/":
        operation=fdiv
        
    rez=operation(num1,num2)
    flog(user_input,num1,num2,rez)
    print("Answer : "+str(rez))
