#Ejercicio 3
v1=int(input("Ingrese la primera venta: "))
v2=int(input("Ingrese la segunda venta: "))
v3=int(input("Ingrese la tercera venta: "))
base=int(input("Ingrese el sueldo base: "))
comision=(v1+v2+v3)*0.10
st=comision+base
print(f"La comision por las tres ventas es: {comision} y el sueldo total con comision es: {st}")
