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
time() - amount of time it will follow the line
end() - finishes the program
clear() - clears the file you wrote
clipboard() - copies program to clipboard for WIN 
clipboardOS() - copies program to clipboard for OSX

'''

import pyperclip
import os 


def initialize():
    global name
   
    f = open(name, "a+")
    f.write(""" #include"ASEIO.h" \n""")
    f.write("void main()\n")
    f.write("{\n")
    f.write("    WER_Init_5(0,1.000000,1,1.000000,0,1,2,3,4,1;)\n")
        
        
def startmotor(distance):
    global name 
    f = open(name, "a+")
    
    time = distance/4750
    f.write('    WER_SetMotor(50,50,\t')
    f.write(str(time))
    f.write(');\n')
        
def leftlineturn(lturnspeed):
    global name 
    f = open(name, "a+") 
    f.write("    WER_LTurn(\t")
    f.write(str(lturnspeed))
    f.write(");\n")

def rightlineturn(lturnspeed):
    global name 
    f = open(name , "a+") 
    f.write("    WER_RTurn(\t")
    f.write(str(lturnspeed))
    f.write(");\n")

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
            
def lineturn(Lspeed=30, Rspeed=-30):
    global name 
    f = open(name, "a+") 
    f.write("    WER_Around(\t")
    f.write(str(Lspeed))
    f.write(",\t")
    f.write(str(Rspeed))
    f.write(",\t")
    f.write("0);\n")
        
def linefollow(inter="t"):
    global name 
    f = open(name, "a+") 
    if "t" in inter:
        f.write("    WER_LineWay_C(50,15,0.1);\n")
       
        
    elif "r" in inter:
        f.write("    WER_LineWay_C(50,5,0.1);\n")
       
        
    elif "l" in inter:
        f.write("    WER_LineWay_C(50,1,0.1);\n")

def button():
    global name 
    f = open(name, "a+") 
    f.write("    WER_next()\n")

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

def time(time):
    global name 
    f = open(name, "a+") 
    f.write("    WER_LineWay_T(50,\t")
    f.write(str(time))
    f.write(");\n")

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
    f = open(name, "a+").readlines()
    pyperclip.copy(f)

def clipboardOS():
    global name 
    f = open(name, "a+").readlines()
    os.system("echo '%s' | pbcopy" % f)


    



    






'''
def move(initial_coordinate=[],
         destination_coordinate=[]):

    obstacle0=[0,0,0,0]
    obstacle1=[0,0,0,0]
    obstacle2=[0,0,0,0]
    obstacle3=[0,0,0,0]
    obstacle4=[0,0,0,0]
    obstacle5=[0,0,0,0]
    obstacle6=[0,0,0,0]
    
    all_obstacle = [obstacle0, obstacle1, obstacle2, obstacle3,
                    obstacle4, obstacle5, obstacle6]

    car_length = 100
    car_width = 100

    x_movement = destination_coordinate[0] - initial_coordinate[0]
    y_movement = destination_coordinate[1] - initial_coordinate[1]

    x_path = []
    y_path = []

    x_overlap = False
    y_overlap = False 

    for x_loc in range(initial_coordinate[0], destination_coordinate[0]):
        x_path.append(x_loc)

    for y_loc in range(initial_coordinate[1], destination_coordinate[1]):
        y_path.append(y_loc)


    for x_coor in x_path:
        for obstacle_coor_ in all_obstacle:
            if x_coor == obstacle_coor[0]:
                x_overlap = True 
                
            elif  x_coor == obstacle_coor[2]:              
                x_overlap = True

            else:
                pass

    for y_coor in y_path:
        for obstacle_coor in all_obstacle:
            if y_coor == obstacle_coor[1]:
                y_overlap = True 
                
            elif y_coor == obstacle_coor[3]:              
                y_overlap = True

            else:
                pass
'''
    

    

     
        
        
        
    
    
       
       
       

       



