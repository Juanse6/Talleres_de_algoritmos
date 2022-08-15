B=float(input("Digite el salario bruto: "))
if(B<900000):
    N=(B*0.15)+B
else:
    N=(B*0.12)+B
print(f"El salio neto es de: ${N} COP")