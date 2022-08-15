D=float(input("Ingrese los kilómetros recorridos: "))
if(D<=300):
    M=50000
elif(D>300 and D<1000):
    M=70000+(D-300)*30000
else:
    M=150000+(D-1000)*9000
print(f"El monto a pagar es de: ${M} COP")