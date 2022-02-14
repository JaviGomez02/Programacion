dinero=10
dinerototal=0
for cont in range(1,20):
    print(str(cont)+" "+str(dinero))
    dinero=dinero*2
    dinerototal=dinerototal+dinero
print("20 "+str(dinero))
print("El dinero total es "+str(dinerototal))