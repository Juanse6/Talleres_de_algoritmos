a=int(input("Digite el primer número (Dividendo): "))
b=int(input("Digite el Segundo número (Divisor): "))
d=int(a/b)
c=0
for i in range(d):
    print(f"{a}-{b}={a-b}")
    a=a-b
    c=c+1
print(f"El resto de la division es: {a} y el cociente es: {c}")