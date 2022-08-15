import math
a=float(input("Digite A: "))
b=float(input("Digite B: "))
c=float(input("Digite C: "))
d=b**2-(4*a*c)
x1=0.0
x2=0.0
if d==0:
    x1=x2=-b/(2*a)
elif d>0:
    x1=(-b+(b**2-4*a*c)**(0.5))/(2*a)
    x2=(-b-(b**2-4*a*c)**(0.5))/(2*a)
else:
    x1=x2="No tiene solución"
print(f"El valor de X1 es: {x1}")
print(f"El valor de X2 es: {x2}")
