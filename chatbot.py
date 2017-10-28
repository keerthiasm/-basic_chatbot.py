import os
import time
import random
import sys

nameIn=["what is your name","what's your name?","what is your name?","please enter your name","please enter your name here","what's ur name?","what's ur name"]
greetIn=["hello","hi","hi there!","hello there!","hi there","hello there"]
birth =["how old are you?","How old are you","What is your age?","What's your age"]
botmaster=["who is your botmaster?","who is your botmaster","who is your Botmaster?","who is your Botmaster","who is your BotMaster?","who is your BotMaster","who is your father?","who is your father","what is your father name?","what is your father name","what's your father name?","what's your father name","what's your mother name?","what's your mother name"]

nameOut=["my name is chutki","i am chutki","my name is chutki!","i am called as chukti","i'm called as chukti"]
greetOut=["hello","hi","hi there!","hello there!","hi there","hello there"]

B="Welcome to Strak chatbot.Let's start our conversation."
print(B)
while True:
        H = raw_input('=>').strip()
        
        if H == '':
            print("=> It's pleasure meeting you")
            time.sleep(2)
            os.system("sudo shutdown-h now")
            break
        elif HLower in nameIn:
            print '=>'+(random.choice(nameOut))
        elif HLower in greetIn:
            print '=>'+(random.choice(greetOut))
        elif HLower in birth:
            print('=> I was activated on 28 October 2017')
        elif HLower in botmaster:
            print ('=> My botmaster is Stark ')
