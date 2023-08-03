#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String
import Tkinter as tk
import time
message = " "
color_pub = rospy.Publisher("/color", String, queue_size=10)
class TrafficLight:
    def __init__(self, root):
        self.root = root
        #self.root2 = root2
        self.current_color = "red"
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=150, height=350)
        self.canvas.pack()

        self.red_light = self.canvas.create_oval(50, 50, 100, 100, fill="red", outline="")
        self.yellow_light = self.canvas.create_oval(50, 150, 100, 200, fill="gray", outline="")
        self.green_light = self.canvas.create_oval(50, 250, 100, 300, fill="gray", outline="")

        self.canvas2 = tk.Canvas(self.root, width=500, height=350)
        self.canvas2.pack()

        self.blue_light_peaton = self.canvas2.create_oval(50, 50, 100, 100, fill="blue", outline="")
        self.red_light_peaton = self.canvas2.create_oval(50, 150, 100, 200, fill="gray", outline="")


    def change_light(self, color):
        if color == "red":
            self.canvas.itemconfig(self.red_light, fill="red")
            self.canvas.itemconfig(self.yellow_light, fill="gray")
            self.canvas.itemconfig(self.green_light, fill="gray")
            self.current_color = "red"

        elif color == "yellow":
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
            self.canvas.itemconfig(self.green_light, fill="gray")
            self.canvas.itemconfig(self.red_light, fill="gray")
            self.current_color = "yellow"
        elif color == "green":
            self.canvas.itemconfig(self.green_light, fill="green")
            self.canvas.itemconfig(self.red_light, fill="gray")
            self.canvas.itemconfig(self.yellow_light, fill="gray")
            self.current_color = "green"
        
        elif color == "apagado_p":
            self.canvas2.itemconfig(self.blue_light_peaton, fill="gray")
            
        elif color == "apagado":
            self.canvas.itemconfig(self.green_light, fill="gray")
            self.canvas.itemconfig(self.red_light, fill="gray")
            self.canvas.itemconfig(self.yellow_light, fill="gray")
            self.current_color = "no color"

        elif color =="blue":
            self.canvas2.itemconfig(self.blue_light_peaton, fill="blue")
            self.canvas2.itemconfig(self.red_light_peaton, fill="gray")

        elif color =="red_p":
            self.canvas2.itemconfig(self.blue_light_peaton, fill="gray")
            self.canvas2.itemconfig(self.red_light_peaton, fill="red")
        
        




# Create the main window
root = tk.Tk()
#root2 = tk.Tk()
root.title("Traffic Light")
#root2.title("Peaton")
traffic_light = TrafficLight(root)
def signal_cb(msg):
    global message, traffic_light,color_pub

    message = msg.data
    color_pub.publish("red")
        # tiempo en verde 5seg
    for i in range(0, 5):        
        traffic_light.change_light("green")
        traffic_light.change_light("red_p")
        time.sleep(1)
    
    # cambio de verde a amarillo (dos parpadeos)
    for i in range(0, 2):
            traffic_light.change_light("apagado")
            time.sleep(0.5)
            traffic_light.change_light("green")
            time.sleep(0.5)

    # amarillo
    for i in range(0,2):
        traffic_light.change_light("yellow")
        time.sleep(1)

    if (message == "Normal"):
        color_pub.publish("blue")
        cont = 7
        print("Se estiman pocos peatones en la zona")
        # tiempo en peaton 7seg

        for i in range(0,5):
            traffic_light.change_light("red")
            traffic_light.change_light("blue")
            
            if cont > 2:
                print(cont)
                cont = cont - 1
            time.sleep(1)
        for i in range(0, 3):
            print(cont)
            cont = cont - 1

            traffic_light.change_light("apagado_p")
            time.sleep(0.5)
            traffic_light.change_light("blue")
            time.sleep(0.5)

    elif (message == "Mid"):
        color_pub.publish("blue")
        # tiempo en peaton 15seg
        cont = 15
        print("Se estiman algunos peatones en la zona")

        for i in range(0,13):
            traffic_light.change_light("red")
            traffic_light.change_light("blue")
            
            if cont > 2:
                print(cont)
                cont = cont - 1
            time.sleep(1)
        for i in range(0, 3):
            print(cont)
            cont = cont - 1

            traffic_light.change_light("apagado_p")
            time.sleep(0.5)
            traffic_light.change_light("blue")
            time.sleep(0.5)
    
    elif (message == "Mucho"):
        color_pub.publish("blue")
        # tiempo en peaton 20seg
        cont = 20
        print("Se estiman muchos peatones en la zona")

        for i in range(0,18):
            traffic_light.change_light("red")
            traffic_light.change_light("blue")
            
            if cont > 2:
                print(cont)
                cont = cont - 1
            time.sleep(1)
        for i in range(0, 3):
            print(cont)
            cont = cont - 1

            traffic_light.change_light("apagado_p")
            time.sleep(0.5)
            traffic_light.change_light("blue")
            time.sleep(0.5)

    elif (message == "Disc"):
        color_pub.publish("blue")
        
        signal = ""

        
        traffic_light.change_light("red")
        traffic_light.change_light("blue")

        signal = raw_input("Si la persona discapacitada termino de cruzar, escriba si: ")
        for i in range(0, 3):
            
            traffic_light.change_light("apagado_p")
            time.sleep(0.5)
            traffic_light.change_light("blue")
            time.sleep(0.5)

def main():
    global message
    rospy.init_node("semaforo")
    rospy.loginfo("Node initiated")
    rospy.Subscriber("/signal",String, signal_cb)

    while not rospy.is_shutdown():
        # Create three circles with different colors

        root.mainloop()
        #root2.mainloop()


if __name__ == "__main__":
    main()