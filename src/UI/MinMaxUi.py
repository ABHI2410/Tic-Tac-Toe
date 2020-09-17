
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication,QMainWindow 
import sys 

class Tic_Tac_Toe(QMainWindow):
	
	def __init__(self):
		super(Tic_Tac_Toe, self).__init__()
		self.setGeometry(200,200,300,300)
		self.setWindowTitle("Tic_Tac_Toe")
		self.initUi()
		
	def initUi(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText("This is label")
		self.label.move(50,50)

		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("Click Me")
		self.b1.clicked.connect(self.clicked)
		self.b1.move(50,80)

	def clicked(self):
		self.label.setText("You pressed the button")
		self.update()

	def update(self):
		self.label.adjustSize()

  
def window():
	app = QApplication(sys.argv)
	win = Tic_Tac_Toe()

	win.show()

	sys.exit(app.exec_())


window()