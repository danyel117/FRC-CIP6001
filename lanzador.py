import wpilib
import wpilib.drive	
controlJoystick={'lanzar':1,'derecha':2,'izquierda':3, }
class MyRobot (wpilib.SampleRobot):
    def robotInit (self):
     	self.motor_RuedaCentral=wpilib.VictorSP()
        self.motor_RuedasLanzamiento=wpilib.VictorSP()
        self.FinalCarrera=wpilib.DigitalInput()#poner el canal 0-9)
        self.lstick=wpilib.Joystick()#poner el valor del joystick)
  
    def operatorControl(self):
               '''Called when operation control mode is enabled'''
        timer = wpilib.Timer()
        timer.start()
        
        while self.isOperatorControl() and self.isEnabled():

            if self.FinalCarrera.get() == False:	
                self.motor_RuedaCentral.set(0.2)
            else:
                self.motor_RuedaCentral.set(0)

            if self.lstick.getRawButtonPressed(controlJoystick['lanzar']):
                self.motor_RuedasLanzamiento.set(1)  
      




                    
   
def autonomous (self):
    



