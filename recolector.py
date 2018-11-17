import wpilib
from wpilib.drive import DifferentialDrive
controldeldriver={'B1':0}
class MyRobot(wpilib.SampleRobot):
   '''Main robot class'''
  
   def robotInit(self):     
        self.lstick = wpilib.Joystick(1)
        self.motor1 = wpilib.VictorSP(1)
      
   def disabled(self):
       '''Called when the robot is disabled'''
       while self.isDisabled():
           wpilib.Timer.delay(0.01)

   def autonomous(self):
       '''Called when autonomous mode is enabled'''
      
       while self.isAutonomous() and self.isEnabled():
           wpilib.Timer.delay(0.01)

   def operatorControl(self):
       '''Called when operation control mode is enabled'''
        timer = wpilib.Timer()
        timer.start()
        while self.isOperatorControl() and self.isEnabled():
	        if self.lstick.getRawButton(0):
			    self.motor1.set(1)
        
        wpilib.Timer.delay(0.02)

if __name__ == '__main__':
   wpilib.run(MyRobot)

