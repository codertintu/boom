

import os
import sys
import time
import random
import urllib.request


# Color and Codes
COLORS = { \
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
    "red-background": "\u001b[41m",
    "reset": "\u001b[0m",
}
 

logo = """

                         ██████╗░░█████╗░░█████╗░███╗░░░███╗           
                         ██╔══██╗██╔══██╗██╔══██╗████╗░████║                                                                                            
                                                                                                                     """

class ANSI():
     def background(code):
        return "\33[{code}m".format(code=code)
  
     def style_text(code):
        return "\33[{code}m".format(code=code)
  
     def color_text(code):
        return "\33[{code}m".format(code=code)
  
  
example_ansi = ANSI.background(
    97) + ANSI.color_text(35)  + logo
print(example_ansi)                                                                                                         
# print(logo)
print()

dev = ANSI.background(
    97) + ANSI.color_text(35) + ANSI.style_text(4) + "DEVELOPED BY ::  FIYAA INJECTAA & JESUPEFEXX & ADITH !  " + "instagram: @injecta_a" 
print(dev)

print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.3)
print('\u001b[32mThank you jesu                                               \u001b[0m'), time.sleep(.3)
print('\u001b[33;1mOwner(s): @fiyaainjectaa&jesu               Last Update: 8.04.2022\u001b[0m'), time.sleep(.3)
print('\u001b[31;1mMaintainer(s): @fiyaa                      Telegram: fiyaainjectaa\u001b[0m'), time.sleep(.3)

print()



print()

print('\u001b[33;1m-----------------------------------------------------------------------------------------------------------------------------------------------------------\u001b[0m'), time.sleep(.5)
print('\u001b[32m[1]\u001b[0m SMS BOOM    - Send unlimited otp message to victim mobile number'),                  time.sleep(.1)
print('\u001b[32m[2]\u001b[0m DEVELOPERS DETAILS AND OTHER SOCIAL MEDIAS AND GMAIL'),                              time.sleep(.1)
print('\u001b[32m[3]\u001b[0m whatsApp number'),                                                                   time.sleep(.1)
print('\u001b[32m[4]\u001b[0m whatsApp otp boom Coming Soon🔥'),                                                   time.sleep(.1)                                     
print('\u001b[33;1m-----------------------------------------------------------------------------------------------------------------------------------------------------------\u001b[0m'), time.sleep(.5)
				

choice = input('      ᴇɴᴛᴇʀ ᴀɴ ᴏᴘᴛɪᴏɴ : ')

if choice == "1":
   os.system("python3 boom_main")

elif choice == "2":
   os.system("python3 boom_det")
elif choice == "3":
   os.system("termux-open-url http://wa.me//+3197010286435")
else:
    print ("invild option try again !")

#  DONT TRY TO REEDIT MY CODE ITS MAYBE TRACABLE AND PANNISHABLE !!!
