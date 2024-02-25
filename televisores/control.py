class Control():
    def __init__(self):
        pass

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if self.estado and (self.canal >= 1 or self.canal <= 120):
            self.canal += 1

    def canalDown(self):
        if self.estado and (self.canal >= 1 or self.canal <= 120):
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
        self.tv.control(self.setControl)

    def getTv(self):
        return self.tv
    
    def setTv(self, tv):
        self.tv = tv