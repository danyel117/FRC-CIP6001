import smbus2 as smbus
import time

class pixy():

    def getBlocks(signature):
        bus = smbus.SMBus(1)
        pixy=0x54
        data=[174,193,32,2,255,1]
        bus.write_i2c_block_data(pixy,0,data)
        time.sleep(0.05)
        res=bus.read_i2c_block_data(pixy, 0, 18)
        if res[6]+255*res[7]==signature:
            return {'s':signature,'x':res[8]+255*res[9],'y':res[10]+255*res[11],'w':res[12]+255*res[13],'h':res[14]+255*res[15]}

    def setLamp(status):
        bus = smbus.SMBus(1)
        pixy=0x54
        data=[174,193,22,2,status,0]
        bus.write_i2c_block_data(pixy,0,data)	
