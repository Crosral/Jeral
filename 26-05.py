# deuda=100000

# print("su deuda es de 100,000 pesos, debe pagarlo, en su tarjeta contiene 250,000 pesos")

# pag=int(input("ingrese el dinero para pagar su deuda"))

# if pag<=99999:
#     print("pagaste menos de lo sugerido")
# elif pag>=100000:
#     total=dinero-pag
#     print(f"perfecto, tu saldo ahora es de {total}")
# else:
#     print("pero escoge una opción correcta")




# [while True:
#     while True:
#             try:
#                 op=int(input('''
#                             1.-pago
#                             2.-compra
#                             3.-salir
#                     '''))
#                 break
#             except Exception:
#                  print("solo se admiten numeros enteros")
#             match op:
#                 case 1:
#                     print("la dedua actual es" (deuda))
#                     while True:
#                          try:
#                               pago=int(input("ingrese el monto a pagar: "))
#                               break
#                          except Exception:
#                               print("solo se admiten numeros enteros")
#                     if pago>0 and pago<=deuda:
#                          deuda=deuda-pago
#                     else:
#                          print(f"el pago debe ser mayor a cero y no debe exceder {deuda}")
#                 case 2:
#                     print("comprando")
#                     monto=int("ingrese el monto de la compra")
#                     deuda+=monto
#                     print(f"la deuda actual es {deuda}")
#                 case 3:
#                     print("saliendo...")
#                 case _:
#                     print("opcion invalida")

                                                          



# for i in range(op=="si"):
    
#     print('''
#         1.- pan $1200
#         2.- frutas $750
#         3.- carne 2500$
#         4.- ropa 26000$
#         5.- muebles 35000$
#         ''')
#     op2=int(input())
#     if op2==1:
#         total=total-1200
#         print("compro pan") 
#     elif op2==2:
#         total=total-750
#         print("compraste frutas")
#     elif op2==3:
#         total=total-2500
#         print("compraste carne")
#     elif op2==4:
#         total=total-26000
#         print("compraste ropa")
#     elif op2==5:
#         total=total-35000
#         print("compraste muebles")
#     else:
#         print("escoge algo valido")

# full=0
# standard=0
# basico=0

# while True:
#     print('''
#           1.-cursar pago del lavado
#           2.-ver ventas diarias
#           3.-salir
#         ''')
#     op=int(input())
#     while op==1:
#             while True:
#                 try:
#                     print(f'''
#                     1.- full (15000)
#                     2.- standard (10000)
#                     3.- basico (7000)
#                     4.- volver
#                     ''')
        
#     while op==2:
#         print(f'''
#         1.- full {full}
#         2.- standard {standard}
#         3.- basico {basico}
#         4.- volver
#             ''')


            #           1.- full {full}
            #   2.- standard {standard}
            #   3.- basico {basico}
            #   4.- volver


# print("inicie sesion usuario")

# cont=int(input("ingrese su contraseña: "))

# if cont==1234:
#     print


usuario101=None
usuario102=None
usuario103=None
contraseña1=None
contraseña2=None
contraseña3=None



print("cree un usuario antes de iniciar sesión")

while True:
    op=int(input('''
                 Seleccione una opción
                 1.- iniciar secion
                 2.- registrar usuario 
                 3.- salir
        '''))
    
    match op:
        case 1:
            if usuario101==None and usuario102==None and usuario103==None:
                print("no hay usuarios registrados")
            else :
                print("ingrese su usuario")
                user=input("")
                contras=input("ingrese su contraseña: ")
                if user<=usuario101 and contras==contraseña1:
                    if contras==contraseña1:
                        print('''
                              1.- realizar llamada
                              2.- enviar correo electronico
                              3.- cerrar sesión
                              
                            ''')



            print(f'''inicie sesion con una de las 3 cuentas
                  1.-{usuario101}
                  2.-{usuario102}
                  3.-{usuario103}
                    ''')
            op2=int(input())

            if op2==1:

                cont=input("ingrese su contraseña")

                if cont==contraseña1:

                    print("inicio sesión correctamente")

                else:
                    print("intente denuevo")

            elif op2==2:

                cont=input("ingrese su contraseña")

                if cont==contraseña2:

                    print("inicio sesión correctamente")

                else:

                    print("intente denuevo")

            elif op2==3:

                cont=input("ingrese su contraseña")

                if cont==contraseña3:

                    print("inicio sesión correctamente")

                else:

                    print("intente denuevo")

            else:
                print("ingrese una opción valida")

        case 2:
                pre=int(input("que usuario registrara  1, 2, 3,: "))
                print("ingrese su usuario")
                user=input("")
                contras=input("ingrese su contraseña: ")

                match pre:
                    case 1:
                    case 2:
                    case 3:
                    case _:
           

            
        case 3:
            print("saliendo...")
            break   
        case _:
            print("opcion invalida")
