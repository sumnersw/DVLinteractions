from serial import *
from rospy import *
from std_msgs import *

class PD5packet:
    def __init__(self):
        dvl_id_word = bytearray(1)
        format_byte = bytearray(1)
        number_of_bytes = bytearray(2)
        sys_config = bytearray(1)

        x_velocity = bytearray(2)
        y_velocity = bytearray(2)
        z_velocity = bytearray(2)
        e_velocity = bytearray(2)
        
        beam_sensor_1 = bytearray(2)
        beam_sensor_2 = bytearray(2)
        beam_sensor_3 = bytearray(2)
        beam_sensor_4 = bytearray(2)
        
        bottom_status = bytearray(1)
        
        velocity_1 = bytearray(2)
        velocity_2 = bytearray(2)
        velocity_3 = bytearray(2)
        velocity_4 = bytearray(2)
        
        ref_layer_start = bytearray(2)
        ref_layer_end = bytearray(2)
        ref_layer_status = bytearray(1)
        
        tofp_hour = bytearray(1)
        tofp_minute = bytearray(1)
        tofp_second = bytearray(1)
        tofp_error = bytearray(1)
        
        bit_result = bytearray(2)
        speed_of_sound = bytearray(2)
        temperature = bytearray(2)
        salinity = bytearray(1)

        depth = bytearray(2)
        pitch = bytearray(2)
        roll = bytearray(2)
        yaw = bytearray(2)

        distance_east = bytearray(4)
        distance_north = bytearray(4)
        distance_up = bytearray(4)
        distance_error = bytearray(4)

        water_mass_east = bytearray(4)
        water_mass_north = bytearray(4)
        water_mass_up = bytearray(4)
        water_mass_error = bytearray(4)
        
        checksum = bytearray(2)
    
    def formatPD5data(self, DVLserialPacket):
        
        dvl_id_word = DVLserialPacket[0]
        format_byte = DVLserialPacket[1]
        number_of_bytes  = (DVLserialPacket[3]<<8)+DVLserialPacket[2]
        sys_config = DVLserialPacket[4]

        x_velocity = (DVLserialPacket[6]<<8)+DVLserialPacket[5]
        y_velocity = (DVLserialPacket[8]<<8)+DVLserialPacket[7]
        z_velocity = (DVLserialPacket[10]<<8)+DVLserialPacket[9]
        e_velocity = (DVLserialPacket[12]<<8)+DVLserialPacket[11]
        
        beam_sensor_1 = (DVLserialPacket[14]<<8)+DVLserialPacket[13]
        beam_sensor_2 = (DVLserialPacket[16]<<8)+DVLserialPacket[15]
        beam_sensor_3 = (DVLserialPacket[18]<<8)+DVLserialPacket[17]
        beam_sensor_4 = (DVLserialPacket[20]<<8)+DVLserialPacket[19]
        
        bottom_status = DVLserialPacket[21]
        
        velocity_1 = (DVLserialPacket[23]<<8)+DVLserialPacket[22]
        velocity_2 = (DVLserialPacket[25]<<8)+DVLserialPacket[24]
        velocity_3 = (DVLserialPacket[27]<<8)+DVLserialPacket[26]
        velocity_4 = (DVLserialPacket[29]<<8)+DVLserialPacket[28]
        
        ref_layer_start = (DVLserialPacket[31]<<8)+DVLserialPacket[30]
        ref_layer_end = (DVLserialPacket[33]<<8)+DVLserialPacket[32]
        ref_layer_status = DVLserialPacket[34]
        
        tofp_hour = DVLserialPacket[35]
        tofp_minute = DVLserialPacket[36]
        tofp_second = DVLserialPacket[37]
        tofp_error = DVLserialPacket[38]
        
        bit_result = (DVLserialPacket[40]<<8)+DVLserialPacket[39]
        speed_of_sound = (DVLserialPacket[42]<<8)+DVLserialPacket[41]
        temperature = (DVLserialPacket[44]<<8)+DVLserialPacket[43]
        salinity = DVLserialPacket[45]

        depth = (DVLserialPacket[47]<<8)+DVLserialPacket[46]
        pitch = (DVLserialPacket[49]<<8)+DVLserialPacket[48]
        roll = (DVLserialPacket[51]<<8)+DVLserialPacket[50]
        yaw = (DVLserialPacket[53]<<8)+DVLserialPacket[52]

        distance_east = (DVLserialPacket[57]<<24)+(DVLserialPacket[56]<<16)+(DVLserialPacket[55]<<8)+DVLserialPacket[54]
        distance_north = (DVLserialPacket[61]<<24)+(DVLserialPacket[60]<<16)+(DVLserialPacket[59]<<8)+DVLserialPacket[58]
        distance_up = (DVLserialPacket[65]<<24)+(DVLserialPacket[64]<<16)+(DVLserialPacket[63]<<8)+DVLserialPacket[62]
        distance_error = (DVLserialPacket[69]<<24)+(DVLserialPacket[68]<<16)+(DVLserialPacket[67]<<8)+DVLserialPacket[66]

        water_mass_east = (DVLserialPacket[73]<<24)+(DVLserialPacket[72]<<16)+(DVLserialPacket[71]<<8)+DVLserialPacket[70]
        water_mass_north = (DVLserialPacket[77]<<24)+(DVLserialPacket[76]<<16)+(DVLserialPacket[75]<<8)+DVLserialPacket[74]
        water_mass_up = (DVLserialPacket[81]<<24)+(DVLserialPacket[80]<<16)+(DVLserialPacket[79]<<8)+DVLserialPacket[78]
        water_mass_error = (DVLserialPacket[85]<<24)+(DVLserialPacket[84]<<16)+(DVLserialPacket[83]<<8)+DVLserialPacket[82]
        
        checksum = (DVLserialPacket[87]<<8)+DVLserialPacket[86]

    def PD5datalist(self, PD5packet):
        
        return Datalist[ PD5packet.dvl_id_word, 
                         PD5packet.format_byte, 
                         PD5packet.number_of_bytes, 
                         PD5packet.sys_config,
                         PD5packet.x_velocity,
                         PD5packet.y_velocity,
                         PD5packet.z_velocity,
                         PD5packet.e_velocity,
                         PD5packet.beam_sensor_1,
                         PD5packet.beam_sensor_2,
                         PD5packet.beam_sensor_3,
                         PD5packet.beam_sensor_4,
                         PD5packet.bottom_status,
                         PD5packet.velocity_1,
                         PD5packet.velocity_2,
                         PD5packet.velocity_3,
                         PD5packet.velocity_4,
                         PD5packet.ref_layer_start,
                         PD5packet.ref_layer_end,
                         PD5packet.ref_layer_status,
                         PD5packet.tofp_hour,
                         PD5packet.tofp_minute,
                         PD5packet.tofp_second,
                         PD5packet.tofp_error,
                         PD5packet.bit_result,
                         PD5packet.speed_of_sound,
                         PD5packet.temperature,
                         PD5packet.salinity,
                         PD5packet.depth,
                         PD5packet.pitch,
                         PD5packet.roll,
                         PD5packet.yaw,
                         PD5packet.distance_east,
                         PD5packet.distance_north,
                         PD5packet.distance_up,
                         PD5packet.distance_error,
                         PD5packet.water_mass_east,
                         PD5packet.water_mass_north,
                         PD5packet.water_mass_up,
                         PD5packet.water_mass_error,
                         PD5packet.checksum]
                         
        


