import serial

# noticing the source port and returning the data from it 
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

# noticing the distination port and sending the data to him
def getFromApp(data, destinationPort =""):
	print(type(data))
	print(destinationPort)
	destinationPort = serial.Serial(port = destinationPort)
	destinationPort.write(data.encode('utf-8'))


# main
if __name__ == "__main__":
# getting information from the user
	sorcePort = input('who you send to: ')
	destinationPort = input('from who you send: ')
# letting the loop start
	realData = '1'
	'''
		a loop that transforming data from port to port and stop
		tranforming when the data equals '0' than in the else term
		sending the last massage that says "end massage" 
	'''
	while(realData!='0'):
		realData = sendToApp(sorcePort = sorcePort)
		if (realData != '0'):
			getFromApp(realData,destinationPort = destinationPort)
		else:
			getFromApp("end massage",destinationPort = destinationPort)