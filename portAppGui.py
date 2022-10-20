import PyQt5.QtWidgets as qtw


baudrateList = ['9600', '3000']

def stamPrintFunc(): #Thisd is a fuction
	print("Button is clicked")


class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.splitPortBtn = qtw.QPushButton(self)
		self.splitPortBtn.setText("split")
		self.mainLayout = qtw.QVBoxLayout()
		self.mainLayout.addLayout(self.createOptionsLayout(portType = 'Original port'))
		self.mainLayout.addLayout(self.createOptionsLayout(portType = 'Virtual port'))
		self.mainLayout.addWidget(self.splitPortBtn)
		# self.splitPortBtn.setCheckable(True)
		self.splitPortBtn.clicked.connect(self.mainLayout.addLayout(self.createOptionsLayout(portType = 'virtual port 2')))
		self.setLayout(self.mainLayout)
		self.show()
		# if self.splitPortBtn.isChecked():
			# self.mainLayout.addLayout(self.createOptionsLayout(portType = 'Virtual port 2'))
		
	def createOptionsLayout(self, portType = 'some port'):
		optionsLayout = qtw.QVBoxLayout()
		layoutH = qtw.QHBoxLayout()
		
		originalLbl = qtw.QLabel(portType, self)
		pairLbl = qtw.QLabel('pair', self)
		portsCB = qtw.QComboBox()
		baudRateCB = qtw.QComboBox()
		baudRateCB.addItems(baudrateList)
		connectPortBtn = qtw.QPushButton('connect to port', self)
		# self.testButton.clicked.connect(stamPrintFunc)
		optionsLayout.addWidget(originalLbl)

		layoutH.addWidget(portsCB)
		layoutH.addWidget(baudRateCB)
		layoutH.addWidget(connectPortBtn)
		optionsLayout.addLayout(layoutH)
		optionsLayout.addWidget(pairLbl)
		return optionsLayout

		def splitButton(self):
			optionsLayout = qtw.QVBoxLayout()
			layoutH = qtw.QHBoxLayout()
			splitPortBtn = qtw.QPushButton('Split', self)
			self.splitButton.setCheckable(true)
			self.splitButton.toggle()



if __name__ == '__main__':
	app = qtw.QApplication([])
	mw = MainWindow()
	app.exec_()