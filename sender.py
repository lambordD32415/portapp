import serial
import serial.tools.list_ports

# for port in serial.tools.list_ports.comports():
	# print(port.name)
	
testPort = serial.Serial()
testPort.port = "\\\\.\\COM4"
	
print(testPort.is_open)


testPort.open()
print(testPort.is_open)
	