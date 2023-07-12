while True:
    print("Menu:\n Enter 1 to sum numbers from 1 to n \n Enter 2 to evaluate 2 numbers exprestion(e.g.2+3)\nEner 3 to end program")
    n= int(input("choice from 1 to 3:"))
    if 1>n>3:
        print("invalid input... try again")
        continue
    elif n ==1 :
        res=0
        cnt=0
        number = int(input("enter a number:"))
        while cnt<=number:
            res=res+number
            number-=1
        print(res)
    elif n==2:
        Total = None
        num1_1, operater, num2_2=  input("enter a simple expression").split()
        num1= int(num1_1)
        num2= int(num2_2)
        if operater == "+":
            Total = num1+num2
        elif operater == "-":
            Total = num1 - num2
        elif operater == "*":
            Total = num1*num2
        elif operater == "**":
            Total = num1**num2
        if operater == "//"or "/":
            if num2 ==0:
                print("no wat to compute this expression")
            else:
                if operater == "/":
                    Total = num1/num2
                elif operater == "//":
                    Total = num1//num2
        if Total !=None:
            print('Expression value is ', Total)
    else:
        break

