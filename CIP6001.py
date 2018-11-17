
import time
import wpilib

def getBlocks(signature):
    address=0x54
    bus = wpilib.I2C(wpilib.I2C.Port.kOnboard,address)
    data=[174,193,32,2,255,1]
    bus.writeBulk(data)
    time.sleep(0.05)
    res=bus.read(address, 18)
    if res[6]+255*res[7]==signature:
        return {'s':signature,'x':res[8]+255*res[9],'y':res[10]+255*res[11],'w':res[12]+255*res[13],'h':res[14]+255*res[15]}

def setLamp(status):
    bus =wpilib.I2C(wpilib.I2C.Port.kOnboard,4)
    adddress=0x54
    data=[174,193,22,2,status,0]
    bus.writeBulk(adddress,data)	

