
class Calculadora: 
    def __init__(self, num1, num2):
        self.numero1= num1
        self.numero2= num2
    
    def suma(self):
        return "El resultado de la suma es: {}+{}={}".format(self.numero1,self.numero2,self.numero1 + self.numero2)
    
    def resta(self):
        if self.numero1 > self.numero2 : 
            return "El resultado de la resta es: {}-{}={}" .format(self.numero1,self.numero2,self.numero1 - self.numero2)
        else: 
            return "El resultado de la resta es: {}-{}={}" .format(self.numero2,self.numero1,self.numero2 - self.numero1)

    def multiplicacion(self):
        multi= self.numero1 * self.numero2
        return "El resultado de la multiplicación es {}*{}={}".format(self.numero1,self.numero2,multi)
    
    def division(self):
        while True:
            if self.numero2 != 0:
                return "El resultado de la división es: {}/{}={}".format(self.numero1, self.numero2,self.numero1 / self.numero2)
            elif self.numero2 == 0:
                return "El valor no es correcto"

class CalEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1,numero2)

    
    def multiplicacion(self):
        multi= super().multiplicacion()
        return multi
    
    def exponente(self):
        exp = round((self.numero1 ** self.numero2), 2)
        return "El resultado de la exponenciación es: {}^{}={}" .format(self.numero1, self.numero2,exp)
    
    def valorAbsoluto(self, n):
        r= abs(n)
        return "El valor absoluto de {} es {}" .format(n, r)

class CalCientifica(Calculadora):
    PI= 3.1416
    
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
    
    def circunferencia(self, radio):
        circunferencia = 2 * radio * CalCientifica.PI
        print("La circunferencia del circulo de radio {} es de: {} mts.".format(radio, circunferencia))

    def areaCirculo(self, radio):
        area_circunferencia = CalCientifica.PI * (radio ** 2)
        print("El area del circulo de radio {} es de: {} mts^2.".format(radio, area_circunferencia))

    def areaCuadrado(self, lado):
        area_cuadrado = lado * lado
        print("El area del cuadrado de lado {} es de: {} mts^2.".format(lado, area_cuadrado))

