A,B,C,D= input(f"Digite los números A,B,C,D que forman N: ").split(",")
A=str(A)
B=str(B)
C=str(C)
D=str(D)
N=A+B+C+D  
N=int(N)  
if(N<=(int(A)*1000+int(B)*100+50)):
    N=N-int(C+D)
elif(N>(int(A)*1000+int(B)*100+50)):
    N=(N-int(C+D))+100
print(f"El resultado redondeado es: {N}")