
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





# tarjeta=20000

# b5k=5
# b10k=5
# b20k=5
# b2k=5
# b1k=10



# print("retire dinero del cajero,")

# while True:
#     print('''caunto dinero quiere retirar?
          
#         1.- 5000
#         2.- 10000
#         3,. 20000
#         4.- 50000
#         5.- otro
#           ''')
    
#     op=int(input("selecione una opción "))

#     if op==1:
#         print("usted retiro 5000")
#         tarjeta=tarjeta-5000
        
#     elif op==2:
#         print("opcion 2")
#     elif op==3:
#         print("salir")
#         break





# intentos=3

# while intentos>0:

#     color=input("ingrese un color ") 

#     if color.lower()!="negro":

#         print("el color no es el requerido")
#         intentos-=1

#     else:

#         print("este es el color requerido")

#         break

# print("gracias por dar el color requerido")



# arancel=200000

# descuento=0


# print('''
#       1.- la florida 20%
#       2.- la pintana 30%
#       3.- puente alto 25%
#       4.- san joaquin 15%
#       ''')

# comuna=int(input("escriba su comuna "))


# if comuna==1:
#     descuento=descuento+20
# elif comuna==2:
#     descuento=descuento+30
# elif comuna==3:
#     descuento=descuento+25
# elif comuna==4:
#     descuento=descuento+15
# else:
#     print("eliga una opcion valida")

# grupo=int(input("¿con cuantas vive en su hogar? "))

# if grupo==1:

#     descuento=descuento+2

# elif grupo>=2 and grupo<=4:

#     descuento=descuento+3

# elif grupo>=5:

#     descuento=descuento+4

# else:
#     print("numero invalido como el niño en silla de ruedas")

# print("el total del descuento es", descuento )
# descpesos=descuento/100*arancel
# apagar=arancel-descpesos
# print(f"el total a pagar es {apagar}")

total=0

print('''
      1.- zapatillas
      2.- poleras
      3.- pelotas
      
''')

cat=int(input())

if cat==1:
    print('''
          1.- zapatillas runing 2000
          2.- zapatillas futbolito 1500
          3.- zapatilla padel 2000
''')
    
op=int(input())
    
if op==1:
    total=total+2000+200
elif op==2:
    total=total+1500+200
elif op==3:
    total=total+60+200
else:
    print("eliga una opcion valida")


if cat==2:
    print('''
          1.- polera runing 2000
          2.- polera futbolito 1500
          3.- polera padel 3500
''')
    
op=int(input())
    
if op==1:
    total=total+2000+600
elif op==2:
    total=total+1500+600
elif op==3:
    total=total+3500+600
else:
    print("eliga una opcion valida")



if cat==3:
    print('''
          1.- pelota 2000
          2.- polera especial 1500
          3.- polera de buen diseño 2500
''')
    
op=int(input())
    
if op==1:
    total=total+2000+200
elif op==2:
    total=total+1500+200
elif op==3:
    total=total+2500+200
else:
    print("eliga una opcion valida")



