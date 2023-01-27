#!/usr/bin/env python3

import os
import subprocess
#import pandas as pd
from datetime import datetime, date, time
#from pandas.core.reshape.concat import concat

def mainMenu():
    print('')
    print('#'*48)
    print('[1] Cylance - Data Pull')
    print('[2] Rapid7 - Data Pull')
    print('[3] N-Able - Data Pull')
    print('[4] AD - Data Pull')
    print('[5] Solarwinds - Device Data Pull')
    print('[6] Solarwinds - Ticket Data Pull')
    print('')
    print('[7] Cylance - Data Manipulation')
    print('[8] Rapid7 - Data Manipulation')
    print('[9] N-Able - Data Manipulation')
    print('[10] AD - Data Manipulation')
    print('[11] Solarwinds - Device Data Manipulation')
mainMenu()

def option1():
	subprocess.run(["powershell", "cylance.ps1"])
def option2():
    subprocess.run(["powershell", "rapid7.ps1"])
def option3():
    subprocess.run(["powershell", "nable.ps1"])
def option4():
    subprocess.run(["powershell", "ad.ps1"])
def option5():
    subprocess.run(["powershell", "solarwinds-device.ps1"])
def option6():
    subprocess.run(["powershell", "solarwinds-ticket.ps1"])
def option7():
    subprocess.run(["python", "cylance.py"])
def option8():
    subprocess.run(["python", "rapid7.py"])
def option9():
    subprocess.run(["python", "nable.py"])
def option10():
    subprocess.run(["python", "ad.py"])
def option11():
    subprocess.run(["python", "solarwinds-device.ps1"])
def option12():
    subprocess.run(["python", "solarwinds-ticket.ps1"])

def runit():
    option = ''
    try:
        option = input('Enter Option: ')
    except:
        print('Error, enter a number.')
    if option == '1':
        option1()
    elif option == '2':
        option2()
    elif option == '3':
        option3()
    elif option == '4':
        option4()
    elif option == '5':
        option5()
    elif option == '6':
        option6()
    elif option == '7':
        option7()
    elif option == '8':
        option8()
    elif option == '9':
        option9()
    elif option == '10':
        option10()
    elif option == '11':
        option11()
    else:
        print('Done.')
        exit()
runit()