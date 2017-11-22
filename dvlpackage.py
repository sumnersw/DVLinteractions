import serial
from PD5package import *
import rospy
import std_msgs


class DVL:
    def __init__(self, Numformat):
            
        operationmode = 0           # operation modes: 0 = packets, 1 = stream
        dvlPort = '/dev/tty01'      # UART1 Rx and Tx,
        serialspeed = 9600
        dvltimeout = 1.0
        DVLraw = bytearray(255)
        DVLserialpacket = bytearray(255)
        DVLcalculatedChecksum = 0     # checksum and format checking
        DVLpacket = PD5packet()
        DVLdata = []

        # change these if PD[X] changes, refer to chapter 8, page 171 in the DVL operation manual
        self.StartingByte = bytearray(1)       # the starting byte changes with #PD[X] format
        self.FormatByte = bytearray(1)         # the format byte changes with #PD[X] format 
        self.IndexChecksumLSB = 0              # the index checksum LSB (and MSB) byte(s) change with #PD[X] format
        self.TotalBytes = 0                    # THE total number of bytes within a serial packet changes with #PD[X] format    
        self.Numformat=Numformat

        if Numformat == 5:
            self.StartingByte[0]=0x7D
            self.FormatByte[0]=0x01
            self.indexChecksumLSB=86
            self.TotalBytes=88

        DVLserial=serial.Serial(dvlPort,serialspeed,timeout=dvltimeout)


    def openPort(self):
        DVLserial.open()


    def closePort(self):
        DVLserial.close()


    def getRawData(self, DVLraw):
        connection_check = DVLserial.readinto(DVLraw)

        if connection_check < 255:
            if connection_check ==0:
                print("\nThe DVL is not responding")
            else:
                print("\nThe DVL's serial stream ended prematurly")
        else:
            return DVLraw    


    def filterRawData(self, DVLraw, DVLserialPacket):
        
        index1=DVLraw.find(self.StartingByte)

        if index1==(self.totalBytes*2+1):
            print("\nThe DVL is not giving valid data")                    
        else:
            for i in range(0,self.TotalBytes+1):
                DVLserialPacket[i]==DVLraw[index1+i]    
                # set the first byte in the DVLserialPacket to where the packet begins in the raw feed     

        return DVLserialPacket


    def dvlChecksum(DVLserialpacket):
    
        for i in range(0,DVLserialPacket[2],1):
            DVLcalculatedChecksum=DVLcalculatedChecksum+DVLserialPacket[i]  
            # sum all the bytes together

        DVLcalculatedChecksum=DVLcalculatedChecksum%65536
        # then modulo by 65536 per page 202 in the DVL operation manual

        DVLsentChecksum=(DVLserialPacket[IndexChecksumLSB+1]<<8)+DVLserialPacket[IndexChecksumLSB]  # add the two checksum bytes together

        # if the checksums match, send the serial packet over to be formated
        if DVLsentChecksum == DVLcalculatedChecksum:
            # uses PD5 format            
            if Numformat == 5:
                return 0
            else:
                return 3        # DVL is not in the correct format, make sure it is in 
                                #PD5, refer to pages 42, 44, 172, and 203-209
        else:
            return 4        # incorrect checksum
    
    def DVL_process_data(self):
        
        self.getRawData(self.DVLraw)
        self.filterRawData(self.DVLraw,self.DVLserialPacket)
        DVLpacket.formatPD5data(self.DVLserialPacket)
        return PD5datalist(PD5packet)
            

    def DVL_talker(self):
        pub = rospy.Publisher('DVL_talk', ByteMultiArray)
        rospy.init_node('DVL_talker', anonymous=True)
        rospy.spin()

        if operationmode == 0:
            rate = rospy.Rate(60)
            while not rospy.is_shutdown():
                self.openPort()
                self.DVL_process_data()
                self.closePort()
                rospy.loginfo(DVLdata)
                pub.publish(DVLdata)
                rate.sleep()
                            
        elif operationmode == 1:
            self.openPort()
            rate = rospy.Rate(-1)
            while not rospy.is_shutdown():
                self.DVL_process_data()
                rospy.loginfo(DVLdata)
                pub.publish(DVLdata)
                rate.sleep()

            self.closePort()
            
        else:
            print "operation mode parameter not set"

    
    def statusCheck(self, DVLserialPacket, DVLraw, StartingByte):
        index_1 = DVLraw.find(StartingByte)
        connection_check = DVLserial.readinto(DVLraw)
        DVLserialPacket = filterRawData(DVLraw, DVLserialPacket)
        DVL_Checksum = dvlChecksum(DVLserialPacket)

        if DVL_Checksum == 0:
            print "\nBottom Tracking Velocity:\tX: "
            print hex(DVLdataPD5[4])
            print "\tY: "
            print hex(DVLdataPD5[5])
            print "\tZ: "
            print hex(DVLdataPD5[6])
            print "\tE: "
            print hex(DVLdataPD5[7])
        elif connection_check == 0:
            print "\nThe DVL is not responding"
        elif connection_check < 255:
            print "\nThe DVL's serial stream ended prematurly"
        elif index1==(totalBytes*2+1) or DVL_Checksum == 3:
            print "\nThe DVL is not in the correct format"
        elif DVL_Checksum == 4:
            print "\nThe DVL's Checksum did not properly add up, run function again"
        elif DVL_Checksum == 5:
            print "/nYou have requested a non-exsistent, or non-programmed format option, please choose 5"

     