
#? 🎯 Challenge  Generate the first n Fibonacci numbers with a generator

def isnum(userInput):      # Chechking for userInput is digit or not
    try:
        intNum = int(userInput)

        if intNum <= 0 :   # As Fibonanci start with 0 and 1
            print('Please Enter a positive number - Not Allowed :',userInput)            
        else:
            return intNum
    except Exception as e:  # If user_input is <=0 or alphabets
        print("Invalid literal:", userInput)  

def fiboSeries():  # Fibonacci series with a generator
    a, b = 0, 1
    while True:
        yield a    #? YEILD
        a, b = b, a+b  

def mainFun():
    user_num = input("Enter a number to Generate Fibonacci Series ")
    checknum = isnum(user_num) 

    if checknum is None:
        return None
    
    for i in fiboSeries():       
        if i < checknum: #Condition if i become checknum end it as i -- 0 1 1 2 3  # 3<5 #!False
            print(i)
        else:
            break
        
print('\nExecution Started')
mainFun()
print('Execution ✅ \n ')













