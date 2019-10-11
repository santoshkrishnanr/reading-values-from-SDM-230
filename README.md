# Reading-values-from-SDM-230
Python program to read values from SDM-230 and write in csv file 

## Getting Started

These instructions will help you do the connection required to read values from SDM-230 Modbus.

### Powering up the sdm230

line and neutral wires towards the input and output side is connected as per the diagram shown


![](https://github.com/santoshkrishnanr/reading-values-from-SDM-230/blob/master/sdm_wiring.png)
### Communicating wire 
A normal 3 or 4 wire can be connected to SDM 230 from their respective pins to any serial RS485 converter like Digitus as shown below 

image1 and image 2 

 Do check [modbus_csv0.3.py](https://github.com/santoshkrishnanr/reading-values-from-SDM-230/blob/master/modbus_csv0.3.py) for the values to be read and written in csv log file
 
 for the the program to read only values remove 
 
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
( 'V', 0x00, '%6.2f' ), # Voltage [V]
( 'Curr', 0x06, '%6.2f' ), # Current [A]
( 'P[act]', 0x0c, '%6.0f' ), # Active Power [W]
( 'P[app]', 0x12, '%6.0f' ), # Apparent Power  [W]
( 'P[rea]', 0x18, '%6.0f' ), # Reactive Power [W]
( 'PF', 0x1e, '%6.3f' ), # Power Factor [1]
( 'Phi', 0x24, '%6.1f' ), # cos(Phi)? [1]
( 'Freq', 0x46, '%6.2f' ), # Line Frequency [Hz]
( 'W[act]', 0x0156, '%6.2f' ), # Energy [kWh]
( 'W[rea]', 0x0158, '%6.2f' ) # Energy react [kvarh]

```



## Authors

* **Santosh Krishnan** - *Initial work* -


## Acknowledgments

* After the the values are read from the smart meter further calculation, ploting graph can be done 
* happy coading !!

