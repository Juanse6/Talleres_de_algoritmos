N=str(input("Escriba su nombre: "))
C=float(input("Digite el valor de su compra: "))
if(C<50000):
    X="0%"
    D=C*0
    T=C-D
elif(50000<=C<100000):
    X="5%"
    D=C*0.05
    T=C-D 
elif(100000<=C<700000):
    X="11%"
    D=C*0.11 
    T=C-D
elif(700000<=C<1500000):
    X="18%"
    D=C*0.18
    T=C-D
else: 
    X="25%"
    D=C*0.25
    T=C-D

print(f"Estimado {N}")
print(f"Elm total de su compra es de: {C} COP")
print(f"Se le aplico un descuento de {X} equivalente a: {D} COP")
print(f"El total de la compra es de: {T} COP")