A,B,C,D=input(f"Digite los números A,B,C,D: ").split(",")
A=int(A)
B=int(B)
C=int(C)
D=int(D)
if(D==0):
    R=(A-C)**2
elif(D>0):
    R=((A-B)**3)/D
print(f"El resultado es: {R}")