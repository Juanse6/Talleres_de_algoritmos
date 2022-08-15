A=float(input("Ingrese la lectura anterior: "))
B=float(input("Ingrese la lectura actual: "))
if(A>=0 and B<=100):
    M=(B-A)*4600
elif(A>=101 and B<=300):
    M=(B-A)*80000
elif(A>=301 and B<= 500):
    M=(B-A)*100000
else:
    (A>=501 and B>501)
    M=(B-A)*120000
print(f"El monto que debe pagar por servicios de luz electrica y servicio de aseo urbano es de: {M}")