notas=[]


while True:
    print('''   

          1.- ingresar notas
          2.- borrar nota
          3.- ver notas colocadas
          4.- promedio de notas
          5.- borrar toda las notas
          6.- salir
            ''')
    op=int(input())

    match op:
        case 1:
            nota=float(input("ingrese la nota del alumno: "))
            notas.append(nota)
        case 2:
            print(notas)
            elim=float(input("ingrese cual quiere eliminar: "))
            notas.remove(elim)
        case 3:
            print(notas)
        case 4:
            if len(notas) == 0:
                print("No hay notas para calcular el promedio.")
            else:
                suma=0
                for n in notas:
                    suma+=n
                promedio=suma/len(notas)
                print(f"El promedio de las notas es: {promedio}")
            print("la nota mayor es", max(notas))
            print("la nota minima es", min(notas))
        case 5:
            notas.clear()
        case 6:
            print("saliendo...")
            break
        case _:
            print("ya wey escogfe algo valido")

            
