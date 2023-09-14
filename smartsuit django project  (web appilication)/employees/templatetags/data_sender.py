from django import template
import serial
import time
import schedule

register = template.Library()


@register.simple_tag()
def main_func():
    list_values = []
    list_in_floats = []
    arduino = serial.Serial('com3', 9600)
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')

    for item in list_values:
        list_in_floats.append(float(item))

    return list_in_floats

    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
