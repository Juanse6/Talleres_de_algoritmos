I=float(input("Ingrese la inversión en el banco: "))
T=float(input("Ingrese la tasa de interes: "))
interes=I*T
D=I+interes
if interes>100000:
    print(f"El interes es mayor a 100000 COP: {interes} COP y puede reinvertir")
else:
    print(f"El interes es menor a 100000 COP: {interes} COP ")
print(f"El dinero total en la cuenta es de: ${D} COP")