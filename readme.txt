****************************
*** DVL Input Arguments: ***
**************************** 
*** NumFormat: specifies which PD format the DVL is currently sending data out as, there are PD0, PD3, PD4, PD5, and PD6
               we use PD5. For more information go to page 172 in the DVL operation manual.
           
*** SerialSpeed: specifies the baud rate which the DVL is currently sending out data at. Generally this will either be 9600 or 115200            
                 to change this value refer to page 14

*************************
*** DVL return codes: ***
************************* 

*** 0: Successfully completed
*** 1: DVL not properly responding, check the serial connection
*** 2: stream ended prematurly, check the serial connections and DVL (make sure there is no wiggling or power issues)
*** 3: DVL is not in the correct format, make sure it is in #PD5, refer to pages 42, 44, 172, and 203-209
*** 4: Bad Checksum
*** 5: Invalid requested format

******************************************************
*** DVLserialPacket[] Index Values for PD5 format: ***
******************************************************

*** [0]:     DVL ID, should always be 0x7D
*** [1]:     DVL Data Structure, should always be 0x01
*** [2-3]:   Number of Bytes in String, should always be 0x56
*** [4]:     System Configuration, should always be 0xF3, 0b1111X011
               Earth Coordinate Velocities
               Tilt infomation used in calculations
               3 beam solution calclulated
               600-kHz Explorer DVL

*** [5-6]:   X-Velocity: Bottom, mm/s, LSB sent First! -32768 or 0x8000 indicated bad velocity
*** [7-8]:   Y-Velocity: Bottom, mm/s, LSB sent First! -32768 or 0x8000 indicated bad velocity
*** [9-10]:  Z-Velocity: Bottom, mm/s, LSB sent First! -32768 or 0x8000 indicated bad velocity
*** [11-12]: E-Velocity: Bottom, mm/s, LSB sent First! -32768 or 0x8000 indicated bad velocity

*** [13-14]: BM1: Vertical range from beam sensor 1 to the bottom, 0 denotes bad read
*** [15-16]: BM2: Vertical range from beam sensor 2 to the bottom, 0 denotes bad read
*** [17-18]: BM3: Vertical range from beam sensor 3 to the bottom, 0 denotes bad read
*** [19-20]: BM4: Vertical range from beam sensor 5 to the bottom, 0 denotes bad read

*** [21]:    Bottom Status, 0 indicates if system OK, check page 205 in DVL operation manual for Error Codes
 
*** [22-23]: 1-Velocity: WaterMass, mm/s, LSB sent First! not used   
*** [24-25]: 2-Velocity: WaterMass, mm/s, LSB sent First! not used   
*** [26-27]: 3-Velocity: WaterMass, mm/s, LSB sent First! not used   
*** [28-29]: 4-Velocity: WaterMass, mm/s, LSB sent First! not used   
 
*** [30-31]: Reference Layer Start, used for water-mass calculations, shoudld be 0
*** [32-33]: Reference Layer End, used for water-mass calculations, shoudld be 0
 
*** [34]:    Reference Layer Status: 0 indicates if system OK, check page 206 in DVL operation manual for Error Codes
 
*** [35]:    TOFP Hour:    Contains the Time of the first ping of the current ensamble
*** [36]:    TOFP Minute:  Contains the Time of the first ping of the current ensamble
*** [37]:    TOFP Second:  Contains the Time of the first ping of the current ensamble
*** [38]:    TOFP Error:   Contains the Time of the first ping of the current ensamble
 
*** [39-40]: Bit Result: Reserved, don't care
*** [41-42]: Speed of Sound: m/s
*** [43-44]: Temperature: in 0.01C incremements from +40.00C
 
*** [45]:    Salinity
*** [46-47]: Depth
*** [48-49]: Pitch
*** [50-51]: Roll
*** [52-53]: Heading
 
*** [54-57]: Distance Made Good over the bottom  in the East, SUM of all X pings
*** [58-61]: Distance Made Good over the bottom  in the North, SUM of all Y pings
*** [62-65]: Distance Made Good over the bottom  in the Up, SUM of all Z pings
*** [66-69]: Distance Made Good over the bottom  error results
 
*** [70-73]: Distance Made Good over the water-mass in the East, SUM of all X pings, not used
*** [74-77]: Distance Made Good over the water-mass in the North, SUM of all Y pings, not used
*** [78-81]: Distance Made Good over the water-mass in the Up, SUM of all Z pings, not used
*** [82-85]: Distance Made Good over the water-mass error results
 
*** [86-87]: CheckSum,sum all individual bytes up, then modulo 0x10000
 
***********************************
*** HOW TO CHANGE DVL SETTINGS: ***
*********************************** 
install BBtalk form Teledyne RDI for the DVL Explorer Series
follow the instructions on page 12 and then keep reading for literally the rest of the manual, 
there's good stuff in there.  