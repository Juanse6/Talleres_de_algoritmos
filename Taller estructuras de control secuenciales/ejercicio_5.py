#Ejercicio 5
n1=float(input("Ingrese la primera calificación: "))
n2=float(input("Ingrese la segunda calificación: "))
n3=float(input("Ingrese la tercera calificación: "))
nf=float(input("Ingrese la calificación del examen final: "))
tf=float(input("Ingrese la calificación del trabajo final: "))
promedio=(n1+n2+n3)/3
p_parcial=promedio*0.55
pnf=nf*0.30
ptf=tf*0.15
calificacion=p_parcial+pnf+ptf
print("La calificación final es:",calificacion)