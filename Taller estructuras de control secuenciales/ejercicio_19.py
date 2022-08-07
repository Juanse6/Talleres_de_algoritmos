#Ejercicio 19
x=int(input("Digite cantidad de naranjas compradas: "))
y=int(input("Digite el precio por una docena de naranjas: "))
k=int(input("Digite el precio por el cual se vendieron las naranjas: "))
inv=(x*y)/12
stonks=(k-inv)*100/inv
print("El porcentaje de ganancia en la inversion es:",stonks)
