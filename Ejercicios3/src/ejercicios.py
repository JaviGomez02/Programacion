#Ejercicio 1
def factorial(num):
    if num==0:
        result=1
    elif num>0:
        result=1
        while num>0:
            result=result*num
            num=num-1
    elif num<0:
        result=-1
    return result

#Ejercicio 2
def leapYear(num):
    if num==0:
        result=-1
    elif (num%4==0 and num%100!=0) or num%400==0:
        result=1
    else:
        result=-1
    return result

#Ejercicio 3
def daysInMonth(mes, anno):
    if mes<1 or mes>12 or anno<=0:
        numeroDias=-1
    elif mes==4 or mes==6 or mes==9 or mes==11:
        numeroDias=30
    elif mes==2 and leapYear(anno)==1:
        numeroDias=29
    elif mes==2:
        numeroDias=28
    else:
        numeroDias=31
    return numeroDias



#Ejercicio 4

def dayOfWeek(day, month, year):
    a=(14-month)/12
    y=year-a
    m=month+12*a-2
    d=round((day+y+y/4-y/100+y/400+(31*m)/12)%7)
    return (d)

#Ejercicio 5
def myPower(num, num2):
    result=1
    if num2==0:
        result=1
    elif num2<0:
        result=-1
    else:
        while num2>=1:
            result=result*num
            num2=num2-1
    return result


#Ejercicio 6
def numberOfNumbers(num):
    result=1
    if num<=0:
        result=-1
    else:
        while num//10>1:
            result=result+1
            num=num//10
    return result

# Ejercicio 7
def isPrime(num):
    if num<=0:
        result=-1
    else:
        esPrimo=True
        cont=2
        while cont <= num//2 and esPrimo==True:
            if (num%cont==0):
                esPrimo=False
            cont=cont+1
        if esPrimo==True:
            result=1
        else:
            result=0
    return result

# Ejercicio 8
def secondOrder(a, b, c):
    if a==0:
        result=-1
    elif (b**2-4*a*c)<0:
        result=0
    elif (b**2-4*a*c)==0:
        result=1
    elif (b**2-4*a*c)>0:
        result=2  
    return result

#Ejercicio 9
def numberDivisorPrime(num):
    result=0
    if num<0:
        result=-1
    else:
        for i in range(2,num):
            if (isPrime(i)==1)and(num%i==0):
                result+=1
    return result

        
#Ejercicio 10
def friend(num1, num2):
    sumadiv=0
    for i in range(1, num1):
        if num1%i==0:
            sumadiv=sumadiv+i
    if sumadiv==num2:
        result=True
    elif sumadiv!=num2:
        result=False
    return result
            


    

    













        
