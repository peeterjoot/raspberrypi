#! /usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

#GPIO.setup(27, GPIO.IN)
#while True:
#    readButton = GPIO.input(27) ;
#    print readButton ;
#    GPIO.output( 17, (not readButton) ) ;
#    time.sleep( 0.1 ) ;

GPIO.output( 17, 1 ) ;
time.sleep( 5 ) ;
GPIO.output( 17, 0 ) ;
