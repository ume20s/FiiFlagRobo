#! /usr/bin/env python
import webiopi
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

RightHand = 0
RightLeg = 1
LeftHand = 2
LeftLeg = 3
R1 = 110
R2 = 60
L1 = 60
L2 = 110

def m_deg(deg):
    pulse = int((650-150)*deg/180+150)
    return pulse

def setup():
    pwm.set_pwm(RightHand, 0, m_deg(110))
    pwm.set_pwm(LeftHand, 0, m_deg(60))
    pwm.set_pwm(RightLeg, 0, m_deg(90))
    pwm.set_pwm(LeftLeg, 0, m_deg(90))
    time.sleep(2)

def loop():
    pwm.set_pwm(RightLeg, 0, m_deg(R1))
    pwm.set_pwm(LeftLeg, 0, m_deg(L1))
    time.sleep(0.1)
    pwm.set_pwm(RightLeg, 0, m_deg(R2))
    pwm.set_pwm(LeftLeg, 0, m_deg(L2))
    time.sleep(0.1)


@webiopi.macro
def MoveHand( Pos, Ang ):
    pwm.set_pwm(int(Pos), 0, m_deg(int(Ang)))
