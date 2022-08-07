#Ejercicio 9
ht=int(input("Ingrese las horas trabajadas: "))
hp=float(input("Ingrese el precio por hora: "))
sueldo=ht*hp
descuento=sueldo*0.20
salario_neto=sueldo-descuento
print(f"El descuento fijo es: {descuento} y el salario neto es: {salario_neto}")
