
import time
import requests
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
              numbering_mode=GPIO.BOARD)



while(True):
      api_response = requests.get('https://covid19api.herokuapp.com/confirmed')


      print(api_response.json()['latest'])

      x=str((api_response.json()['latest']))
      lcd.clear()
      lcd.write_string('Total Confirmed')
      lcd.crlf()
      lcd.write_string(x)
      time.sleep(1000)
