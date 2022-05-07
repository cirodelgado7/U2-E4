class Ventana:
    __titulo = ''
    __xSuperiorI = 0
    __ySuperiorI = 0
    __xInferiorD = 0
    __yInferiorD = 0

    def __init__(self, titulo='', xSuperiorI=0, ySuperiorI=0, xInferiorD=500, yInferiorD=500):
        self.__titulo = titulo
        self.__xSuperiorI = xSuperiorI
        self.__ySuperiorI = ySuperiorI
        self.__xInferiorD = xInferiorD
        self.__yInferiorD = yInferiorD

    def mostrar(self):
        print('Ventana: {} \nxSupI: {} \nySupI: {} \nxInfD: {} \nyInfD: {}'
              .format(self.__titulo, self.__xSuperiorI, self.__ySuperiorI, self.__xInferiorD, self.__yInferiorD))

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def alto(self):
        return self.__xInferiorD - self.__xSuperiorI

    def ancho(self):
        return self.__yInferiorD - self.__ySuperiorI

    def moverDerecha(self, desplazamiento):
        if self.__xSuperiorI + desplazamiento <= 500 and self.__xInferiorD + desplazamiento <= 500:
            self.__xSuperiorI += desplazamiento
            self.__xInferiorD += desplazamiento
        else:
            print('No es posible realizar el desplazamiento')

    def moverIzquierda(self, desplazamiento):
        if self.__xSuperiorI - desplazamiento >= 0 and self.__xInferiorD - desplazamiento >= 0:
            self.__xSuperiorI -= desplazamiento
            self.__xInferiorD -= desplazamiento
        else:
            print('No es posible realizar el desplazamiento')

    def bajar(self, desplazamiento=1):
        if self.__ySuperiorI + desplazamiento <= 500 and self.__yInferiorD + desplazamiento <= 500:
            self.__ySuperiorI += desplazamiento
            self.__yInferiorD += desplazamiento
        else:
            print('No es posible realizar el desplazamiento')

    def subir(self, desplazamiento=1):
        if self.__ySuperiorI - desplazamiento >= 0 and self.__yInferiorD - desplazamiento >= 0:
            self.__ySuperiorI -= desplazamiento
            self.__yInferiorD -= desplazamiento
        else:
            print('No es posible realizar el desplazamiento')
