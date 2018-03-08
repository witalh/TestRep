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
    print("Enter 'l' to view log file")
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
    #strlog=str(num1)+oper+str(num2)+"="+str(rez)
    strlog="{}{}{}={}\n".format(num1,oper,num2,rez)
    #print(strlog)
    filelog.write(strlog)
    filelog.close
    return

def viewlog():
    fname="calc.log"
    filelog=open(fname,"r")
    strlog=filelog.read()
    print("---- Log Operations ----")
    print(strlog)
    print("------ End of Log ------")

    analyslog(strlog)
    
    filelog.close
    return

def analyslog(strlog):
    avail_oper=['+','-','*','/']
    stat={}

    l=len(strlog)
    print("Length: "+str(l))

    for c in avail_oper:
        stat[c]=0
    stat['all']=0    

    print(stat)    

    for c in strlog:
        if c in avail_oper:
            stat[c]+=1
            stat['all']+=1
    print(stat)
    print("---- Statistic Operations ----")
    for c in stat:
        print("{0}:{1} - {2}%".format(c,stat[c],round(100*stat[c]/stat['all'],2))) 
            
            

    return

def getoper(user_input):
    if user_input=="+":
        operation=fadd
    elif user_input=="-":
        operation=fsub
    elif user_input=="*":
        operation=fmul
    elif user_input=="/":
        operation=fdiv
    else:
        operation=None

    return operation

# main
avail_oper=['+','-','*','/','q','l']
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

    if user_input=="l":
        viewlog()
        continue

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
    
    operation=getoper(user_input)
    if operation==None:
        print("Invalid operation")
        continue
        
    rez=operation(num1,num2)
    flog(user_input,num1,num2,rez)
    print("Answer : "+str(rez))
