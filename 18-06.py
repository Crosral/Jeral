

# list_prod=[
#     {"nombre":"zapato", 
#      "precio":20000}
#     ,
#     {"nombre":"pelota", 
#      "precio":24000} 
# ]

# # list_prod[0]["nombre"]

# # num=[4,6,7,4,5,6,55]

# def mostrar_art(lista):
#       for i, p in enumerate(lista):
#          print(i, p, ".-", ["nombre"], "$", p["precio"])







# while True:
#     print('''   
#           1.- agregar producto
#           2.- mostrar productos
#           3.- actualizar producto
#           4.- 
#           5.-
#         ''')
    
#     op=int(input())
#     match op:
#             case 1:
#                 nom=input("ingrese el nombre del producto: ")
#                 pre=int(input("ingrese el precio: "))
#                 list_prod.insert(0, {"nmbre":nom, "precio":pre})
#             case 2:
#                     mostrar_art(list_prod)
#             case 3:
#                 for i in range(len(list_prod)):
#                     print(i+1 ,",-", list_prod[i])
#                 opc=int(input("selecione el producto a actualizar"))
#                 print(list_prod[opc-1])
#                 nn=input("ingrese un nuevo nombre ") 
#                 np=int(input("ingrese un nuevo precio"))
#                 list_prod[opc-1]["nombre"]==nn
#                 list_prod(opc-1)["precio"]==np
#                 print("articulo actualizado")
#             case 4:
#                 for n, p in enumerate(list_prod):
#                     pre(n+1, ".-", p["nombre"], "$", p["precio"])
#                     opc=int(input("seleccione el producto a borrar"))
#                     list_prod(opc-1)
#             case 5:
#                 print("saliendo...")
#                 break
#             case _:
#               print("pero coloca algo valido no manches")




personas={

    1:{"nombrs":" Diego Ruvera",
       "numeros=":[7361226,7326827],
       "estadocivil": "casado",
       "trabajando": True,
       "edad": 64},
    2:"dato2",
    3:"dato3",
}

while True:
    try:
        print('''  
              1.- ingresar persona
              2.- nostrar listado
              3.- actualizar persona
              4.- borrar persona
              5.- salir
              
            ''')
        op=int(input("selecione una opcion"))
        match op:
            case 1:
                nombre=input("ingrese el nombre")
                numero=int(input("ingrese el numero"))
                est=int(input("estado civil 1.- casado 2.- soletor"))
                if est==1:
                    estcivil="civil"
                else:
                    estcivil="soltero"
                edad=int(input("ingrese su edad"))
                nextkey=len(personas+1)
                personas[nextkey+1]={"nombre": nombre,
                                     "numeros": {numero},
                                     "estadp civil": estcivil, 
                                     "trabajando": True,
                                     "edad": edad }
                print("persona infresada con existe")
            case 2:
                for oersiba, val in personas.items():
                    print(personas, val)
            case 3:
                print()
            case 4:
                print()
            case 5:
                print()
            case _:
                print()
    except Exception as e:
        print("el error es ", e)


