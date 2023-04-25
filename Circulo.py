#Este es mi pull request a Pepe

from cmath import pi

class Circulo:

    _radio:float

    def __init__(self,radio: float):
        self._radio=radio
        
    def area(self):
        area = self._radio**2 * pi
        return area

    def circunferencia(self):
        circunferencia = self._radio*2*pi
        return circunferencia