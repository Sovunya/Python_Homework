from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
from functools import partial
import math

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.line_edit = QLineEdit()
        self.line_edit.setFixedHeight(35)

        self.memory_label = QLabel()
        self.memory_label.setFixedHeight(35)

        self.grid_layout = QVBoxLayout()

        button_values = [
            ["7", "8", "9", "/", "sqrt"],
            ["4", "5", "6", "*", "^"],
            ["1", "2", "3", "-", "mem"],
            ["0", ".", "=", "+", "clear"],
        ]

        for row in button_values:
            button_row = QHBoxLayout()
            for label in row:
                button = QPushButton(label)
                button.setFixedHeight(50)
                button.setFixedWidth(50)
                button_row.addWidget(button)
                button.clicked.connect(partial(self.buttonClicked, label))
            self.grid_layout.addLayout(button_row)

        self.grid_layout.addWidget(self.line_edit)
        self.grid_layout.addWidget(self.memory_label)

        self.centralWidget.setLayout(self.grid_layout)

    def buttonClicked(self, label):
        current_text = self.line_edit.text()
        memory_text = self.memory_label.text()

        if label == "clear":
            self.line_edit.clear()
        elif label == "=":
            try:
                result = eval(current_text)
                self.line_edit.setText(str(result))
            except:
                self.line_edit.setText("Error")
        elif label == "mem":
            self.memory_label.setText(current_text)
        elif label == "sqrt":
            try:
                result = math.sqrt(float(current_text))
                self.line_edit.setText(str(result))
            except:
                self.line_edit.setText("Error")
        else:
            self.line_edit.setText(current_text + label)

if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()
