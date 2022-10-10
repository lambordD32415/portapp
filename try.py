import serial
# import threading

# gets the waiting data in the port and returns it 
def getWaitingDataFromPort(port):
	data = port.read(port.in_waiting)
	decodedData = data.decode('utf-8')
	return decodedData

# sending data to a port
def sendDataToPort(data, destinationPort):
	destinationPort.write(data.encode('utf-8'))

# openning the port that going to use and checking if it proper
def getPortNameAndConnect(portToEnter):
# letting the loop start
	port = serial.Serial()
	'''
	a loop that asks the user which port to connect and connecting it
	but if the name of the port is not exists or already opened then he asks again 
	as well their is a serial.Serial variable named port without any serial.Serial.port
	information so when it comes to the while loop its checking if its not open 
	and for the first time the condition equals true and then he  opens the port just 
	if the port is currect and then it gets out from the loop
	'''
	while(not port.is_open):
		try:
			port.port = "\\\\.\\" + input("Enter " + portToEnter + " Port To Connect ")
			port.open()
		except serial.serialutil.SerialException:
			print("ERROR - this port not found or already opened")
			
	# clears the waiting data before use it
	port.read(port.in_waiting)
	return port

# this function runs all the transmission between the original port and a virtual port and stopping it.
def runTheTransmission(originalPort, virtualPort):
# letting the loop start
	data = '1'
	'''
		a loop that getting waiting data from ports
		and transforming it from original port to a virtual ports and vice versa 
		than it stops tranforming when the data equals '0' and in the last if term
		thier is a command that prints "the transforming stoped" in the console 
	'''
	while(data != '0'):
		if(originalPort.in_waiting != 0):
			data = getWaitingDataFromPort(originalPort)
			sendDataToPort(data, virtualPort)
		elif(virtualPort.in_waiting != 0):
			data = getWaitingDataFromPort(virtualPort)
			sendDataToPort(data, originalPort)
		if(data == '0'):
			print("the transforming stoped")


# main
if __name__ == "__main__":
# getting information from the user and openning the useing ports
	originalPort = getPortNameAndConnect("Original")
	virtualPort_A = getPortNameAndConnect("Virtual a")
	# virtualPort_B = getPortNameAndConnect("Virtual b")
	
	# firstSplit = threading.Thread(target=runTheTransmission, args = [originalPort, virtualPort_A])
	# secondSplit = threading.Thread(target=runTheTransmission, args = [originalPort, virtualPort_B])
	
	# firstSplit.start()
	# secondSplit.start()
	
	# runTheTransmission(originalPort,virtualPort_A)
	runTheTransmission(originalPort,virtualPort_B)
