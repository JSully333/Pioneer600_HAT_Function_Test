#!/usr/bin/python
# -*- coding:utf-8 -*-
#Code had been changed to work as a module for other programs also.
#Ensure that 1-wire is Enables in raspi-config, under Interfaces.
import os
import glob
import time



base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
def read_rom():
	name_file=device_folder+'/name'
	f = open(name_file,'r')
	return f.readline()

def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		temp_f = temp_c * 9.0 / 5.0 + 32.0
		return temp_c, temp_f

if __name__ == "__main__":
        print(' rom: '+ read_rom())
        while True:
                print(' C=%3.3f  F=%3.3f'% read_temp())
                time.sleep(1)
