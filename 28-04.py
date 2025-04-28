
# suma=0
# while True:
#     num=int(input("ingrese un numero , cero para salir :"))
#     if num==0:
#         break
#     suma+=num
#     print(suma)
# print(F"La suma total es {suma}")


# import random

# print("ingrese 2 numeros")
# num=int(input("ingrese el primer numero "))
# num2=int(input("ingrese otro numero mayor que el anterior "))

# while num<=num2:
#     print("el numero debe ser mayor al anterior ")
#     num2=int(input("ingrese otro numero mayor que el anterior "))

# numram=random.randint(num,num2)

# print(f"el numero elegido entre ellos fue {numram}")

# import random

# print("este juego se trata de adivinar el rango de un numero")

# nram=random.randint(1,50)

# num=int(input("se genero un numero aleatorio del 1 hasta el 50, adivina el numero"))
# intentos=8

# while nram!=num:
#     intentos=intentos-1
#     if intentos==0:
#         break
#     if num<nram:
#         print(f"intente otra vez, el numero es mayor, te quedan {intentos} intentos")
#         num=int(input())
#     else:
#         print(f"el numero es menor, te quedan {intentos} intentos")
#         num=int(input())

# if intentos==0:
#     print("na, malo")
# else:
#     print("felicidades, adivinaste el numero")


# STREET FIGHTER


# import random

# hp1=50
# hp2=50



# while hp1>=0 and hp2>=0:

#     n1r=random.randint(5,8)
#     n2r=random.randint(5,14)
#     n3r=random.randint(6,12)
#     n4r=random.randint(7,14)

#     print('''Ryu y Ken empezeran a pelear, usted es Ryu, usted comienza primero, eliga sus ataques
          
#           1.- Hadoken 
#           2.- Shoryuken 
#           3.- Tatsumaki Senpukyaku 
          
#           ''')
    
#     op=int(input())
    
#     if op==1:
#         hp2=hp2-n1r
#         hp1=hp1-n2r
#         print(f"usted uso Hadoken, ken quedo con {hp2} puntos de vida, ken ataco y lo dejo con {hp1} de vida")
#     elif op==2:
#         hp2=hp2-n3r
#         hp1=hp1-n2r
#         print(f"usted uso Shoryuken, ken quedo con {hp2} puntos de vida, ken ataco y lo dejo con {hp1} de vida")

#     elif op==3:
#         hp2=hp2-n4r
#         hp1=hp1-n2r
#         print(f"usted uso Tatsumaki Senpukyaku, ken quedo con {hp2} puntos de vida, ken ataco y lo dejo con {hp1} de vida")
#     else:
#         print("eliga una opción valida")

# if hp1<hp2:
#     print("usted perdio")
# else:
#     print("you win")



# while True:
#     print('''
#     1.- opcion 1
#     2.- opcion 2
#     3.-salir

#     ''')


    # op=int(input("selecione una opción "))

    # if op==1:
    #     print("opcion 1")
    # elif op==2:
    #     print("opcion 2")
    # elif op==3:
    #     print("salir")
    #     break





tarjeta=20000

b5k=5
b10k=5
b20k=5
b2k=5
b1k=10



print("retire dinero del cajero,")

while True:
    print('''caunto dinero quiere retirar?
          
        1.- 5000
        2.- 10000
        3,. 20000
        4.- 50000
        5.- otro
          ''')
    
    op=int(input("selecione una opción "))

    if op==1:
        print("usted retiro 5000")
        tarjeta=tarjeta-5000
        
    elif op==2:
        print("opcion 2")
    elif op==3:
        print("salir")
        break


