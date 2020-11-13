# Abilix-Python
Creates a text file containing VJC c-based language 
Only Tested on the default Abilix Car model 

# documentation

initialize() - starts the robot

startmotor(distance) - moves forward in a specific distance in milimeters

leftlineturn(lturnspeed) - turns left after detection by linefollow

rightlineturn(lturnspeed) - turns right after detection by linefollow

turnleft(degree) - turn to a specified degree to the left

turnright(degree) - turn to a specified degree to the right

lineturn(Lspeed,Rspeed) - turn after linefollow detection

linefollow(inter="t,l,r") - detects either one of the three types of intersection

motor(motor,power) - motor = motor# - power = strength of motor

wait(time) - amount of time the robot will remain not moving

stopmotor() - turn off all moving motors

time() - amount of time it will follow the line

end() - finishes the program

clear() - clears the file you wrote

clipboard() - copies program to clipboard for WIN

clipboardOS() - copies program to clipboard for OSX


