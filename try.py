import serial


def sendToApp(sorcePort = ""):
	destinationPort = serial.Serial(port=sorcePort)
	while(True):
		waitingToRead = destinationPort.in_waiting
		if(waitingToRead != 0):
			print(waitingToRead)
			data = destinationPort.read(waitingToRead)
			decodedData = data.decode('utf-8')
			print(decodedData)
			if(decodedData != None):
				return decodedData


def getFromApp(data, destinationPort =""):
	print(type(data))
	destinationPort = serial.Serial(port = destinationPort)
	destinationPort.write(data.encode('utf-8'))

if __name__ == "__main__":
do{
	sorcePort = input('who you send to')
	destinationPort = input('from who you send')
}
while(realData!='0'):
		if(realData=='1'):
			
		realData = sendToApp(sorcePort = sorcePort)
		if (realData != '0'):
			getFromApp(realData,destinationPort = destinationPort)


	# printMessage(msg="junk", sendTo=10)
	# print(type("String"))
	# myPort = serial.Serial()
	# print(type(myPort))
	# myPort.open()
	# serial.Serial().write()
	# ksdfsdf



	