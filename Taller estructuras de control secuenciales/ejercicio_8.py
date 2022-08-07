#Ejercicio 8
import math
ladoa=float(input("Digite lado a "))
ladob=float(input("Digite lado b "))
ladoc=float(input("Digite lado c "))
semi=(ladoa+ladob+ladoc)/2
area=math.sqrt(semi*(semi-ladoa)(semi-ladob)(semi-ladoc))
print("El área es"+str(area))