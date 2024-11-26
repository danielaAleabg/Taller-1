lado1=float(input("ingrese la medida del primer lado del triangulo "))
lado2=float(input("ingrese la medida del segundo lado del triangulo "))
lado3=float(input("ingrese la medida del tercer lado del triangulo "))
perimetro=lado1+lado2+lado3
if (lado1==lado2==lado3):
    lado=lado1=lado2=lado3
    area=((3)**0.5/4)*(lado**2)
    print("el area del triangulo es ",area," y su perimetro es ",perimetro)
elif(lado1==lado2!=lado3 or lado1==lado3!=lado2 or lado3==lado2!=lado1):
    s=(lado1+lado2+lado3)/2
    area=(s*(s-lado1)*(s-lado2)*(s-lado3))**0.5
    print("el area del triangulo es ",area," y su perimetro es ",perimetro)
else:
    s=(lado1+lado2+lado3)/2
    area=(s*(s-lado1)*(s-lado2)*(s-lado3))**0.5
    print("el area del triangulo es ",area," y su perimetro es ",perimetro)
