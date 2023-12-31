#Its simply program to test OPC UA Client on local machine

from time import sleep
import random
from opcua import Server

server = Server()

#Create server for local use
#Init
server.set_endpoint("opc.tcp://127.0.0.1:12345")
server.register_namespace("Room1")
objects = server.get_objects_node()
tempsens = objects.add_object('ns=2;s="TS1"', "Temperature Sensor 1")
tempsens.add_variable('ns=2;s="TS1_VendorName"', "TS1 Vendor Name", "Sensor King")
tempsens.add_variable('ns=2;s="TS1_SerialNumber"', "TS1 Serial Number", 12345678)
temp = tempsens.add_variable('ns=2;s="TS1_Temperature"', "TS1 Temperature", 20)
bulb = objects.add_object(2, "Light Bulb")
state = bulb.add_variable(2, "State of Light Bulb", False)
state.set_writable()
temperature = 20.0

#Main Loop
try:
    print("Start Server")
    server.start()
    print("Server Online")
    while True:
        temperature += random.uniform(-1, 1)
        temp.set_value(temperature)
        print("New Temperature: " +str(temp.get_value()))
        print("State of Light bulb: " +str(state.get_value()))
        sleep(2)     
finally:
    server.stop()
    print("Server Offline")
        
