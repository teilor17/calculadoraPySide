from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setFixedSize(235, 235)
        self.componente_general = QWidget(self)
        self.setCentralWidget(self.componente_general)
        #Layout Principal
        self.layout_principal = QVBoxLayout()
        self.componente_general.setLayout(self.layout_principal)
        #Metodos para la parte Visual
        self._area_de_captura()



if __name__ == '__main__':
    app = QApplication()
    calculadora = Calculadora()
    calculadora.show()
    app.exec()

