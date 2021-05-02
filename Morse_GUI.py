import time
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

import tkinter as tk
from tkinter import *

led=LED(24)
BRate=0.25

import re

def morse_dash():
    led.on()
    time.sleep(4*BRate)
    led.off()
    time.sleep(BRate)

def morse_dot():
    led.on()
    time.sleep(BRate)
    led.off()
    time.sleep(BRate)

CODE = {' ': '_', 
"'": '.----.', 
'(': '-.--.-', 
')': '-.--.-', 
',': '--..--', 
'-': '-....-', 
'.': '.-.-.-', 
'/': '-..-.', 
'0': '-----', 
'1': '.----', 
'2': '..---', 
'3': '...--', 
'4': '....-', 
'5': '.....', 
'6': '-....', 
'7': '--...', 
'8': '---..', 
'9': '----.', 
':': '---...', 
';': '-.-.-.', 
'?': '..--..', 
'A': '.-', 
'B': '-...', 
'C': '-.-.', 
'D': '-..', 
'E': '.', 
'F': '..-.', 
'G': '--.', 
'H': '....', 
'I': '..', 
'J': '.---', 
'K': '-.-', 
'L': '.-..', 
'M': '--', 
'N': '-.', 
'O': '---', 
'P': '.--.', 
'Q': '--.-', 
'R': '.-.', 
'S': '...', 
'T': '-', 
'U': '..-', 
'V': '...-', 
'W': '.--', 
'X': '-..-', 
'Y': '-.--', 
'Z': '--..', 
'_': '..--.-'}

def convertToMorseCode(sentence):
    sentence = sentence.upper()
    encodedSentence = ""
    for character in sentence:
        encodedSentence += CODE[character] + " " 
    return encodedSentence

def writeCode():
    sentence = inputtxt.get("1.0", "end-1c")
    encodedSentence = convertToMorseCode(sentence)
    print(encodedSentence)
    Output.insert(END, str(encodedSentence))
    pattern = re.compile('.')
    if pattern.match(encodedSentence):
        [morse_dot() for _ in encodedSentence]
    else:
        [morse_dash() for _ in encodedSentence]
        
        
root = Tk()
root.geometry("300x300")
root.title(" Morse_Code_GUI ")
  
      
l = Label(text = "Convert to morse code")
inputtxt = Text(root, height = 10,
                width = 25,
                bg = "light yellow")
  
Output = Text(root, height = 5, 
              width = 25, 
              bg = "light cyan")
  
Display = Button(root, height = 2,
                 width = 20, 
                 text ="Translate",
                 command = lambda:writeCode())
  
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
  
mainloop()
        