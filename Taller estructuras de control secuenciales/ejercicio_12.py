#Ejercicio 12
m1=float(input("Digite nota Matematicas 1 "))
m2=float(input("Digite nota Matematicas 2 "))
m3=float(input("Digite notaMatematicas 3 "))
mf=float(input("Digite nota final Matematicas "))
f1=float(input("Digite nota Fisica 1 "))
f2=float(input("Digite nota Fisica 2 "))
ff=float(input("Digite nota final Fisica "))
q1=float(input("Digite nota Quimica 1 "))
q2=float(input("Digite nota Quimica 2 "))
q3=float(input("Digite nota Quimica 3 "))
qf=float(input("Digite nota final Quimica "))
mm=(((m1+m2+m3)/3)*0.1)+(mf*0.9)
ff=(((f1+f1)/2)*0.2)+(ff*0.8)
qq=(((q1+q2+q3)/3)*0.15)+(qf*0.85)
prom=(mm+qq+ff)/3
print("El promedio de las tres notas es " + str(prom))