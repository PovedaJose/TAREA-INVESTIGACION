from Calculadora import *
from opeNumeros import *
from lista import *
from cadena import *
import os
class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo= titulo
        self.opciones= opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        op= input("Elija opcion [1...{}]: ".format(len(self.opciones)))
        return op

op= " "
while op != 5:
    os.system("cls")
    menu= Menu("Menu Principal", ["1) Calculadora","2) Numeros", "3) Lista","4) Cadenas","5) Salir"])
    op= menu.menu()
    if op == "1":
        op1= " "
        while op != "10":
            os.system("cls")
            menu1= Menu("Menu Calculadora", ["1) Suma","2) Resta", "3) Multiplicacion" , "4) Division", 
            "5) Exponente" , "6) Valor Absoluto", "7) Circuferencia", "8) Área Circulo", "9) Area Cuadrado", "10) Salir"])
            op1= menu1.menu()
            process = CalEstandar(0,0)
            process1 = CalCientifica(0,0)
            if op1=="1":
                os.system("cls")
                print("Suma de dos numeros")
                n1= int(input("Ingrese un numero: "))
                n2= int(input("Ingrese el segundo numero: "))
                calEst= CalEstandar(n1,n2)
                suma= calEst.suma()
                print(suma)
                input("Presione una tecla para continuar...")
            if op1=="2":
                os.system("cls")
                print("Resta de dos numeros")
                n1= int(input("Ingrese un numero: "))
                n2= int(input("Ingrese el segundo numero: "))
                calEst= CalEstandar(n1,n2)
                resta= calEst.resta()
                print(resta)
                input("Presione una tecla para continuar...")
            if op1=="3":
                os.system("cls")
                print("Multiplicación de dos numeros")
                n1= int(input("Ingrese un numero: "))
                n2= int(input("Ingrese el segundo numero: "))
                calEst= CalEstandar(n1,n2)
                mul= calEst.multiplicacion()
                print(mul)
                input("Presione una tecla para continuar...")
            if op1=="4":
                os.system("cls")
                print("División de dos numeros")
                n1= int(input("Ingrese un numero: "))
                n2= int(input("Ingrese el segundo numero: "))
                calEst= CalEstandar(n1,n2)
                div= calEst.division()
                print(div)
                input("Presione una tecla para continuar...")
            if op1=="5":
                os.system("cls")
                print("Exponente de dos numeros")
                n1= int(input("Ingrese un numero: "))
                n2= int(input("Ingrese el segundo numero: "))
                calEst= CalEstandar(n1,n2)
                ex= calEst.exponente()
                print(ex)
                input("Presione una tecla para continuar...")
            if op1=="6":
                os.system("cls")
                print("Valor absoluto")
                n= int(input("Ingrese un numero: "))
                print(process.valorAbsoluto(n))
                input("Presione una tecla para continuar...")
            if op1=="7":
                os.system("cls")
                print("Circunferencia")
                radio= float(input("Ingrese un numero: "))
                process1.circunferencia(radio)
                input("Presione una tecla para continuar...")
            if op1=="8":
                os.system("cls")
                print("Área de un Circulo")
                radio= float(input("Ingrese el radio: "))
                process1.areaCirculo(radio)
                input("Presione una tecla para continuar...")
            if op1=="9":
                os.system("cls")
                print("Área de un Cuadrado")
                lado= int(input("Ingrese el lado: "))
                process1.areaCuadrado(radio)
                input("Presione una tecla para continuar...")
            if op1=="10":
                break

    elif op=="2":
        op2= " "
        while op != 11: 
            os.system("cls")
            menu2= Menu("Menu Numero", ["1) Presentar Números","2) Suma de Números", 
            "3) Múltiplo", "4) Presentar los divisores", "5) Número Primo", "6) Factorial", 
            "7) Fibonacci", "8) Perfecto", "9) Primos gemelos", "10) Números amigos", "11) Salir"])
            op2= menu2.menu()
            if op2=="1":
                os.system("cls")
                print("Presentar de los números de 1 a n")
                n= int(input("Ingrese un numero: "))
                pres = Basico()
                pres.numerosN1(n)
                input("Presione una tecla para continuar...")
            if op2=="2":
                os.system("cls")
                print("Suma de los números de 1 a n")
                n= int(input("Ingrese un numero: ")) 
                pres = Intermedio()
                print(pres.numerosN(n))
                input("Presione una tecla para continuar...")
            if op2=="3":
                os.system("cls")
                print("Número es multiplo de otro")
                num= int(input("Ingrese un numero: "))
                multiplo = int(input("Ingrese el multiplo a comrpobar: "))
                pres = Basico()
                print(pres.multiplo(num, multiplo))
                input("Presione una tecla para continuar...")
            if op2=="4":
                os.system("cls")
                print("Divisores de un numero")
                n1= int(input("Ingrese un numero: "))
                pres = Basico()
                print(pres.divisoresNumero(n1))
                input("Presione una tecla para continuar...")
            if op2=="5":
                os.system("cls")
                print("Numero Primo")
                num= int(input("Ingrese un numero: ")) 
                pres = Basico()
                res = pres.primo(num)
                if res: print("El numero {} es primo".format(num))
                else: print("El numero {} no es primo".format(num))
                input("Presione una tecla para continuar...")
            if op2=="6":
                os.system("cls")
                print("Factorial de cualquier numero ")
                num= int(input("Ingrese un numero: ")) 
                pres = Intermedio()
                print(pres.factorial(num))
                input("Presione una tecla para continuar...")
            if op2=="7":
                os.system("cls")
                print("Fibonacci de una serie de n números ")
                n= int(input("Ingrese un numero: ")) 
                pres = Intermedio()
                pres.fibonacci(n)
                input("Presione una tecla para continuar...")
            if op2=="8":
                os.system("cls")
                print("Numero Perfecto")
                num= int(input("Ingrese un numero: ")) 
                pres = Basico()
                print(pres.perfecto(num))
                input("Presione una tecla para continuar...")
            if op2=="9":
                os.system("cls")
                print("Primos gemelos")
                n1= int(input("Ingrese un numero: "))
                n2= int(input("Ingrese otro numero: "))
                pres = Intermedio()
                print(pres.primosGemelos(n1,n2))
                input("Presione una tecla para continuar...")
            if op2=="10":
                os.system("cls")
                print("Números amigos")
                n1= int(input("Ingrese un numero: "))
                n2= int(input("Ingrese otro numero: "))
                pres = Intermedio()
                print(pres.amigos(n1, n2))
                input("Presione una tecla para continuar...")
            if op2=="11":
                break  
    
    elif op=="3":
        op3= " "
        os.system("cls")
        lista = []
        print("Creando una lista")
        n = int(input("Cuantos numeros desea agregar: "))
        for i in range(n):
            dato = input("Ingrese el valor {}: ".format(i+1))
            lista.append(dato)

        while op != 11:
                menu3= Menu("Menu Listas", ["1) Presentar Lista","2) Buscar valor",
                "3) Retornar los factoriales", "4) Retornar números primos", "5) Recorrer una lista de diccionario", "6) Insertar dado la posición",
                "7) Eliminar ocurrencias", "8) Retornar la eliminación de una lista", "9) Tupla en una lista", "10) Clientes", "11) Salir"])
                op3= menu3.menu()
                c= Lista(lista)
                if op3=="1":
                    os.system("cls")
                    print("Presentación de la lista")
                    print(c.presentarLista())
                    input("Presione una tecla para continuar...")
                if op3=="2":
                    os.system("cls")
                    print("Buscar valor")
                    print(c.presentarLista())
                    valor = input("Ingrese un valor que quiere buscar : ")
                    print(c.buscarLista(valor))
                    input("Presione una tecla para continuar...")
                if op3=="3":
                    os.system("cls")
                    lista = []
                    print("Creando una lista")
                    n = int(input("Cuantos numeros desea agregar: "))
                    for i in range(n):
                        dato = int(input("Ingrese el dato {}: ".format(i + 1)))
                        lista.append(dato)
                    factorial = Lista(lista)
                    print(factorial.listaFactorial())
                    input("Presione una tecla para continuar...")
                if op3=="4":
                    os.system("cls")
                    print("Lista Primo")
                    lista = []
                    print("Creando una lista")
                    n = int(input("Cuantos numeros desea agregar: "))
                    for i in range(n):
                        dato = int(input("Ingrese el dato {}: ".format(i + 1)))
                        lista.append(dato)
                    primo = Lista(lista)
                    print(primo.listaPrimo())
                    input("Presione una tecla para continuar...")
                if op3=="5":
                    os.system("cls")
                    print("Lista Notas Diccionario")
                    listaNotasDiccionario= {}
                    print(c.listaNotas(listaNotasDiccionario))
                    input("Presione una tecla para continuar...")
                if op3=="6":
                    os.system("cls")
                    print(c.lista)
                    posicion= int(input("Ingrese la posicion: "))
                    valor= input("Ingrese el valor que quiere ingresar: ")
                    print(c.insertarLista(posicion,valor))
                    print(lista)
                    input("Presione una tecla para continuar...")
                if op3=="7":
                    os.system("cls")
                    print(c.presentarLista())
                    valor= input("Ingrese el valor a eliminar: ")
                    print(c.eliminarLista(valor))
                    input("Presione una tecla para continuar...")
                if op3=="8":
                    os.system("cls")
                    print("Retornar cualquier valor de una lista eliminándolo ")
                    print(c.presentarLista())
                    posicion= int(input("Ingrese la posicion que quiere eliminar: "))
                    print(c.retornaValorLista(posicion))
                    input("Presione una tecla para continuar...")
                if op3=="9":
                    os.system("cls")
                    print("Copiar cada elemento de una tupla en una lista")
                    tupla=()
                    print(c.copiarTuplaLista(tupla))
                    input("Presione una tecla para continuar...")
                if op3=="10":
                    os.system("cls")
                    print("Dar el vuelto a varios clientes")
                    listaClientesDiccionario= {}
                    print(c.vueltoLista(listaClientesDiccionario))
                    input("Presione una tecla para continuar...")
                if op3=="11":
                    break

    
    elif op=="4":
        op4= " "
        cadena = input("Ingrese una cadena: ")
        cad= Cadena(cadena)
        while op != "10": 
            os.system("cls")
            menu4= Menu("Menu Cadenas", ["1) Presentar Cadena","2) Buscar carácter", 
            "3) Retornar posición", "4) Retornar palabras", "5) Retornar una cadena", "6) Insertar dado la posición", 
            "7) Eliminar ocurrencias", "8) Retornar la eliminación de una cadena", "9) Concatenar", "10) Salir"])
            op4= menu4.menu()
            
            if op4=="1":
                os.system("cls")
                print("Presentación de la cadena")
                cad.recorrerCadena()
                input("Presione una tecla para continuar...")
            if op4=="2":
                os.system("cls")
                print("Buscar caracter en una cadena")
                print(cad.cadena)
                buscado = input("Digame el caracter buscar: ")
                print(cad.buscarCaracter(buscado))
                input("Presione una tecla para continuar...")
            if op4=="3":
                os.system("cls")
                print("Retornar una lista con la posiciones dado un carácter de la cadena")
                print(cad.cadena)
                caracter= input("Ingrese un caracter que quiere buscar: ")
                print(cad.listaPosiciones(caracter))
                input("Presione una tecla para continuar...")
            if op4=="4":
                os.system("cls")
                print("Retornar una lista con todas las palabras de una cadena")
                print(cad.cadena)
                print(cad.listaPalabras())
                input("Presione una tecla para continuar...")
            if op4=="5":
                os.system("cls")
                print("Retornar una cadena a partir de una lista")
                print(cad.cadenaLista())
                input("Presione una tecla para continuar...")
            if op4=="6":
                os.system("cls")
                print("Insertar un dato a la cadena dada la posición")
                print(cad.cadena)
                posicion= int(input("Ingrese la posicion a insertar: "))
                buscado= input("Ingrese un dato a la cadena: ")
                print(cad.insertarDato(buscado,posicion))
                input("Presione una tecla para continuar...")
            if op4=="7":
                os.system("cls")
                print("Eliminar ocurrencia de una cadena")
                print(cad.cadena)
                buscado= input("Ingrese un dato a la elimanar u ocurrencia: ")
                print(cad.eliminarOcurrencias(buscado))
                input("Presione una tecla para continuar...")
            if op4=="8":
                os.system("cls")
                print("Retornar cualquier valor de una cadena eliminándolo ")
                print(cad.cadena)
                posicion= int(input("Ingrese la posicion que quiere eliminar: "))
                print(cad.retornaValor(posicion))
                input("Presione una tecla para continuar...")
            if op4=="9":
                os.system("cls")
                print("Concatenar cadenas")
                print(cad.cadena)
                dato= input("Ingrese un dato que quiera agregar a la cadena: ")
                print(cad.concatenarCadena(dato))
                input("Presione una tecla para continuar...")
            if op4=="10":
                break


    elif op=="5":
        print("Gracias por tu visita")
        break
    
    else:
        print("Opción  no valida")           
        
os.system("cls")