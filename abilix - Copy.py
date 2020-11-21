"""
Created on Mon Dec  9 18:42:53 2019

@author: aaron
"""
'''
documentation

initialize() - starts the robot
startmotor(distance) - moves forward in a specific distance in milimeters
leftlineturn(lturnspeed) - turns left after detection by linefollow
rightlineturn(lturnspeed) - turns right after detection by linefollow
turnleft(degree) - turn to a specified degree to the left
turnright(degree) - turn to a specified degree to the right
lineturn(Lspeed,Rspeed) - turn after linefollow detection
linefollow(inter=t,l,r) - detects either one of the three types of intersection
motor(motor,power) - motor = motor# - power = strength of motor
wait(time) - amount of time the robot will remain not moving
stopmotor() - turn off all moving motors
time(distance) - amount of distance it will follow the line
end() - finishes the program
clear() - clears the file you wrote
clipboard() - copies program to clipboard for WIN 
motordeg(port, direction, degree) - turns the motor to a certiain degree 

'''

import pyperclip
import os 


def initialize():
    global name
   
    f = open(name, "a+")
    f.write(""" #include "ASEIO.h" \n""")
    f.write("void main()\n")
    f.write("{\n")
    f.write("    WER_InitRobot_5(0,1.000000,1,1.000000,0,1,2,3,4,1);\n")
        
        
def startmotor(distance):
    global name 
    f = open(name, "a+")
    
    time = distance/475
    f.write('    WER_SetMotor(50,50,\t')
    f.write(str(time))
    f.write(');\n')

def nstartmotor(distance):
    global name 
    f = open(name, "a+")
    
    time = distance/475
    f.write('    WER_SetMotor(-50,-50,\t')
    f.write(str(time))
    f.write(');\n')
    
        
def leftlineturn():
    global name 
    f = open(name, "a+") 
    f.write("    WER_Around(\t")
    f.write(str(-30))
    f.write(",\t")
    f.write(str(30))
    f.write(",\t")
    f.write("0);\n")

def rightlineturn():
    global name 
    f = open(name, "a+") 
    f.write("    WER_Around(\t")
    f.write(str(30))
    f.write(",\t")
    f.write(str(-30))
    f.write(",\t")
    f.write("0);\n")

def turnleft(degree):
    global name 
    f = open(name , "a+") 
    degree1 = 0.0067
    degree2 = degree1*degree
    f.write('    WER_SetMotor(-30,30,\t')
    f.write(str(degree2))
    f.write(');\n')

def turnright(degree):
    global name 
    f = open(name, "a+") 
    degree1 = 0.0067
    degree2 = degree1*degree
    f.write('    WER_SetMotor(30,-30,\t')
    f.write(str(degree2))
    f.write(');\n')
        
def linefollow(inter):
    global name 
    f = open(name, "a+") 
    if "t" in inter:
        f.write("    WER_LineWay_C(50,15,0.2);\n")
       
        
    elif "r" in inter:
        f.write("    WER_LineWay_C(50,5,0.2);\n")
       
        
    elif "l" in inter:
        f.write("    WER_LineWay_C(50,1,0.2);\n")

def button():
    global name 
    f = open(name, "a+") 
    f.write("    WER_next();\n")

def motor(motor=1,power=30):
    global name 
    f = open(name , "a+") 
    f.write("    SetMoto(\t")
    f.write(str(motor))
    f.write(",\t")
    f.write(str(power))
    f.write(");\n")

def wait(time):
    global name 
    f = open(name, "a+") 
    f.write("    wait(\t")
    f.write(str(time))
    f.write(");\n")

def stopmotor():
    global name 
    f = open(name, "a+") 
    f.write("    SetMoto(1,0);\n")
    f.write("    SetMoto(0,0);\n")
    f.write("    SetMoto(2,0);\n")
    f.write("    SetMoto(3,0);\n")

def time(distance):
    time = distance/475
    global name 
    f = open(name, "a+") 
    f.write("    WER_LineWay_T(50,\t")
    f.write(str(time))
    f.write(");\n")

def motordeg(port, direction, degree):
    global name
    time = degree*(1/400)
    f = open(name, "a+")
    if direction == "r":
        motor(port,30)
        wait(time)
        stopmotor()

    elif direction =="l":
        motor(port,-30)
        wait(time)
        stopmotor()
        

def end():
    global name 
    f = open(name , "a+") 
    f.write("}\n")

def clear():
    global name 
    f = open(name, "w+")
    f.write("")

def clipboard():
    global name
    f = open(name, "r")
    content = f.read()
    pyperclip.copy(content)



###############################################
def loc1():
    global name 
    startmotor(100)
    linefollow("l")
    leftlineturn()
    linefollow("r")
    startmotor(200)
    time(80)
    leftlineturn()
    time(200)

def loc2():
    global name 
    startmotor(100)
    linefollow("l")
    leftlineturn()
    linefollow("r")
    turnleft(30)
    startmotor(300)
    time(400)

def loc3():
    startmotor(100)
    linefollow("l")
    leftlineturn()
    linefollow("r")
    startmotor(200)
    time(80)
    time(240)

def loc4(): # start from back of the box 
    global name
    startmotor(150)
    linefollow("l")
    leftlineturn()
    linefollow("l")
    leftlineturn()
    linefollow("l")
    time(230)
    
    

def loc5():
    global name
    startmotor(150)
    linefollow("l")
    leftlineturn()
    linefollow("r")
    rightlineturn()
    linefollow("l")

def loc6():
    global name
    startmotor(150)
    linefollow("l")
    linefollow("l")
    leftlineturn()

def loc7():
    global name
    startmotor(150)
    linefollow("l")
    linefollow("l")
    linefollow("l")
    leftlineturn()
    time(110)

def loc8():
    global name
    startmotor(150)
    linefollow("l")
    linefollow("l")
    linefollow("l")
    linefollow("l")
    leftlineturn()

def loc9():
    global name
    startmotor(150)
    linefollow("l")
    linefollow("l")
    linefollow("l")
    linefollow("l")
    time(130)
    

def loc10back():
    startmotor(100)
    linefollow("l")
    linefollow("l")
    leftlineturn()
    time(100)
    turnleft(90)
    wait(1)
    turnleft(80)
    startmotor(90)
    end()

def loc10front():
    global name
    startmotor(150)
    linefollow("l")
    rightlineturn()
    linefollow("t")
    turnleft(90)
    startmotor(350)
    leftlineturn()

def loc10right():
    global name
    startmotor(150)
    linefollow("l")
    linefollow("l")
    linefollow("l")
    linefollow("l")
    wait(0.3)
    nstartmotor(50)
    wait(0.3)
    turnright(90)
    startmotor(90)



       

       



