lista=[0,1,2,3,4,5,6,7,8,9,10]
num=int(input("Introduce el número que quieres ver: "))
mult=0
if num>=0 and num<=10:
    while mult<=10:
        print(str(num)+"*"+str(mult)+"="+str(num*mult))
        mult+=1
else:
    print("El número debe ser entre 0 y 10")