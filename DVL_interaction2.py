# Author: Stephen Sumner
# Robotics Club at UCF, AUVSI Robosub 2017/2018
# 11/20/2017
#
# This program is the python implementation for communication with
# the Teledyne RDI Doppler Velocity Log
from dvlpackage import *
from PD5package import *
import serial
import rospy
import std_msgs

numberformat = 5

newDVL = DVL(numberformat)
newDVL.statusCheck(newDVL.DVLserialPacket,newDVL.DVLraw,newDVL.StartingByte)
newDVL.DVL_talker()
