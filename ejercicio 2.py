##Ejercicio 2
import math
opcion= input("""seleccione la operacion que quiere realizar:
        1. suma
        2. resta
        3. multiplicacion
        4. division
        5. raiz cuadrada
        6. potencia
        7. porcentaje
        """)
if (opcion=="1" or opcion == "suma"):
    num1= float(input("ingrese el primer número"))
    num2= float(input("ingrese el segundo número"))
    resultado=num1+num2
    print("la suma de los dos números es igual a ",resultado)

elif(opcion=="2" or opcion=="resta"):
    num1= float(input("ingrese el primer número"))
    num2= float(input("ingrese el segundo número"))
    resultado=num1-num2
    print("la resta de los dos números es igual a ",resultado)

elif(opcion=="3" or opcion=="multiplicacion"):
    num1= float(input("ingrese el primer número"))
    num2= float(input("ingrese el segundo número"))
    resultado=num1*num2
    print("la multiplicación de los dos números es igual a ",resultado)

elif(opcion=="4" or opcion=="division"):
    num1= float(input("ingrese el primer número"))
    num2= float(input("ingrese el segundo número"))
    if (num2>0 or num2<0):
        resultado=num1/num2
        print("la division de los dos números es igual a ",resultado)
    else:
        print("INCORRECTO. El denominador es cero")

elif(opcion=="5" or opcion=="raiz cuadrada"):
    num1= float(input("ingrese el primer número"))
    if (num1>=0):
        resultado=math.sqrt(num1)
        print("la raíz cuadrada del número es igual a ",resultado)
    else:
        print("Una raíz cuadrada siempre debe ser positiva")

elif(opcion=="6" or opcion=="potencia"):
    num1= float(input("ingrese la base"))
    num2= float(input("ingrese la potencia"))
    resultado=num1**num2
    print(resultado)

elif(opcion=="7" or opcion=="porcentaje"):
    num1= float(input("ingrese el primer número"))
    num2= float(input("ingrese el segundo número"))
    resultado=(num1*num2)/100
    print(resultado)
else:
    print("OPCION INCORRECTA")

