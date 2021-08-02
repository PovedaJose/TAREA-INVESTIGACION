from opeNumeros import Intermedio

class Lista(Intermedio):
    def __init__(self, lista):
        self.lista = lista

    def  presentarLista(self):
        print(self.lista)

    def  buscarLista(self, valor):
        p = self.lista.count(valor)
        return"El valor {} se encuentra {} vez/veces en la lista." .format(valor, p)

    def listaFactorial(self):
        lis = []
        for i in self.lista:
            fact = super().factorial(i)
            lis.append(fact)
        return "La lista de los factoriales es: {}".format(lis)

    def listaPrimo(self):
        lis = []
        for i in self.lista:
            aux = super().primo(i)
            if aux: lis.append(i)
        return "La lista de los primos es: {}".format(lis)

    def listaNotas(self, listaNotasDiccionario):
        list = []
        while True:
            try:
                datos=int(input("Cuantos alumnos va a ingresar: "))
                break
            except ValueError:
                print('Ingrese valor válido')
        for alu in range(datos):
            aux = []
            alumno= input("Ingrese el nombre del alumno {}: ".format(alu))
            while True:
                try:
                    notas= int(input("¿Cuantas notas va a ingresar por el estudiante {}?: ".format(alumno)))
                    break
                except ValueError:
                    print('Ingrese valor válido')
            for nota in range(notas):
                no= round(float(input("Nota {}: ".format(nota))),2)
                aux.append(no)
            listaNotasDiccionario = {"Nombre": alumno, "Notas":aux}
            list.append(listaNotasDiccionario)
        return "La lista de los cliente son: {}".format(list)

    def insertarLista(self, valor, posicion):
        self.lista.insert(valor, posicion)
        return "La nueva lista es: {}".format(self.lista)

    def eliminarLista(self, valor):
        try: 
            while True:
                self.lista.remove(valor)
        except:
            pass
        return "La lista queda: {}".format(self.lista)

    def retornaValorLista(self, posicion):
        if posicion<len(self.lista):
            c= self.lista.pop(posicion)
            print("El valor eliminado es: {}".format(c.split()))
        else:
            print("La posicion {} no se encuentra en la lista".format(posicion))
        return "La nueva lista queda: {}".format(self.lista)

    def copiarTuplaLista(self, tupla):
        while True:
            try:
                n= int(input("Cuantos elementos quiere agregar: "))
                break
            except ValueError:
                print('Ingrese valor válido')
        for i in range(n):
            lis=input("Ingrese valor: ")
            self.lista.append(lis)
            tupla= tuple(self.lista)
            lista= list(tupla)
        print(tupla)
        return "Copiamos la tupla en una lista y quedó: {}".format(lista)
        
    def vueltoLista(self, listaClientesDiccionario):
        list = []
        datos=int(input("Cuantos clientes va a ingresar: "))
        for cup in range(datos):
            "nombre{}".format(cup)
            cliente= input("Ingrese el nombre del cliente: ")
            cupo= float(input("¿Cuánto es el vuelto del cliente {}?: ".format(cliente)))
            listaClientesDiccionario = {"Nombre":cliente,"Vuelto":cupo}
            list.append(listaClientesDiccionario)
        return "La lista de los cliente son: {}".format(list)




