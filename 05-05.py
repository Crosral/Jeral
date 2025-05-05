#calcular el puntaje de credito
#debe calcular que tanto credito tiene una persona
#en cierta entidad financiera, debera considerar
#cantidad de ingreso, nivel educacionaly nacionalidad
#cantidad de ingresos
#500.000 a 1.000.000 : 300.000
#1.000.000 a 1.500.000 : 650.000
#1.500.001 o mas : 1.000.000
#nivel educacional
#basico : x1, medio : x1.3, superopr x1.5
#nacionalidad
#chilena : +300.000, extranjero : +0



# op1=input('''¿cuanto dinero ganas?
          
#           1.- 500.000
#           2.- 1.000.000
#           3.- 1.500.000
          
#           ''')

# finc=0

# if op1==1:

#     finc+=500000

# elif op1==2:

#     finc+=1000000

# elif op1==3:
#     finc+=1500000

# else:
#     print("elije una opción valida")


# op2=input('''¿cual es su nacionalidad? 
      
#       1.-chilena
#       2.-extrajenra
      
#       ''')

# dine=0

# nac=""

# if op2==1:
#     nac="chilena"
#     dine=dine+300000
# elif op2==2:
#     nac="extranjera"
# else:
#     print("pero escoge algo valido no te hagas >:v")
    


# op3=input('''¿cual es su nivel educacional?
          
#           1.- basico
#           2.- media
#           3.- superior

#           ''')



# est2=0
# est=""
# if op3==1:

#     est="basico"
#     est2+=1
# elif op3==2:

    
#     est="media"
#     est2+=1.3

# elif op3==3:

#     est="superior"
#     est2+=1.5
# else:
#     print("deja de equivocarte")

# total=finc*est2
# total+=finc+dine
# print(f"usted es de nacionalidad {nac}") 

# print(f"sus estudios son de nivel {est} y sus ingresos totales son {total}")

# import random

# print("ungrese dos digitos")
# n1=int(input())
# n2=int(input())

# while n1>n2:
#     print("el numero 2 no puede ser menor que el numero 1")
#     n2=int(input("numero 2 "))

# num=random.randint(n1,n2)
# print("▄" num)




rg=int(input("¿cuantos ramos tienes?"))


for i in range(rg):
    nt=input("ingrese la cantidad de notas que tienes")

nf=rg

ntf=nf/nt

if ntf<4.5:
    print(f"reprobaste horrible con un {ntf}")
elif ntf>=4.6 or ntf<=5:
    print(f"te salvaste, tienes {ntf}")
elif ntf>=5.1 or ntf<=6:
    print(f"buena nota, tienes {ntf}")
elif ntf>=6.1 or ntf<=6.9:
    print(f"excelente, tienes {ntf}")
elif ntf>=7:
    print(f"nah, re capo, tienes {ntf}")
else:
    print("por alguna razon tienes esta cantidad extraña")
