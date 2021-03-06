# Reading-values-from-SDM-230
Python program to read values from SDM-230 and write in csv file 

## Getting Started

These instructions will help you do the connection required to read values from SDM-230 Modbus.

### Powering up the sdm230

line and neutral wires towards the input and output side is connected as per the diagram shown
(**Warning!! keep in mind its 230v AC)


![](https://github.com/santoshkrishnanr/reading-values-from-SDM-230/blob/master/sdm_wiring.png)
### Communicating wire 
A normal 3 or 4 wire can be connected to SDM 230 from their respective pins to any serial RS485 converter like Digitus as shown below 

![](https://github.com/santoshkrishnanr/reading-values-from-SDM-230/blob/master/sdm_modbus.jpeg) ![](https://github.com/santoshkrishnanr/reading-values-from-SDM-230/blob/master/digitus.jpeg)

* Do check [modbus_csv0.3.py](https://github.com/santoshkrishnanr/reading-values-from-SDM-230/blob/master/modbus_csv0.3.py) 
  for the values to be read and written in csv log file
 * keep in mind that the  port='/dev/ttyUSB0', baudrate=2400 and the baudrate has to be same in both SDM device and the program 
 port can be check by 
 ```
 dmesg | grep tty
 ```
 
 ** for the the program to read only values and not writing in csv 
 
```
import csv
with open('log.csv','w') as f:
	thewriter=csv.writer(f)
  thewriter.writerow(['year,month,date,hr:min:sec:ms,frequency     ','voltage     ','current    '])
  .
  ..
  ...
  thewriter.writerow([now,f1,v1,i1])
```




## To get other parameters like (Active power, Apparent Power,cos(Phi),etc)

change the reister address in 

```
    v = modbus.read_input_registers(0x00,2 , unit=1)
		f = modbus.read_input_registers(0x46,2 , unit=1)
		i = modbus.read_input_registers(0x06,2 , unit=1)
```
to its respective adress as shown below 
```
( 'V', 0x00), # Voltage [V]
( 'Curr', 0x06 ), # Current [A]
( 'P[act]', 0x0c  ), # Active Power [W]
( 'P[app]', 0x12 ), # Apparent Power  [W]
( 'P[rea]', 0x18  ), # Reactive Power [W]
( 'PF', 0x1e ), # Power Factor [1]
( 'Phi', 0x24  ), # cos(Phi)? [1]
( 'Freq', 0x46 ), # Line Frequency [Hz]
( 'W[act]', 0x0156 ), # Energy [kWh]
( 'W[rea]', 0x0158  ) # Energy react [kvarh]

```





* **Santosh Krishnan** - *Initial work* -


* After the the values are read from the smart meter further calculation, ploting graph can be done 
* happy coading !!

