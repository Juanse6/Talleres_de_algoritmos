#Ejercicio 14
l1=int(input("Ingrese la lectura anterior de kilovatios: "))
l2=int(input("Ingrese la lectura actual de kilovatios: "))
l3=int(input("Ingrese el costo por kilovatio: "))
monto=abs(l2-l1)*l3
print("El monto total a pagar en un mes de luz es:",monto)
