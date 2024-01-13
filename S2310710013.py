__doc__ = "Python Coding Assignmant from VCVD WS2023/2024, Gusenbauer Daniela"

#import system libs
import argparse
import math
import matplotlib.pyplot as plt
import numpy as np

#Paramter
gravity = -9.81  #m/s²#Parameter fix:  Gravitational acceleration
kmh_to_ms=3.6 #Conversion factor km/h zu m/s

#==============
#Method for calculating the braking distance, Comparison to rule of thump
def Calculation():
  Calculation.__doc__ ="Berechnugn des Bremsweges und Zeit"
  velocity_ms= cmd_call_args_.velocity/kmh_to_ms #Convert k/m to m/s
  angle = math.radians(cmd_call_args_.incline)  #Convert degrees to radians
  #Pysik Model Calculations
  anglefunk=cmd_call_args_.friction*math.cos(angle)+math.sin(angle)
  brakeway= -velocity_ms**2/(2*gravity*abs(anglefunk))

  #Rule of thump
  distance_k=cmd_call_args_.velocity/10
  distance_stop=distance_k**2+distance_k*3
  distance_danger=(distance_k**2)/2+distance_k*3

  #Outout Comparison
  print("\nComparison Calcuation to the rule of thump:")
  print("Brakeway calculation",round(brakeway,2), "m")
  print("Distance stop",round(distance_stop,2), "m")
  print("Distance danger",round(distance_danger,2), "m")
#===============

#================================================
#Methode zur Erstellung der Diagramme 1;Velocity\time 2;Distance\time
#based on
#source:
#https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/
#and Excample Prof. Altinger
def Generateplots(file_name_out):
  Generateplots.__doc__="Creation  diagrams Velocity\time, Distance\time"
  angle = math.radians(cmd_call_args_.incline) #Convert degrees to radians
  #Calculation time and deceleration
  #anglefunktion of brackets for calculations
  anglefunk=cmd_call_args_.friction*math.cos(angle)+math.sin(angle)
  #Time wenn the Velocity =0
  time_end=-(cmd_call_args_.velocity/kmh_to_ms)/(gravity*(abs(anglefunk)))
  acceleration= gravity*(abs(anglefunk))

  #define figure
  fig = plt.figure()
  #1;Velocity\time
  velocity_to_time = fig.add_subplot(2,1,1) #add plot 1
  #data
  time = np.arange(0.0, time_end, 0.01)
  #Unit: m/s= km/h + m/s²*s*kmh_to_ms (-> km/h)
  veleocity_t = cmd_call_args_.velocity+acceleration*time*kmh_to_ms
  #define plots
  velocity_to_time.plot(time, veleocity_t, color ="green", lw = 2)
  #add axis label
  velocity_to_time.set_xlabel("time [s]")
  velocity_to_time.set_ylabel("velocity [km/h]")
  velocity_to_time.set_title("veleocity/time", fontweight ="bold")
  velocity_to_time.grid(1)

  #2;Distance\time
  distance_per_time = fig.add_subplot(2,1,2) #add plot 2
  #data
  #Unit:m(s)= km/h /kmh_to_ms (->m/s) *s+ m/s²*s²
  distance_t = cmd_call_args_.velocity/kmh_to_ms*time+1/2*acceleration*(time**2)
  #define plots
  distance_per_time.plot(time, distance_t, color ="red", lw = 2)
  #add axis label
  distance_per_time.set_xlabel("time [s]")
  distance_per_time.set_ylabel("distance [m]")
  distance_per_time.set_title("distance/time", fontweight ="bold")
  distance_per_time.grid(1)
  #No overlapping of the diagrams
  plt.tight_layout()
  #export as PDF
  plt.savefig(file_name_out)
#================================================

#setup arg parser - Read parameters from the terminal
arg_parser_ = argparse.ArgumentParser(description="Imput variables calculation")
arg_parser_.add_argument("--mass", type=float, help="[kg] mass of the vehicle")
arg_parser_.add_argument("velocity", type=float, help="[k/h] velocity (<=0)")
arg_parser_.add_argument("friction", type=float, help="roadfriction (<=0)")
arg_parser_.add_argument("--incline", type=float, help="[°]incline of the road")
cmd_call_args_ = arg_parser_.parse_args()

#Check whether entries are correct
if cmd_call_args_.velocity <= 0 or cmd_call_args_.friction <= 0:
  print("velocity and friction are not allowed to be below 0")
else:
  #if correct - Start calculation and output  print("Eingaben:")
  print("velocity ",cmd_call_args_.velocity, "km/h")
  print("friction ",cmd_call_args_.friction)
  print("mass ",cmd_call_args_.mass, "kg")
  print("incline ",cmd_call_args_.incline,"°")
  Calculation() #Compare Calc to Rule
  Generateplots("ResultsPlots.pdf") #Plots
