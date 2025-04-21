

# num=int(input("ingrese el numero para multiplicarlo por 10 "))

# for i in range(10):
#     print( num, " x ", i+1, " = ", num*(i+1))


#genera las tablas del 1 al 10 de cada una

# num=int(input("ingrese el numero para multiplicarlo por 10 "))

# for j in range(10):
#     for i in range(10):
#         print( (j+1), " x ", i+1, " = ", (j+1)*(i+1))





#promedio de notas

# cant=int(input("cuantas notas son "))
# suma=0

# for i in range(cant):

#     print("ingrese una nota ", i+1)
#     nota=float(input())
#     suma=nota+suma


# prom=suma/cant
# print("el promedio es ", prom)







#cantidad de alumnos y luego la cantidad de notas 
#y mostrar el promedio de notat

# cantA=int(input("cantidad de alumnos "))


# for j in range(cantA):
#         cantN=int(input("cantidad de notas "))
#         suma=0

#         for i in range(cantN):
#             print("ingrese una nota ", i+1, " del alumno ", j+1, "(use valores decimales)")
#             nota=float(input())
#             suma=nota+suma


# prom=suma/cantN
# print("el promedio es ", prom)

# if prom>=4:
#       print("lo lograste causa")
# else:
#       print("reprobaste pendejo")
    






num=int(input())

if num % 2==0:
    print("el numero ", num ," es par")
else:
    print("el numero ", num , " es impar")