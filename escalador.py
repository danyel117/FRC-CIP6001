#!/usr/bin/env python3

import wpilib

class MyRobot(wpilib.IterativeRobot):
    '''Main robot class'''
    
    def robotInit(self):
        '''Robot-wide initialization code should go here'''

        self.lstick = wpilib.Joystick(0)

        self.motor_D1 = wpilib.Victorsp(1)
        self.motor_I1 = wpilib.Victorsp(2)
        self.G_motor=wpilib.SpeedControllerGroup(self.motor_D1, self.motor_I1)
       
        self.robotdrive = wpilib.drive.differentialdrive(self.motor_D1, self.motor_I1)
        #self.ultrasound1 = wpilib.ultrasonic(1,2,1)
        #self.ultrasound1.SetAutomaticMode(True)

        #self.ultrasound2 = wpilib.ultrasonic(3,4,1)
        #self.ultrasound2.SetAutomaticMode(True)


        #motor_d1 y motor_d2 son los motores de la caja de reducción 
        ##ultrasound1 frontal es el sensor us que se usa para detectar la barra pegada a pared mientras ultrasound2 es el que se usa para saber qué tan arriba esta el robot mientras escala.

    def autonomousInit(self):
        '''Called only at the beginning of autonomous mode'''
        pass

    def autonomousPeriodic(self):
        '''Called every 20ms in autonomous mode'''
        pass

    def disabledInit(self):
        '''Called only at the beginning of disabled mode'''
        pass
    
    def disabledPeriodic(self):
        '''Called every 20ms in disabled mode'''
        pass

    def teleopInit(self):
        '''Called only at the beginning of teleoperated mode'''
        pass

    def teleopPeriodic(self):
        '''Called every 20ms in teleoperated mode'''

        #Prob will use PS4, XBOX or Joystic

        while self.isOperatedControl() and self.isEnabled():
            if self.lstick.getRawButton(Joystick["R2"]):
                self.G_motor.set(1)
            if self.lstick.getRawButton(Joystick['cualquier boton']):
            #if self.lstick.Get("boton") Button(("Controller") ["Boton 2"]):
                self.G_motor.setInverted(0.5)                                   
                
                #Despues de que se encuentre la distancia en mm hacia la barra y se avanzan 5 cm 
                    #Bajar dos garras para anclarse a la barra para recojer el sistema interno del sistema telescópico


if __name__ == '__main__':
    wpilib.run(MyRobot)




