
import pyrebase
import sys
import time
from simplecrypt import encrypt, decrypt
password="vdhdnsnwn#745jrjmmfen"
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
def setup():
	GPIO.setup(1, GPIO.OUT,initial=0
	GPIO.setup(2, GPIO.OUT,initial=0)
	GPIO.setup(3, GPIO.OUT,initial=0)
	GPIO.setup(4, GPIO.OUT,initial=0)
	GPIO.setup(5, GPIO.OUT,initial=0)
	GPIO.setup(6, GPIO.OUT,initial=0)
	GPIO.setup(7, GPIO.OUT,initial=0)
	GPIO.setup(8, GPIO.OUT,initial=0)
	GPIO.setup(9, GPIO.OUT,initial=0)
	GPIO.setup(10, GPIO.OUT,initial=0)
	GPIO.setup(11, GPIO.OUT,initial=0)
	GPIO.setup(12, GPIO.OUT,initial=0)
	GPIO.setup(13, GPIO.OUT,initial=0)
	GPIO.setup(14, GPIO.OUT,initial=0)
	GPIO.setup(15, GPIO.OUT,initial=0)
	GPIO.setup(16, GPIO.OUT,initial=0)
	GPIO.setup(17, GPIO.OUT,initial=0)
	GPIO.setup(18, GPIO.OUT,initial=0)
	GPIO.setup(19, GPIO.OUT,initial=0)
	GPIO.setup(20, GPIO.OUT,initial=0)
	GPIO.setup(21, GPIO.OUT,initial=0
	GPIO.setup(22, GPIO.OUT,initial=0)
	GPIO.setup(23, GPIO.OUT,initial=0)
	GPIO.setup(24, GPIO.OUT,initial=0)
	GPIO.setup(25, GPIO.OUT,initial=0)
	GPIO.setup(26, GPIO.OUT,initial=0)
	GPIO.setup(27, GPIO.OUT,initial=0)
	GPIO.setup(28, GPIO.OUT,initial=0)
	GPIO.setup(29, GPIO.OUT,initial=0)
	GPIO.setup(30, GPIO.OUT,initial=0)
	GPIO.setup(31, GPIO.OUT,initial=0)
	
def setPinUp(pinno):
	GPIO.output(pinno,GPIO.HIGH)
	
def setpinLow(pinno):
	GPIO.output(pinno,GPIO.LOW)
	
def decryptText(text):
	return decrypt(password,text)
def streamhandler(message):
	print(message["pin"])
	
config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
try:
values=db.child("shyam").child("items").stream(streamhandler)
except KeyboardInterrupt:
print("exiting........")
