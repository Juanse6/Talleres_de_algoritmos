a=0
g=0
d=0
while True:
    c=int(input())
    if (c==1):
        a=a+1
    elif(c==2):
        g=g+1
    elif(c==3):
        d=d+1
    elif(c==4):
        break
    else:
        c=c
print("MUITO OBRIGADO")
print(f"Alcool: {a}")
print(f"Gasolina: {g}")
print(f"Diesel: {d}")