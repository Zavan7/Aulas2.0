import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton ('Testando isso aqui.')
botao.setStyleSheet('font-size: 100px; color: blue;')
botao.show()

app.exec()