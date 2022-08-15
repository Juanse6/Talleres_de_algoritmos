t=float(input("digitela temperatura: "))
d=""
if(t>85 and t<=120):
    d="Natación"
elif(t>70 and t<=85):
    d="Tenis"
elif(t>32 and t<=70):
    d="Golf"
elif(t>10 and t<=32):
    d="Esquí"
elif(t>0 and t<=10):
    d="Marcha"
else:
    d="La temperatura no pertenece a ningun deporte"
print(f"El deporte a practicar es {d}")