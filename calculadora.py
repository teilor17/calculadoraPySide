from functools import partial

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setFixedSize(235,235)
        self.componente_general = QWidget(self)
        self.setCentralWidget(self.componente_general)
        # Creamos un layout principal
        self.layout_principal = QVBoxLayout()
        self.componente_general.setLayout(self.layout_principal)
        # Metodos para crear la parte visual de la calculadora
        self._crear_area_captura()
        self._crear_botone()
        self._conectar_botones()

    def _crear_area_captura(self):
        self.linea_entrada = QLineEdit()
        # Modificamos algunas propiedades
        self.linea_entrada.setFixedHeight(35)
        self.linea_entrada.setAlignment(Qt.AlignRight)
        self.linea_entrada.setReadOnly(True)
        # Agregamos la linea de entrada al layout principal
        self.layout_principal.addWidget(self.linea_entrada)

    def _crear_botone(self):
        #creamos un diccionario para definir cada boton de la calculadora
        self.botonoes = {}
        layout_botones = QGridLayout()
        #texto y posicion en el grid layout
        self.botones = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '3': (2, 0),
            '2': (2, 1),
            '1': (2, 2),
            '-': (2, 3),
            '0': (3, 0),
            '.': (3, 1),
            'C': (3, 2),
            '+': (3, 3),
            '=': (3, 4)
        }
        #creamos los botones y los agregamos al layot
        #la posicion es una tuple con valores
        for text_boton, posicion in self.botones.items():
            self.botonoes[text_boton] = QPushButton(text_boton)
            self.botonoes[text_boton].setFixedSize(40, 40)
            #publicar botones
            layout_botones.addWidget(self.botonoes[text_boton], posicion[0], posicion[1])
        #agergamos el layout de bootones al principal
        self.layout_principal.addLayout(layout_botones)

    def conectar_botones(self):
        for text_boton, boton in self.botones.items():
            if text_boton not  in {'=','C'}:
                #boton.clicked.connect(lambda: self._construir_exprecion(text_boton))
                boton.clicked.connect(partial(self._construir_exprecion, text_boton))










if __name__ == '__main__':
    app = QApplication()
    calculadora = Calculadora()
    calculadora.show()
    app.exec()