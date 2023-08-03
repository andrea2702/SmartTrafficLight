#!/usr/bin/env python

import rospy
import numpy as np
import random
from std_msgs.msg import String
import time


randInt = 0

if __name__== '__main__':
    rospy.init_node("signal")
    rospy.loginfo("Node initiated")

    signal_pub = rospy.Publisher("/signal", String, queue_size=10)

    


    while not rospy.is_shutdown():
        
      
        
        

        if(randInt == 1):
            print("Muchos peatones")
            randInt = randInt + 1
            signal_pub.publish("Mucho")
        elif(randInt == 3):
            print("Algunos Peatones")
            randInt = randInt + 1
            signal_pub.publish("Mid")
        elif(randInt == 2):
            print("persona con discapacidad detectada")
            randInt = randInt + 1
            signal_pub.publish("Disc")

        else:
            print("Pocos Peatones")
            signal_pub.publish("Normal")
            randInt = randInt +1

        signal = raw_input("")
        

        
        
       
        

