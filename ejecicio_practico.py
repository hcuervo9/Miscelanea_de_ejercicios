import math
from os import system as sy
import sys
from time import sleep



brkCascada=False
while True:
    if brkCascada == True:
        break
    print("1. Operadores")
    print("2. Condicionales")
    print("3. Ciclos")
    print("99. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        while True:
            if brkCascada==True:
                break
            sy("cls")
            print("1. Calcular el área de un triángulo.")
            print("2. Ingresar dos números por teclado y sumarlos.")
            print("3. Ingresar un número y visualizar el número elevado al cuadrado.")
            print("4. Convierta de euros a dólares.")
            print("5. Calcular el área y el perímetro de un cuadrado.")
            print("6. Determine el área y el volúmen de un cilindro.")
            print("7. Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área (pi*r)^2 del círculo inscrito")
            print("8. Calcular el promedio de tres (3) números")
            print("99. Regresar")
            opcion_menu1 = input("Seleccione una opcion: ")
            if opcion_menu1 == "1":
                sy("cls")
                base = int(input('Ingresar la base del triangulo: '))
                altura = int(input('Ingresar la altura del triangulo: '))
                area = (base * altura) / 2
                print('EL AREA DEL TRIANGULO ES: ', area, 'cm²')
                sleep(4) 
            elif opcion_menu1 == "2":
                sy("cls")
                numero1 = int(input('Ingrese el primer numero: '))
                numero2 = int(input('Ingrese el segundo numero: '))
                suma = numero1 + numero2
                print(f'LA SUMA DE LOS DOS NUMEROS ES: {suma}')
                sleep(4)
            elif opcion_menu1 == "3":
                sy("cls")
                numero = int(input('Ingrese un numero: '))
                cuadrado = numero ** 2
                print(f'El cuadrado del numero es: {cuadrado}')
                sleep(4)
            elif opcion_menu1 == "4":
                sy("cls")
                euro = float(input('Digite el numero de euros a convertir: '))
                dollar = 1.096
                eurusd = euro * dollar
                print(f'El numero de dollares que tiene es: {eurusd}')
                sleep(4)
            elif opcion_menu1 == "5":
                
                sy("cls")
                lado = int(input('Ingrese el primer lado: '))
                perimetro = lado * 4
                area = lado * lado
                print(f'El area del cuadrado es: {area}')
                print(f'El perimetro del cuadrado es: {perimetro}')
                sleep(4)

            elif opcion_menu1 == "6":
                sy("cls")
                radio = int(input('Ingrese el valor del radio: '))
                altura = int(input('Ingrese el valor de la altura: '))
                area = 2 * 3.1416 * radio * (radio + altura)
                volumen = 3.1416 * (radio **2) * altura

                print(f'El area del cilindro es: {area}')
                print(f'El volumen del cilindro es: ´{volumen}')
                sleep(4)
            elif opcion_menu1 == "7":
                sy("cls")
                radio = float(input('Ingrese el radio: '))
                area = math.pi * radio ** 2
                longitud = 2 * math.pi * radio
                print(f'El area es: {area:.2f}')
                print(f'la longitud de la circunferencia es: {longitud:.2f}')
                sleep(4)    
            elif opcion_menu1 == "8":
                sy("cls")
                numero1 = int(input('Ingrese el primer numero: '))
                numero2 = int(input('Ingrese el segundo numero: '))
                numero3 = int(input('Ingrese el tercer numero: '))

                promedio = numero1 + numero2 + numero3
                print(f'El promedio de los tres numeros es: {promedio}')
                sleep(4)
            elif opcion_menu1 == "99":
                sy("cls")
                break
    elif opcion == "2":
        while True:
            if brkCascada==True:
                break
            sy("cls")
            print("1. Determinar si un número es positivo o negativo.")
            print("2. Algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor.")
            print("3. Ingrese tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos.")
            print("4. Dados dos números A y B, sumarlos si A es menor que B o sino restarlos.")
            print("5. Dados dos números A y B encontrar el cociente entre A y B.")
            print("6. Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.")
            print("7. Determine si un año es bisiesto o no.")
            print("99. Regresar")
            opcion_menu1 = input("Seleccione una opcion: ")

            if opcion_menu1 == "1":
                sy("cls")
                numero = int(input('Ingrese un numero: '))
                if (numero>0):
                    print('El numero ingresado es positivo')
                if (numero<0):
                    print('El numero ingresado es negativo')
                sleep(4)
            elif opcion_menu1 == "2":
                sy("cls")
                print('Debe ingresar dos numeros')
                numero1 = int(input('Ingrese el primer numero: '))
                numero2 = int(input('Ingrese el segundo numero: '))
                if numero1 == numero2:
                    print('Los dos numeros son iguales: ')
                elif numero1 > numero2:
                    print(f'El numero {numero1} es mayor que {numero2}')
                else:
                    print(f'El numero {numero2} es mayor que {numero1}')
                sleep(4)
            elif opcion_menu1 == "3":
                sy("cls")
                n1 = int(input('Ingrese el primer numero: '))
                n2 = int(input('Ingrese el segundo numero: '))
                n3 = int(input('Ingrese el tercer numero: '))

                if n2 < n1 > n3 :
                    print('El numero mayor es el primer numero : ',n1)
                elif n1 < n2 > n3 :
                    print('El numero mayor es el segundo numero : ',n2)
                elif n1 < n3 > n2:
                    print('El numero mayor es el tercer numero : ',n3)
                sleep(4)
            elif opcion_menu1 == "4":
                sy("cls")
                n1 = int(input('Ingrese el primer numero: '))
                n2 = int(input('Ingrese el segundo numero: '))

                suma = n1+n2
                resta = n1-n2
                
                if n1 < n2 :
                    print(f'La suma de los dos numeros es: {suma}')
                elif n1 > n2 :
                    print(f'la resta de los dos numeros es: {resta}')
                sleep(4)
            elif opcion_menu1 == "5":
                sy("cls")
                n1 = float(input('Ingrese el primer numero: '))
                n2 = float(input('Ingrese el segundo numero: '))

                if n2 == 0:
                    print('¡¡¡¡¡La division no es posible ¡¡¡¡¡¡ ')

                else:
                    print(n1/n2)
                sleep(4)
            elif opcion_menu1 == "6":
                sy("cls")
                n1 = int(input('Ingrese el primer numero: '))
                n2 = int(input('Ingrese el segundo numero: '))

                suma = n1+n2
                multiplicar = n1*n2

                if n1 < 0:
                    print(f'La suma de los dos numeros es: {suma}')
                elif n2 < 0:
                    print(f'La suma de los dos numeros es: {suma}')

                else:
                    print(f'La multiplicacion de los dos numeros es: {multiplicar}')
                sleep(4)
            elif opcion_menu1 == "7":
                sy("cls")
                anio = int(input('Ingrese el año: '))

                if anio % 4 == 0:
                    if anio % 100 !=0 or anio % 400 ==0:
                        print('El año es bisiesto')
                    else:
                        print('El año no es bisiesto')
                else:
                    print('El año no es bisiesto')
                sleep(4)
            elif opcion_menu1 == "99":
                sy("cls")
                break
    elif opcion == "3":
        while True:
            if brkCascada==True:
                break
            sy("cls")
            print("1. Imprimir todos los múltiplos de 3 que hay entre 1 y 100.")
            print("2. Imprimir los números impares entre 0 y 100.")
            print("3. Imprimir los números pares del 1 al 100.")
            print("4. Imprimir los cuadrados de los números del 1 al 30.")
            print("5. Sumar los cuadrados de los cien primeros números naturales.")
            print("6. Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente.")
            print("7. Sumar todos los números que se digitan por teclado mientras no sea cero.")
            print("99. Regrsar")
            opcion_menu1 = input("Seleccione una opcion: ")

            if opcion_menu1 == "1":
                sy("cls")
                for i in range (1,101):
                    if i % 3 == 0:
                        print(i)
                sleep(4)
            elif opcion_menu1 == "2":
                sy("cls")
                for i in range (1,101):
                    if i % 2:
                        print(i)
                sleep(4)
            elif opcion_menu1 == "3":
                sy("cls")                
                for i in range (1,101):
                    if i % 2 == 0:
                        print(i)
                sleep(4)
            elif opcion_menu1 == "4":
                sy("cls")
                for i in range (1,31):
                    print(i**2)
                sleep(4)
            elif opcion_menu1 == "5":
                sy("cls")
                suma = 0
                for i in range (1,101):
                    cuadrado = (i * i)
                    suma = cuadrado + suma
                print(suma)
                sleep(4)
            elif opcion_menu1 == "6":
                sy("cls")
                n1 = int(input("Ingrese un numero: "))
                n2 = int(input("Ingrese un mumero mayor que el primer numero: "))

                if n1 < n2:
                    for i in range (n1, n2):
                        print (i)
                sleep(4)
            elif opcion_menu1 == "7":
                sy("cls")
                suma  = 0
                while True:
                    num = input("Ingrese un número o presione x para salir: ")
                    if num == "x":
                        break 
                    else:
                        suma = suma + int(num)
                if suma > 0:
                    print(f"La suma es:  {suma}")
                else:
                    print("No fue posible realizar la suma")
                sleep(4)
            elif opcion_menu1 == "99":
                sy("cls")
                break
    elif opcion == "99":
        break
    else:
        print("Error")