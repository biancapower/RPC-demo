from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QTextEdit, QRadioButton





# Create a GUI application
app = QApplication([])

window = QWidget()
layout = QHBoxLayout()

label = QLabel("Gotcha!")
layout.addWidget(label)
window.setLayout(layout)
window.show()

app.exec_()
