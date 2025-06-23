# anio=1985

# if len(str(anio)) ==4:
#     print("tiene largo de 4")

def valida_pass(password):
    while True:
        password=input("ingrese su contraseña")

        cMayus=0
        cMinusculas=0
        cnumeros=0
        tine_gato=0
        l=0


        for l in password:
            if l.isupper():
                cMayus+=1
            if l.islower():
                cMinusculas+=1
            if l.isdigit():
                cnumeros+=1
        if cMayus<3:
            print("debe tener almenos 3 letras en mayusculas")
        elif cMinusculas<1:
            print("deve tener almenos 1 letra en minuscula")
        elif cnumeros<3:
            print("debe tener almenos 3 numeros")
        elif tine_gato<3:
            print("debe tener almenos un caracter  '#' ")
        else:
            print("contraseña creada")
            return True
        
valida_pass("SperMARio22#")

pp=False

while pp!=True:
    clave=input/"ingrese su contraseña"
    
    pp=valida_pass(clave)



prod=[
    1:{"nombre":"zelda tdtk"
       "precio": 80000
       "code": ZZ}
]
