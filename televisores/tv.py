class TV():
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        
        TV._numTV += 1

    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getCanal(self):
        return self._canal

    def setCanal(self, canal):
        if self._estado and (canal >= 1 and canal <= 120):
            self._canal = canal

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, precio):
        self._precio = precio

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, volumen):
        if self._estado and (volumen >= 0 and volumen <= 7):
            self._volumen = volumen

    def getControl(self):
        return self._control
    
    def setControl(self, control):
        self._control = control

    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV

    def turnOff(self):
        self._estado = False

    def turnOn(self):
        self._estado = True

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        self.setCanal(self._canal + 1)

    def canalDown(self):
        self.setCanal(self._canal - 1)
    
    def volumenUp(self):
        self.setVolumen(self._volumen + 1)
    
    def volumenDown(self):
        self.setVolumen(self._volumen - 1)


