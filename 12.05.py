








def suma():
    n1=int(input("ingrese un numero "))
    n2=int(input("agrege otro numero "))
    print("la suma es", n1+n2)
def resta():
    n1=int(input("ingrese un numero "))
    n2=int(input("agrege otro numero "))
    print("la resta es", n1-n2)
def multi():
    n1=int(input("ingrese un numero "))
    n2=int(input("agrege otro numero "))
    print("la multiplicación es", n1*n2)
def division():
    n1=int(input("ingrese un numero "))
    n2=int(input("agrege otro numero "))
    try:
        resultado=n1/n2 
        print("la división es", resultado)
    except ZeroDivisionError:
        print("la división por cero no esta permitida")












def calcu():
    



    while True:
        op=int(input('''
             
             1.- suma
             2.- resta
             3.- multiplicación
             4.- division
             5.- salir
             
            '''))
        match op:
            case 1:
                print("suma")
                suma()
            case 2:
                print("resta")
                resta()
            case 3:
                print("multiplicación")
                multi()
            case 4:
                print("división")
                division()
            case 5:
                print("saliendo")
                break
            case _:
                print("opcion no valida")


calcu()



#realizar un programa que incluya match y llame a otras
# 3 funciones, estas funciones deben incluir
# if. if else, for, y/o while
#el programa debe ser recursivo
