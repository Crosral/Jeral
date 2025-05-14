# import random

# def azarn():
#     num=random.randint(1,18)
#     return num

# def arancel():
#     print

# def menu_tarea():
#     print



# while op!=3:
#     print('''
          
#           Seleccione un aopción
#           1.- numero al azar
#           2.- calcular arancel
#           3.- salir
          

#         ''')
    
#     op=int("input")
#     match op:
#         case 1:
#             azarn()
#         case 2:
#             arancel()
#         case 3:
#             break
#         case _:
#             print(



# nm=input("ingrese su nombre porfavor ")

# op=int(input('''
#           escoga que quiere comprar

#           1.- pan 
#           2.- frutas
#           3.- carne
#           4.- ¿terminar compras?
#         '''))
# total=0

# global total=int()

# def pan():
#         print('''

#         1.- hallulla 150%
#         2.- marraqueta 200$
#         3.- amasado 300$
#         4.- salir
#             ''')

#         cmp=int(input())
#         if cmp==1:

#             print("ha comprado una hallulla, se le cobro 150$")
#             total=total+150
#         elif cmp==2:

#             print("compro una marraqueta, se le sumo 200$")
#             total=total+200
#         elif cmp==3:

#              print("compor un amasado, se le cobro 300$")
#              total=total+300
#         elif cmp==4:
             
#              print("saliendo de la compra")
#              return
#         else:
             
#              print("usted escogio una opcion invalida")

# def fruta():
#     print('''

#            1.- platano
#            2.- naranja
#            3.- manzana
#            4.- salir
#         ''')
#     comp=int(input())

#     if comp==1:
#         print("compraste un platano, se cobro 165$")
#         total=total+165
#     elif comp==2:
#         print("compraste una naranja, se cobro 130")
#         total=total+130
#     elif comp==3:
#         print("compraste una manzana, se te cobro 175")
#         total=total+175
#     elif comp==4:
#         print("saliendo")
#         return
#     else:
#         print("no te hagas pendejo elige algo valido")    

# def carne():
#     print('''

#            1.- pollo
#            2.- cerdo
#            3.- vacuno
#            4.- salir
#         ''')
     
#     comp1=int(input())

#     if comp1==1:
#         print("compraste carne de pollo, se cobro 270$")
#         total=total+270
#     elif comp1==2:
#         print("compraste carne de cerdo, se cobro 350")
#         total=total+350
#     elif comp1==3:
#         print("compraste carne de vacuno, se te cobro 425")
#         total=total+425
#     elif comp1==4:
#         print("saliendo")
#         return
#     else:
#         print("no te hagas pendejo elige algo valido")

# def boleta():
#     rsp=input("esta seguro [diga si o no]")
#     if rsp=="si":
#         print(f"el total a pagar es {total}, gracias {nm} por su compra")
#         return
#     elif rsp=="no":
#         print("volviendo a las compras")
#         return
#     else:
#         print("no ses mamon escoge algo valido")


# match op:
#     case 1:
#         pan()
#     case 2:
#         fruta()
#     case 3:
#         carne()
#     case 4:
#         boleta()
#     case _:
#         print("escoge algo valido")
