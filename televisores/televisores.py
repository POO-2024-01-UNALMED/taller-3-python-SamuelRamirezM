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

