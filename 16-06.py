list_prod=[""
    ["nombre": "zapato", "precio": 20000]
    ["nombre": "pelota", "precio": 24000]
]
while True:
    print('''   
          1.- agregar producto
          2.- mostrar productos
          3.- actualizar producto
          4.- salir
        ''')
    
    op=int(input())
    match op:
            case 1:
                nom=input("ingrese el nombre del producto: ")
                pre=int(input("ingrese el precio: "))
                list_prod.insert(0, {"nmbre":nom, "precio":pre})
            case 2:
                for p in list_prod:
                    print(p)
            case 3:
                for i in range(len(list_prod)):
                    print(i+1 ,",-", list_prod[i])
                opc=int(input("selecione el producto a actualizar"))
                print(list_prod[opc-1])
                nn=input("ingrese un nuevo nombre ")
                np 
                list_prod.pop(opc-1)
            case 4:
                print("saliendo...")
                break
            case _:
              print("pero coloca algo valido no manches")
