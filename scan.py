#!/usr/bin/env python
# coding: utf-8
import os, re, requests, json, urllib, random, sys
from time import sleep, strftime, localtime
from bs4 import BeautifulSoup as sop
from requests.exceptions import ConnectionError as legh

# Recode Tidak Membuatmu Menjadi Mastah :D

bl = '\033[0;34m' #  Blue
dg = '\033[1;30m' # darkgrey
lb = '\033[1;34m' # lightblue
lg = '\033[1;32m' # lightgreen
lc = '\033[1;36m' # lightcyan
lr = '\033[1;31m' # lightred
lp = '\033[1;35m' # lightpurple
yw = '\033[1;33m' #  yellow
wh = '\033[1;37m' #  white
no = '\033[0m'
bold = '\033[1m'
under = '\033[4m'

def banner():
   print(yw+"|  | |\  | | \    / "+bold+wh+"| "+lg+"Tools Scan Proxy Universitas")
   print(yw+"|  | | \ | |  \  /  "+bold+wh+"| "+lg+"Avaliable Version 0.5")
   print(yw+"\__/ |  \| |   \/   "+bold+wh+"| "+lg+"Created By Kang Ngulik\n"+wh)

def pas1():
   os.system('clear')
   os.system('touch pas.txt')
   wkt = strftime("%H%M", localtime())
   file = open('pas.txt', 'w')
   file.write(wkt)
   file.close()
   pas2()

def pas2():
   os.system('clear')
   banner()
   try:
     with open('pas.txt', 'r') as yoman:
         ua = raw_input(lr+bold+"[?] "+wh+"Password "+lr+">>"+wh+" ")
         info = yoman.read()
         if ua == info:
           os.system("rm -rf pas.txt")
	   print(lr+"[!] "+wh+"Password Salah Sob..")
	   sleep(1.5)
           main()
         else:
	   print(lr+"[!] "+wh+"Selamat Datang..")
	   sleep(1.5)
           pas1()
   except Exception:
     print(lr+'[!] '+wh+'Error..\n')
     sys.exit()
   except KeyboardInterrupt:
     print(bold+lr+'[!] '+wh+'Exit..\n')
     sys.exit()

def main():
   try:
     os.system('clear')
     banner()
     ip = raw_input(lr+'[?] '+wh+'Proxy '+lr+'>>'+wh+' ')
     port = raw_input(lr+'[?] '+wh+'Port  '+lr+'>>'+wh+' ')
     print(lr+"[+] "+wh+"Start Checking..\n")
   except KeyboardInterrupt:
     print(lr+"[!] "+bold+wh+"Exit..\n")
     sys.exit()
   os.system("touch open.txt")
   os.system("touch close.txt")
   os.system("touch sakti.txt")
   sk = open("sakti.txt", "w")
   op = open("open.txt", "w")
   cl = open("close.txt", "w")
   a = 0
   wkt = strftime("%H:%M", localtime())
   while a <= 255:
    try:
      ngab = requests.get('http://'+ip+'.'+str(a)+':'+port+'/delay/0', timeout=2)
      pr = ip+'.'+str(a)+':'+port
      jos = ngab.status_code
      if ngab.status_code==200:
       print(wh+"["+lg+wkt+wh+"] "+lc+pr+wh+" is "+lg+"open (200)")
       a += 1
       op.write(pr+'\n')
      elif ngab.status_code==301:
       print(wh+"["+lg+wkt+wh+"] "+lc+pr+wh+" is "+lg+"open (301)")
       a += 1
       op.write(pr+'\n')
      elif ngab.status_code==307:
       print(wh+"["+lg+wkt+wh+"] "+lc+pr+wh+" is "+lg+"open (307)")
       a += 1
       op.write(pr+'\n')
      elif ngab.status_code==404:
       print(wh+"["+lg+wkt+wh+"] "+lc+pr+wh+" is "+lg+"open")
       a += 1
       op.write(pr+'\n')
      elif ngab.status_code==302:
       print(wh+"["+lg+wkt+wh+"] "+lc+pr+wh+" is "+lg+"open (302)")
       a += 1
       op.write(pr+'\n')
      elif ngab.status_code==403:
       print(wh+"["+lg+wkt+wh+"] "+lc+pr+wh+" is "+lr+"close (403)")
       a += 1
       cl.write(pr+'\n')
      elif ngab.status_code==401:
       print(wh+"["+lg+wkt+wh+"] "+lc+pr+wh+" is "+yw+"sakti (401)")
       a += 1
       sk.write(pr+'\n')
      elif ngab.status_code==503:
       print(wh+"["+lg+wkt+wh+"] "+lc+pr+wh+" is "+lg+"open (503)")
       a += 1
       op.write(pr+'\n')
      elif ngab.status_code==508:
       print(wh+"["+lg+wkt+wh+"] "+lc+pr+wh+" is "+lg+"open")
       a += 1
       op.write(pr+'\n')
      else:
       print(wh+"["+lg+wkt+wh+"] "+lc+pr+wh+" is "+lg+"open")
       a += 1
       op.write(pr+'\n')
    except requests.exceptions.Timeout:
      a += 1
      print(wh+"["+lg+wkt+wh+"] "+lc+ip+"."+str(a)+":"+port+wh+" is "+lr+"close")
      cl.write(ip+'.'+str(a)+':'+port+'\n')
      continue
    except legh:
      a += 1
      print(wh+"["+lg+wkt+wh+"] "+lc+ip+"."+str(a)+":"+port+wh+" is "+lr+"close")
      cl.write(ip+'.'+str(a)+':'+port+'\n')
      continue
    except KeyboardInterrupt as ex:
      cl.close()
      op.close()
      sk.close()
      erere()
    except Exception as Er:
      print(Er)


def erere():
    jum = open("open.txt", "r")
    jom = open("close.txt", "r")
    jim = open("sakti.txt", "r")
    jim = jim.readlines()
    jum = jum.readlines()
    jom = jom.readlines()
    print(lg+"\n     Hidup"+wh+": "+str(len(jum))+lr+" Mati"+wh+": "+str(len(jom))+yw+" Sakti:"+wh+" "+str(len(jim))+"\n")
    os.system("rm -rf close.txt")
    sys.exit()

if __name__=='__main__':
   pas1()
   erere()
