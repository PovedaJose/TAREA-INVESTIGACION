from Calculadora import calEstandar, calCientifica
from opeNumeros import Basico, Intermedio
from lista import Lista
from cadena import Cadena
import os


class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo = titulo
        self.opciones = opciones

    def  menu(self):
        print( self.titulo)
        for opcion in self.opciones:
            print(opcion)
        while True :
            try:
                opc = int(input('Elija opción [1...{}]: '.format(len(self.opciones))))
                return opc
            except ValueError :
                print('Ingrese un valor válido.')


#&    M E N Ú  -  P R I N C I P A L     
opc = ''
while opc != 5:
    os.system('cls')
    menu = Menu('||--MENU PRINCIPAL--||', ['1) Calculadora', '2) Operacion numeros', '3) Tratamiento de listas', '4) Operacion de cadenas', '5) Salir'])
    opc = menu.menu()

    #* Submenú Calculadora.
    if opc == 1:
        opc1 = ''
        while opc1 != 10 :
            os.system( 'cls' )
            menu1 = Menu('//--MENU CALCULADORA--//', ['1) Suma', '2) Resta', '3) Multiplicacion', '4) Division', '5) Exponente', '6) valor absoluto', '7) circunferencia', '8) area circulo','9) Area cuadrado', '10) Salir'])
            opc1 = menu1.menu()
            if opc1 != 10 and opc1 < 10:
                os.system('cls')
                # Validación de las variables de entrada
                if opc1 not in range(6,10):
                    while True:
                        try:
                            num1 = int(input('Ingrese 1° número: '))
                            num2 = int(input('Ingrese 2° número: '))
                            break
                        except ValueError :
                            print('Dato erroneo. Ingrese nuevamente')
                    calculo = calEstandar(num1,num2)
                
                if opc1 in range(7, 9):
                    while True:
                        try:
                            radio = int(input('Ingrese radio:'))
                            break
                        except ValueError:
                            print('Dato erroneo. Ingrese nuevamente')
                    calculo = calCientifica(0, 0)
                # M E T O D O S
                if opc1 == 1:
                    print('<< Suma de 2 números. >>')
                    calculo.suma()
                    print(input('Toque ENTER para continuar ...'))

                elif opc1 == 2:
                    print('<< Resta de 2 números. >>')
                    calculo.resta()
                    print(input('Toque ENTER para continuar ...'))

                elif opc1 == 3:
                    print('<<Multiplicación de 2 números.>>')
                    print('{} * {} = {}' . format( num1, num2, calculo.multiplicacion()))
                    print(input('Toque ENTER para continuar ...'))

                elif opc1 == 4:
                    print ('<< División de 2 números. >>')
                    calculo.division()
                    print(input('Toque ENTER para continuar ...'))

                elif opc1 == 5:
                    print('<<Cálculo del exponente.>>')
                    calculo.exponente()
                    print(input('Toque ENTER para continuar ...'))

                elif opc1 == 6:
                    print('<< Valor absoluto. >>')
                    while True:
                        try:
                            numero = int(input('Ingrese número :'))
                            break
                        except ValueError:
                            print('Dato erroneo. Ingrese nuevamente')
                    calculo = calEstandar(0, 0)
                    print('El valor absoluto del numero {} es: {}'.format(numero, calculo.valor_absoluto(numero)))
                    print(input('Toque ENTER para continuar ...'))

                elif opc1 == 7:
                    print('<< Circunferencia. >>')
                    calculo.circunferencia(radio)
                    print(input('Toque ENTER para continuar ...'))

                elif  opc1 == 8:
                    print('<<Cálculo del area del circulo.>>')
                    calculo.area_circulo(radio)
                    print(input('Toque ENTER para continuar ...'))

                elif opc1 == 9:
                    print('<<Cálculo de area del cuadrado.>>')
                    while True:
                        try:
                            lado = int(input('Ingrese lado: '))
                            break 
                        except ValueError:
                            print('Dato erroneo. Ingrese nuevamente')
                    calculo = calCientifica(0, 0)
                    calculo.area_cuadrado(lado)
                    print(input('Toque ENTER para continuar ...'))

        print(input('Toque ENTER para volver a Menu Principal...'))

    #* Submenú Operaciones de números
    if opc == 2:
        opc2  =  ''
        while opc2 != 11:
            os.system('cls')
            menu2 = Menu('//--MENU OPERACION NUMEROS--//',['1) Presentar los numeros de 1 a n', '2) Sumar los numeros de 1 a n', '3) Multiplo de cualquier numero', '4) Presentar los divisores de un numero',
                        '5) Numero primo','6) Factorial de cualquier numero', '7) Fibonacci de una serie de n numeros', '8) Perfecto', '9) Primos gemelos', '10) Numeros amigos' , '11) Salir'])
            opc2  =  menu2.menu()

            #Validación de las variables de entrada.
            if opc2 != 11 and opc2 < 11:
                os.system('cls')
                if opc2 in range(3 ,7) or opc2 == 8:
                    while True:
                        try:
                            numero = int(input('Ingresa un número:'))
                            break
                        except ValueError:
                            print('Dato erroneo. Ingrese nuevamente')
                    operacion = Basico()

                if opc2 in range(1, 3) or opc2 == 7:
                    while True:
                        try:
                            n = int((input('Hasta que numero desea presentar: ')))
                            break
                        except ValueError:
                            print('Dato erroneo. Ingrese nuevamente')
                    operacion = Basico()
                    operacion1 = Intermedio()
                
                if opc2 in range(9,11):
                    while True:
                        try:
                            num1 = int((input('Ingrese primer número: ')))
                            num2 = int((input('Ingrese segundo número: ')))
                            break
                        except ValueError:
                            print('Dato erroneo. Ingrese nuevamente')
                    operacion1 = Intermedio()
                #  Metodos
                if opc2 == 1:
                    print('<<Presentación de los numeros del 1 al {}>>'.format(n))
                    operacion.numerosN(n)
                    print(input('Toque ENTER para continuar ...'))

                if opc2 == 2:
                    print('<<Suma de los numeros del 1 al {}>>'.format(n))
                    operacion1.numerosN(n)
                    print(input('Toque ENTER para continuar ...'))

                if opc2 == 3:
                    print('<< múltiplos del número {} >>'.format(numero))
                    operacion.multiplo(numero)
                    print(input('Toque ENTER para continuar ...'))

                if opc2 == 4:
                    print('<< Presentar divisores. >>')
                    print('Divisores del número {}:'.format(numero))
                    operacion.DivisoresNumero(numero)
                    print(input('Toque ENTER para continuar ...'))

                if opc2 == 5:
                    print('<< Número primo.>>')
                    operacion.primo(numero)
                    print(input('Toque ENTER para continuar ...'))

                if opc2 == 6:
                    print('<<Factorial.>>')
                    print(operacion1.factorial(numero))
                    print(input('Toque ENTER para continuar ...'))

                if opc2 == 7:
                    print('<< Fibonacci. >>')
                    operacion1.fibonacci(n)
                    print(input('Toque ENTER para continuar ...'))

                if opc2 == 8:
                    print('<<Número Perfecto.>>')
                    operacion.perfecto(numero)
                    print(input('Toque ENTER para continuar ...'))

                if opc2 == 9:
                    print('<<Números primos gemelos entre {} y {}>>'.format(num1,num2))
                    operacion1.primosGemelos(num1,num2)
                    print(input('Toque ENTER para continuar ...'))

                if opc2 == 10:
                    print('<<Numeros Amigos>>')
                    operacion1.amigos(num1,num2)
                    print(input('Toque ENTER para continuar ...'))

        print(input('Toque ENTER para volver a Menu Principal...'))


    #* Submenú Tratamiento de Listas
    if opc==3:
        opc3= " "
        os.system("cls")

        lista = []
        print("Cree una lista")
        while True:
            try:
                n = int(input("Cuántos números desea agregar: "))
                break
            except ValueError:
                print(' Ingrese valor válido')
        for i in range(n):
            dato = input("Ingrese el valor {}: ".format(i+1))
            lista.append(dato)
        c = Lista(lista)

        while opc3 != 11:
            os.system('cls')
            menu3 = Menu("//--Menu Tratamiento de Listas--//", ["1) Presentar Lista","2) Buscar valor",
                "3) Retornar los factoriales", "4) Retornar números primos", "5) Recorrer una lista de diccionario", "6) Insertar dado la posición",
                "7) Eliminar ocurrencias", "8) Retornar la eliminación de una lista", "9) Tupla en una lista", "10) Clientes", "11) Salir"])
            opc3 = menu3.menu()

            if opc3 != 11 and opc3 < 11:
                os.system('cls')
                if opc3 in range(3,5):
                    lista = []
                    print("Cree una lista")
                    while True:
                        try:
                            n = int(input("Cuántos números desea agregar: "))
                            break
                        except ValueError:
                            print(' Ingrese valor válido')
                    for i in range(n):
                        dato = int(input("Ingrese el valor {}: ".format(i+1)))
                        lista.append(dato)
            
                if opc3==1:
                    os.system("cls")
                    print("Presentación de la lista")
                    print(c.presentarLista())
                    input("Presione una tecla para continuar...")

                if opc3==2:
                    os.system("cls")
                    print("Buscar valor")
                    print(c.presentarLista())
                    valor = input("Ingrese un valor que quiere buscar : ")
                    print(c.buscarLista(valor))
                    input("Presione una tecla para continuar...")

                if opc3==3:
                    os.system("cls")
                    factorial = Lista(lista)
                    print(factorial.listaFactorial())
                    input("Presione una tecla para continuar...")

                if opc3==4:
                    os.system("cls")
                    print("Lista Primo")
                    primo = Lista(lista)
                    print(primo.listaPrimo())
                    input("Presione una tecla para continuar...")

                if opc3==5:
                    os.system("cls")
                    print("Lista Notas Diccionario")
                    listaNotasDiccionario= {}
                    print(c.listaNotas(listaNotasDiccionario))
                    input("Presione una tecla para continuar...")

                if opc3==6: 
                    os.system("cls")
                    print(c.lista)
                    while True:
                        try:
                            posicion= int(input("Ingrese la posicion: "))
                            valor= int(input("Ingrese el valor que quiere ingresar: "))
                            break
                        except ValueError:
                            print('Dato erroneo. Ingrese nuevamente')
                    c = Lista(lista)
                    print(c.insertarLista(posicion,valor))
                    input("Presione una tecla para continuar...")

                if opc3==7:
                    os.system("cls")
                    print(c.presentarLista())
                    valor= input("Ingrese el valor a eliminar: ")
                    print(c.eliminarLista(valor))
                    input("Presione una tecla para continuar...")

                if opc3==8:
                    os.system("cls")
                    print("Retornar cualquier valor de una lista eliminándolo ")
                    print(c.presentarLista())
                    posicion= int(input("Ingrese la posicion que quiere eliminar: "))
                    print(c.retornaValorLista(posicion))
                    input("Presione una tecla para continuar...")

                if opc3==9: 
                    os.system("cls")
                    print("Copiar cada elemento de una tupla en una lista")
                    tupla=()
                    print(c.copiarTuplaLista(tupla))
                    input("Presione una tecla para continuar...")

                if opc3==10:
                    os.system("cls")
                    print("Dar el vuelto a varios clientes")
                    listaClientesDiccionario= {}
                    print(c.vueltoLista(listaClientesDiccionario))
                    input("Presione una tecla para continuar...")            
    
        print(input('Toque ENTER para volver a Menu Principal...')) 


    #* Submenú Tratamiento de Listas
    if opc == 4:
        opc4 = ''
        cadena = input("Ingrese una cadena: ")
        cad= Cadena(cadena)
        while opc4 != 10:
            os.system('cls')
            menu4 = Menu('//--OPERACIONES DE CADENAS--//', ['1) Recorrer y presentar los datos de una cadena', '2) Buscar un carácter en una cadena', '3) Retornar una lista con la posiciones dado un carácter de la cadena', '4) Retornar una lista con todas las palabras de una cadena',
                '5) Retornar una cadena a partir de una lista', '6) Insertar un dato en una cadena dada lo Posición', '7) Eliminar todas las ocurrencias en una cadena', '8) Retornar cualquier valor de una cadena eliminándolo ',
                '9) Concatenar cadenas', '10) Salir'])
            opc4 = menu4.menu ()

            if opc4==1:
                os.system("cls")
                print("Presentación de la cadena")
                cad.recorrerCadena()
                input("Presione una tecla para continuar...")
            if opc4==2:
                os.system("cls")
                print("Buscar caracter en una cadena")
                print(cad.cadena)
                buscado = input("Digame el caracter buscar: ")
                print(cad.buscarCaracter(buscado))
                input("Presione una tecla para continuar...")
            if opc4==3:
                os.system("cls")
                print("Retornar una lista con la posiciones dado un carácter de la cadena")
                print(cad.cadena)
                caracter= input("Ingrese un caracter que quiere buscar: ")
                print(cad.listaPosiciones(caracter))
                input("Presione una tecla para continuar...")
            if opc4==4:
                os.system("cls")
                print("Retornar una lista con todas las palabras de una cadena")
                print(cad.cadena)
                print(cad.listaPalabras())
                input("Presione una tecla para continuar...")
            if opc4==5:
                os.system("cls")
                print("Retornar una cadena a partir de una lista")
                print(cad.cadenaLista())
                input("Presione una tecla para continuar...")
            if opc4==6:
                os.system("cls")
                print("Insertar un dato a la cadena dada la posición")
                print(cad.cadena)
                posicion= int(input("Ingrese la posicion a insertar: "))
                buscado= input("Ingrese un dato a la cadena: ")
                print(cad.insertarDato(buscado,posicion))
                input("Presione una tecla para continuar...")
            if opc4==7:
                os.system("cls")
                print("Eliminar ocurrencia de una cadena")
                print(cad.cadena)
                buscado= input("Ingrese un dato a la elimanar u ocurrencia: ")
                print(cad.eliminarOcurrencias(buscado))
                input("Presione una tecla para continuar...")
            if opc4==8:
                os.system("cls")
                print("Retornar cualquier valor de una cadena eliminándolo ")
                print(cad.cadena)
                posicion= int(input("Ingrese la posicion que quiere eliminar: "))
                print(cad.retornaValor(posicion))
                input("Presione una tecla para continuar...")
            if opc4==9:
                os.system("cls")
                print("Concatenar cadenas")
                print(cad.cadena)
                dato= input("Ingrese un dato que quiera agregar a la cadena: ")
                print(cad.concatenarCadena(dato))
                input("Presione una tecla para continuar...")
        print(input('Toque ENTER para volver a Menu Principal...'))
    
    if opc == 5:
        os.system('cls')
        print('-------------------------------')
        print('  Gracias por su visita...!!')
        print('-------------------------------')
        
