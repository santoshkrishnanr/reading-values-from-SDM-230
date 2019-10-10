import struct
import binascii
import datetime
import time
import csv

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder



modbus = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=2400, timeout=1)
modbus.connect()
with open('log.csv','w') as f:
	thewriter=csv.writer(f)

 	thewriter.writerow(['year,month,date,hr:min:sec:ms,frequency     ','voltage     ','current    '])
	
	while True:
                
		v = modbus.read_input_registers(0x00,2 , unit=1)
		f = modbus.read_input_registers(0x46,2 , unit=1)
		i = modbus.read_input_registers(0x06,2 , unit=1)
	        now= datetime.datetime.now()
		
	        print(now.strftime("-------%Y-%m-%d %H:%M:%S----------"))
		decoder = BinaryPayloadDecoder.fromRegisters(v.registers,byteorder=Endian.Big)
	                                             
		v1=decoder.decode_32bit_float()
	        print ("voltage is ", v1, "V")
		
		decoder = BinaryPayloadDecoder.fromRegisters(f.registers,byteorder=Endian.Big)
		f1=decoder.decode_32bit_float()
		print ("frequency is ",f1, "hz")
		
		decoder = BinaryPayloadDecoder.fromRegisters(i.registers,byteorder=Endian.Big)
		i1=decoder.decode_32bit_float()
		print ("current is ", i1, "I")
	        print""

		thewriter.writerow([now,f1,v1,i1])
	
	        time.sleep(1)