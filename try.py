import serial

# gets the waiting data in the port and returns it 
def getWaitingDataFromPort(port = serial.Serial.port):
	while(True):
		data = port.read(port.in_waiting)
		decodedData = data.decode('utf-8')
		return decodedData

# sending data to a port
def sendDataToPort(data, destinationPort = serial.Serial.port):
	print(destinationPort) 
	destinationPort.write(data.encode('utf-8'))

# openning the port that going to use and checking if it proper
def getPortNameAndConnect(portToEnter):
# letting the loop start
	numErr = 1
	'''
	a loop that asks the user which port to connect and connect it
	but if the name of the port is not exist or already open then he asks agian 
	as well numErr shows if thier is any errors in a way that
	if numErr is equal 1 thier is an error and if it equals 0 so thier are no errors at all
	'''
	while(numErr != 0):
		try:
			portName = "\\\\.\\" + input("Enter " + portToEnter + " Port To Connect ")
			port = serial.Serial(portName)
			numErr = 0
			# clears the waiting data before use it
			port.read(port.in_waiting)
			return port
		except serial.serialutil.SerialException:
			print("ERROR - this port not found or already open")

# main
if __name__ == "__main__":
# getting information from the user and openning the useing ports
	originalPort = getPortNameAndConnect("Original")
	virtualPort = getPortNameAndConnect("Virtual")
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