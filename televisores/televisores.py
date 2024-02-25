class Marca():
    def __init__(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, marca):
        self.nombre = marca

class TV():
    numTV = 0
    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = "Control"

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getCanal(self):
        return self.canal

    def setCanal(self, canal):
        self.canal = canal

    def getPrecio(self):
        return self.precio
    
    def setPrecio(self, precio):
        self.precio = precio

    def getVolumen(self):
        return self.volumen
    
    def setVolumen(self, volumen):
        self.volumen = volumen

    def getControl(self):
        return self.control
    
    def setControl(self, control):
        self.control = control

    def turnOff(self):
        self.estado = False

    def turnOn(self):
        self.estado = True

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.estado and (self.canal >= 1 and self.canal <= 120):
            self.canal += 1

    def canalDown(self):
        if self.estado and (self.canal >= 1 and self.canal <= 120):
            self.canal -= 1
    
    def volumenUp(self):
        if self.estado:
            self.volumen += 1
    
    def volumenDown(self):
        if self.estado:
            self.volumen -= 1

class Control():
    def __init__(self, tv):
        self.tv = tv

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if self.estado and (self.canal >= 1 and self.canal <= 120):
            self.canal += 1

    def canalDown(self):
        if self.estado and (self.canal >= 1 and self.canal <= 120):
            self.canal -= 1
    
    def volumenUp(self):
        if self.estado:
            self.volumen += 1
    
    def volumenDown(self):
        if self.estado:
            self.volumen -= 1

    def setCanal(self, canal):
        self.canal = canal
    
    def setVolumen(self, volumen):
        self.volumen = volumen

    def enlazar(self, tv):
        self.tv = tv
        self.tv.control(self)
