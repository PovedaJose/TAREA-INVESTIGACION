class Calculadora:
    def __init__(self, numero1, numero2):
        self.num1 = numero1
        self.num2 = numero2

    def suma(self):
        print('{} + {} = {}'.format(self.num1, self.num2, self.num1+self.num2))

    def resta(self):
        print('{} - {} = {}'.format(self.num1, self.num2, self.num1 - self.num2))

    def multiplicacion(self):
        print('{} * {} = {}'.format(self.num1, self.num2, self.num1 * self.num2))

    def division(self):
        if self.num2 == 0:
            print('No se puede dividir entre cero')
        else:
            print('{} / {} = {}'.format(self.num1, self.num2, self.num1 / self.num2))


class calEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)

    def multiplicacion(self):     #polimorfismo
        mult = self.num1 * self.num2
        return mult

    def exponente(self):
        print('{} ** {} = {}'.format(self.num1, self.num2, self.num1 ** self.num2))

    def valor_absoluto(self,numero):
        if numero < 0:
            numero = numero*-1
        return numero


class calCientifica(Calculadora):
    PI = 3.1416

    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)

    def circunferencia(self, radio):
        perimetro = 2 * self.PI * radio
        print('El perimetro(circunferencia) es: {}'.format(perimetro))

    def area_circulo(self, radio):
        area = self.PI * (radio**2)
        print('Un circulo con radio {} tiene un area de: {}'.format(radio, area))

    def area_cuadrado(self, lado):
        print('Un cuadrado cuyo lado sea {} tiene un area de {}'.format(lado,lado**2))


