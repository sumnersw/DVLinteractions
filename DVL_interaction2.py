# Author: Stephen Sumner, John Millner
# Robotics Club at UCF, AUVSI Robosub 2017/2018
# 10/22/2017
#
# This program is the python implementation for communication with
# the Teledyne RDI Doppler Velocity Log
from dvlpackage import *

import serial
import rospy
import std_msgs

def DVLformatPD5(DVLserialPacket):
    #
    # This function takes as an argument a list of bytes called DVLserialPacket
    # DVLserialPacket should contain 88 bytes of valid data as read from the Doppler Velocity Log
    #

    DVLdataPD5[0]=DVLserialPacket[0]                            # Explorer DVl identification word (should always be 0x7D
    DVLdataPD5[1]=DVLserialPacket[1]                            # Format Byte (should always be 0x01)
    DVLdataPD5[2]=(DVLserialPacket[3]<<8)+DVLserialPacket[2]    # Number of bytes in the array, minus the checksum(should always be 0x87)
    DVLdataPD5[3]=DVLserialPacket[4]                            # system config in binary XX-X-X-X-XXX more info on page 205

    DVLdataPD5[4]=(DVLserialPacket[6]<<8)+DVLserialPacket[5]    # X-Velocity: Bottom, mm/s, LSB sent First! -32768 or 0x8000 indicated bad velocity
    DVLdataPD5[5]=(DVLserialPacket[8]<<8)+DVLserialPacket[7]    # Y-Velocity: Bottom, mm/s, LSB sent First! -32768 or 0x8000 indicated bad velocity
    DVLdataPD5[6]=(DVLserialPacket[10]<<8)+DVLserialPacket[9]   # Z-Velocity: Bottom, mm/s, LSB sent First! -32768 or 0x8000 indicated bad velocity
    DVLdataPD5[7]=(DVLserialPacket[12]<<8)+DVLserialPacket[11]  # E-Velocity: Bottom, mm/s, LSB sent First! -32768 or 0x8000 indicated bad velocity

    DVLdataPD5[8]=(DVLserialPacket[14]<<8)+DVLserialPacket[13]  # BM1: Vertical range from beam sensor 1 to the bottom, 0 denotes bad read
    DVLdataPD5[9]=(DVLserialPacket[16]<<8)+DVLserialPacket[15]  # BM2: Vertical range from beam sensor 1 to the bottom, 0 denotes bad read
    DVLdataPD5[10]=(DVLserialPacket[18]<<8)+DVLserialPacket[17] # BM3: Vertical range from beam sensor 1 to the bottom, 0 denotes bad read
    DVLdataPD5[11]=(DVLserialPacket[20]<<8)+DVLserialPacket[19] # BM4: Vertical range from beam sensor 1 to the bottom, 0 denotes bad read

    DVLdataPD5[12]=DVLserialPacket[21]  # Bottom Status, 0 indicates if system OK, check page 205 in DVL operation manual for Error Codes

    DVLdataPD5[13]=(DVLserialPacket[23]<<8)+DVLserialPacket[22]     # 1-Velocity: WaterMass, mm/s, LSB sent First! not used 
    DVLdataPD5[14]=(DVLserialPacket[25]<<8)+DVLserialPacket[24]     # 2-Velocity: WaterMass, mm/s, LSB sent First! not used 
    DVLdataPD5[15]=(DVLserialPacket[27]<<8)+DVLserialPacket[26]     # 3-Velocity: WaterMass, mm/s, LSB sent First! not used 
    DVLdataPD5[16]=(DVLserialPacket[29]<<8)+DVLserialPacket[28]     # 4-Velocity: WaterMass, mm/s, LSB sent First! not used 

    DVLdataPD5[17]=(DVLserialPacket[31]<<8)+DVLserialPacket[30]     # Reference Layer Start, used for water-mass calculations, shoudld be 0
    DVLdataPD5[18]=(DVLserialPacket[33]<<8)+DVLserialPacket[32]     # Reference Layer End, used for water-mass calculations, shoudld be 0
  
    DVLdataPD5[19]=DVLserialPacket[34]      # Reference Layer Status: 0 indicates if system OK, check page 206 in DVL operation manual for Error Codes
  
    DVLdataPD5[20]=DVLserialPacket[35]      # TOFP Hour:    Contains the Time of the first ping of the current ensamble
    DVLdataPD5[21]=DVLserialPacket[36]      # TOFP Minute:  Contains the Time of the first ping of the current ensamble
    DVLdataPD5[22]=DVLserialPacket[37]      # TOFP Second:  Contains the Time of the first ping of the current ensamble
    DVLdataPD5[23]=DVLserialPacket[38]      # TOFP Error:   Contains the Time of the first ping of the current ensamble

    DVLdataPD5[24]=(DVLserialPacket[40]<<8)+DVLserialPacket[39]     # Bit Result: Reserved, don't care
    DVLdataPD5[25]=(DVLserialPacket[42]<<8)+DVLserialPacket[41]     # Speed of Sound: m/s
    DVLdataPD5[26]=(DVLserialPacket[44]<<8)+DVLserialPacket[43]     # Temperature: in 0.01C incremements from +40.00C
    DVLdataPD5[27]=DVLserialPacket[45]                              # Salintity

    DVLdataPD5[28]=DVLserialPacket[46]

    DVLdataPD5[29]=(DVLserialPacket[48]<<8)+DVLserialPacket[47] # Depth
    DVLdataPD5[30]=(DVLserialPacket[50]<<8)+DVLserialPacket[49] # Pitch
    DVLdataPD5[31]=(DVLserialPacket[52]<<8)+DVLserialPacket[51] # Roll
    DVLdataPD5[32]=(DVLserialPacket[54]<<8)+DVLserialPacket[53] # Yaw
 
    DVLdataPD5[33]=(long(DVLserialPacket[58])<<24)+(long(DVLserialPacket[57])<<16)+(long(DVLserialPacket[56])<<8)+long(DVLserialPacket[55]) # Distance Made Good over the bottom  in the East, SUM of all X pings
    DVLdataPD5[34]=(long(DVLserialPacket[62])<<24)+(long(DVLserialPacket[61])<<16)+(long(DVLserialPacket[60])<<8)+long(DVLserialPacket[59]) # Distance Made Good over the bottom  in the North, SUM of all Y pings
    DVLdataPD5[35]=(long(DVLserialPacket[66])<<24)+(long(DVLserialPacket[65])<<16)+(long(DVLserialPacket[64])<<8)+long(DVLserialPacket[63]) # Distance Made Good over the bottom  in the Up, SUM of all Z pings
    DVLdataPD5[36]=(long(DVLserialPacket[70])<<24)+(long(DVLserialPacket[69])<<16)+(long(DVLserialPacket[68])<<8)+long(DVLserialPacket[67]) # Distance Made Good over the bottom  error results
 
    DVLdataPD5[37]=(long(DVLserialPacket[74])<<24)+(long(DVLserialPacket[73])<<16)+(long(DVLserialPacket[72])<<8)+long(DVLserialPacket[71]) # Distance Made Good over the water-mass in the East, SUM of all X pings, not used
    DVLdataPD5[38]=(long(DVLserialPacket[78])<<24)+(long(DVLserialPacket[77])<<16)+(long(DVLserialPacket[76])<<8)+long(DVLserialPacket[75]) # Distance Made Good over the water-mass in the North, SUM of all Y pings, not used
    DVLdataPD5[39]=(long(DVLserialPacket[82])<<24)+(long(DVLserialPacket[81])<<16)+(long(DVLserialPacket[80])<<8)+long(DVLserialPacket[79]) # Distance Made Good over the water-mass in the Up, SUM of all Z pings, not used
    DVLdataPD5[40]=(long(DVLserialPacket[86])<<24)+(long(DVLserialPacket[85])<<16)+(long(DVLserialPacket[84])<<8)+long(DVLserialPacket[83]) # Distance Made Good over the water-mass error results
  
    DVLdataPD5[41]=(DVLserialPacket[88]<<8)+DVLserialPacket[87] # CheckSum,sum all individual bytes up, then modulo 0x10000


def DVL(NumFormat, SerialSpeed):
  
#    DVLraw=bytearray(255)           # unformated feed taken directly from serial where the packet of data is randomly within
#    DVLserialPacket=bytearray(255)  # unformated packet of data from DVLraw
    
#    StartingByte=bytearray(1)       # THE STARTING BYTE CHANGES WITH #PD[X] FORMAT, CHANGE THIS IF PD[X] CHANGES, REFER TO CHAPTER 8, PAGE 171 IN THE DVL OPERATION MANUAL
#    FormatByte=bytearray(1)         # THE FORMAT BYTE CHANGES WITH #PD[X] FORMAT, CHANGE THIS IF PD[X] CHANGES, REFER TO CHAPTER 8, PAGE 171 IN THE DVL OPERATION MANUAL
#    IndexChecksumLSB=0              # THE INDEX CHECKSUM LSB (AND MSB) BYTE(S) CHANGE WITH #PD[X] FORMAT, CHANGE THIS IF PD[X] CHANGES, REFER TO CHAPTER 8, PAGE 171 IN THE DVL OPERATION MANUAL
#    TotalBytes=0                    # THE total number of bytes within a serial packet CHANGES WITH #PD[X] FORMAT, CHANGE THIS IF PD[X] CHANGES, REFER TO CHAPTER 8, PAGE 171 IN THE DVL OPERATION MANUAL    

    if NumFormat == 5:
        StartingByte[0]=0x7D
        FormatByte[0]=0x01
        indexChecksumLSB=86
        TotalBytes=88
    else:
        return 5

    dvlPort = '/dev/tty01'    # UART1 Rx and Tx, 
    DVLserial = serial.Serial(DVLport, SerialSpeed, bytesize=EIGHTBITS, timeout=1.0) # function argument "SerialSpeed" sets speed of communication, generally its either 9600 or 115200


# TODO: re-write this section so that instead of opening and closing the connection,
#       The program continuously reads in the data and publishes as often as it can.
    
    DVLserial.open()
    connection_check = DVLserial.readinto(DVLraw) # dump a portion of the DVL serial stream into an array for processing
    DVLserial.close()    

    if connection_check == 0:
        return 1                        # The Serial Stream did not properly open
    elif connection_check < 255:
        return 2                        # The Serial Stream ended prematurely

    while 1:                            # walk through the raw data to find the starting bit of the DVL packet
    #
    #        |--------------------------------------\\\\\\\\\\\\\\\\\\\\\----------------------------------------|
    #        |.......startedListeningMidPacket.......|NewCompletePacket!|.......FinsihedListeningMidPacket.......|
    #        |--------------------------------------/////////////////////----------------------------------------|
    #        
    #
        index1=DVLraw.find(StartingByte)

        if index1==(totalBytes*2+1):
            return 3    # the DVL Stream is giving invalid data, we know this becuase after scaniing through 255 bytes from the stream, no starting byte was found even when given 3 chances                    
        else:
            for i in range(0,TotalBytes):
                DVLserialPacket[i]==DVLraw[index1+i]    # set the first byte in the DVLserialPacket to where the packet begins in the raw feed     
            DVLbyteSize=(DVLraw[index1+3]<<8)+DVLraw[index1+2]+2    #figure out how many bytes to add to the serial packet by using the "No. of Bytes" bytes 3&4 that are included in the packet. add two to include the checksum


    DVLcalculatedChecksum=0 # checksum and format checking
    
    for i in range(0,DVLserialPacket[2],1):
        DVLcalculatedChecksum=DVLcalculatedChecksum+DVLserialPacket[i]  # sum all the bytes together

    DVLcalculatedChecksum=DVLcalculatedChecksum%65536   # then modulo by 65536 per page 202 in the DVL operation manual

    DVLsentChecksum=(DVLserialPacket[IndexChecksumLSB+1]<<8)+DVLserialPacket[IndexChecksumLSB]  # add the two checksum bytes together

    if DVLsentChecksum==DVLcalculatedChecksum:      # if the checksums match, send the serial packet over to be formated
        if NumFormat == 5:      # uses PD5 format
            DVLformatPD5(DVLserialPacket)
            return 0
        else:
            return 3        # DVL is not in the correct format, make sure it is in #PD5, refer to pages 42, 44, 172, and 203-209
    else:
        return 4        # incorrect checksum

DVLcheck = DVL(5, 9600)

if DVLcheck == 0:
    print("\nBottom Tracking Velocity:\tX: ")
    print hex(DVLdataPD5[4])
    print("\tY: ")
    print hex(DVLdataPD5[5])
    print("\tZ: ")
    print hex(DVLdataPD5[6])
    print("\tE: ")
    print hex(DVLdataPD5[7])
elif DVLcheck == 1:
    print("\nThe DVL is not responding")
elif DVLcheck == 2:
    print("\nThe DVL's serial stream ended prematurly")
elif DVLcheck == 3:
    print("\nThe DVL is not in the correct format")
elif DVLcheck == 4:
    print("\nThe DVL's Checksum did not properly add up, run function again")
elif DVLcheck == 5:
    print("/nYou have requested a non-exsistent, or non-programmed format option, please choose 5")
