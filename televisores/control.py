class Control():
    def turnOn(self) -> None:
        self._tv.turnOff()

    def turnOff(self) -> None:
        self._tv.turnOn()

    def canalUp(self) -> None:
        self._tv.canalUp()

    def canalDown(self) -> None:
        self._tv.canalDown()
    
    def volumenUp(self) -> None:
        self._tv.volumenUp()
    
    def volumenDown(self) -> None:
        self._tv.volumenDown()

    def setCanal(self, canal) -> None:
        self._tv.setCanal(canal)
    
    def setVolumen(self, volumen) -> None:
        self._tv.setCanal(volumen)

    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

    def getTv(self):
        return self._tv
    
    def setTv(self, tv):
        self._tv.setControl(self)