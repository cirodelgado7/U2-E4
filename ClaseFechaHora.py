class FechaHora:
    __dd = 0
    __mm = 0
    __aa = 0
    __hs = 0
    __min = 0
    __seg = 0

    def __init__(self, dd=1, mm=1, aa=2020, hs=0, min=0, seg=0):
        self.__dd = dd
        self.__mm = mm
        self.__aa = aa
        self.__hs = hs
        self.__min = min
        self.__seg = seg

    def Mostrar(self):
        print('%.2d/%.2d/%.2d\t -\t %.2d:%.2d:%.2d' % (self.__dd, self.__mm, self.__aa, self.__hs, self.__min, self.__seg))
        self.validaEntrada(self.__dd, self.__mm, self.__aa, self.__hs, self.__min, self.__seg)

    def validaEntrada(self, dd, mm, aa, hs, min, seg):
        valido = False
        if hs in range(0, 24):
            if min in range(0, 60):
                if seg in range(0, 60):
                    if mm in [1, 3, 5, 7, 8, 10, 12]:
                        if dd in range(1, 32):
                            valido = True
                    elif mm in [4, 6, 9, 11]:
                        if dd in range(1, 31):
                            valido = True
                    elif mm == 2:
                        bisiesto = self.bisiesto(aa)
                        if bisiesto:
                            if dd in range(1, 30):
                                valido = True
                        else:
                            if dd in range(1, 29):
                                valido = True
        if valido:
            print('La fecha y la hora ingresadas son válidas')
        else:
            print('La fecha y la hora ingresadas no son válidas')

    def bisiesto(self, aa):
        bisiesto = False
        if aa % 4 == 0 and (aa % 100 != 0 or aa % 400 == 0):
            bisiesto = True
        return bisiesto

    def PonerEnHora(self,hs = 00, min = 00, seg = 00):
        self.__hs = hs
        self.__min = min
        self.__seg = seg

    def AdelantarHora(self, hs = 00, min = 00, seg = 00):
        self.__hs += hs
        self.__min += min
        self.__seg += seg
        if seg >= 60:
            self.__seg = self.__seg % 60
            self.__min += self.__seg // 60
        if min >= 60:
            self.__min = self.__min % 60
            self.__hs += self.__min // 60
        if self.__hs >= 24:
            self.__hs = self.__hs % 24
            self.__dd += self.__hs // 24
        if self.__mm in [1,3,5,7,8,10,12]:
            if self.__dd >= 31:
                if self.__mm >= 12:
                    self.__aa += 1
                    self.__mm = 1
                    self.__dd = (self.__dd % 31) + 1
        elif self.__mm in [4,6,9,11]:
            if self.__dd >= 30:
                self.__mm += self.__dd // 30
                self.__dd = (self.__dd % 30) + 1
        elif self.__mm==2: #  Controlar si el año es bisiesto
            bisiesto = self.bisiesto(aa)

            if bisiesto == True: #  Cambio para los meses de 29 dias
                if self.__dd >= 29:
                    self.__mm += self.__dd // 29  #  suma el resultado de la division.
                    self.__dd = (self.__dd % 29)  #  si la division no da exacta sumo el resto
            else:
                if self.__dd >= 28: #  Cambio para los meses de 28 dias
                    self.__mm += self.__dd // 28
                    self.__dd = (self.__dd % 28)

         #  Actualizacion de meses y años en quinto lugar y ultimo lugar.
        if self.__mm > 12:
            self.__aa += mm // 24
            self.__mm = mm % 24