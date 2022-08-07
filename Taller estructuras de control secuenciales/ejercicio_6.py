#Ejercicio 6
m=int(input("Digite cantidad de mujeres: "))
h=int(input("Digite cantidad de hombres: "))
estudiantes=m+h
mp=(m*100)/estudiantes
hp=(h*100)/estudiantes
print(f"El procentaje de mujeres es: {round (mp,2)} y el porcentaje de hombres es: {round (hp,2)}")
