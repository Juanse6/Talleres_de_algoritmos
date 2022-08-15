M=int(input("Ingrese cantidad de dinero: $"))
B1=(M-M%100000)/100000
M=M%100000
B2=(M-M%50000)/50000
M=M%50000
B3=(M-M%20000)/20000
M=M%20000
B4=(M-M%10000)/10000
M=M%10000
B5=(M-M%5000)/5000
M=M%5000
B6=(M-M%2000)/2000
M=M%2000
B7=(M-M%1000)/1000
M=M%1000
M1=(M-M%500)/500
M=M%500
M2=(M-M%200)/200
M=M%200
M3=(M-M%100)/100
M=M%100
M4=(M-M%50)/50
M=M%50
if(B1>0):
    print(f"La Cantidad de billetes de 100000 es de: {B1}")
if(B2>0):
    print(f"La Cantidad de billetes de 50000 es de: {B2}")
if(B3>0):
    print(f"La Cantidad de billetes de 20000 es de: {B3}")
if(B4>0):
    print(f"La Cantidad de billetes de 10000 es de: {B4}")
if(B5>0):
    print(f"La Cantidad de billetes de 5000 es de: {B5}")
if(B6>0):
    print(f"La Cantidad de billetes de 2000 es de: {B6}")
if(B7>0):
    print(f"La Cantidad de billetes de 1000 es de: {B7}")
if(M1>0):
    print(f"La Cantidad de monedas de 500 es de: {M1}")
if(M2>0):
    print(f"La Cantidad de monedas de 200 es de: {M2}")
if(M3>0):
    print(f"La Cantidad de monedas de 100 es de: {M3}")
if(M4>0):
    print(f"La Cantidad de monedas de 50 es de: {M4}")