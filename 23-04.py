

# c1="aqua"
# c2="koku"
# cv1=0
# cv2=0

# cantV=int(input("cuantos votantes son? "))

# for i in range(cantV):
#     print("por quien votara 1.- ", (c1), " 2.- ", (c2))
#     voto=int(input())
#     if voto==1:
#         cv1=cv1+1
#     else:
#         cv2=cv2+1

# print("la cantidad de  votos de ", (c1), " es ", (cv2))
# print("la cantidad de  votos de ", (c2), " es ", (cv1))
# if cv1>cv2:
#     print(f"gano ", (c1))
# elif cv1<cv2:
#     print(f"gano ", (c2))
# else:
#     print("es un empate")






# frase=input("ingrese una frase", )

# c=0
# v=0
# for i in frase:
#     print(i)
#     if i.lower() in "aeiou":
#         v=v+1
#     elif i.lower() =="":
#         cons=cons+1
#     else:
#         c=c+1


# print("la cantidad de vocales es ", v)
# print("la cantidad de caracteres es ", c)






# cant=int(input("ingrese la cantidad de numeros "))

# for i in range(cant):

#     num=int(input("ingrese un numero :"))

#     if num %2==0:

#         print("el numero es par")

#     else:

#         print("el numero es impar")







# num=int(input("ingrese un numero "))

# for i in range(num):

#     if (i) %2==0:

#         print("el numero ", (i) ," es par")

#     else:

#         print("el numero ", (i) ," es impar")
    

cant=int(input("cuantos productos llevaras? "))

total=0

for i in range(cant):
    print('''
          
          que productos llevara?

          1... blazepam $9000
          2... metamotazona $19500
          3... oblea china $1000

                  ''')
    

    op=int(input())
    if op==1:
        print("usted lleva blazepam")
        total=total+9000
    elif op==2:
        print("usted compro metamotazona")
        total=total+19500
    elif op==3:
        print("compro oblea china")
        total=total+1000
    else:
        print("eliga una opción valida")


print("el costo total fue de ", (total))



