
clave=1234
password=int(input("ingrese su clave "))
intentos=3

while clave!=password and intentos<-0:
    
    intentos=intentos-1
    print("quedan", (intentos) ,"intentos")
    print("error, contraseña incorrecta")

    password=int(input("intente denuevo ")) 

if intentos>=0:
    print("ya no hay mas intentos")
else:
    print("bienvenido usuario")
