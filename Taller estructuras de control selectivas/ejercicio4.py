M=float(input("\nDime el valor total de la compra "))
if (M>5000000):
    F=float(M*0.55)
    C=float(M*0.25)
    P=float(M*0.30)
    I=float(C*0.20)
else:
    F=float(M*0.70)
    C=float(M*0.30)
    I=float(C*0.20)
    P=0
print(f"Los fondos utilizados de la empresa son: {F}")
print(f"El credito al fabricante es de: {C}")
print(f"Por intereses del fabricante se tiene: {I}")
print(f"El prestamo del banco es de: {P}")