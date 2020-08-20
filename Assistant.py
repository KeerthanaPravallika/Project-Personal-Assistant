import os
import pyttsx3

print("Hello Keerthana Pravallika ! , This is your Personal Assistant \'Pandu\'")
pyttsx3.speak("Hello Keerthana pravallika , This is your Personal Assistant Pandu")

pyttsx3.speak("How can I help you ")
ch = input("How can I help you? ")

while(True):
    
    
    if(("notepad" in ch or "editor" in ch or "text editor" in ch or "write" in ch ) and ("not" not in ch)):
        pyttsx3.speak("Opening Notepad")
        os.system("notepad")
    elif(("browse" in ch or "google" in ch or "search" in ch or "chrome" in ch or "net" in ch or "internet" in ch) and ("not" not in ch)):
        pyttsx3.speak("Opening Chrome")
        os.system("chrome")
    elif(("message" in ch or "whatsapp" in ch or "text" in ch or "ping" in ch or "call" in ch) and ("not" not in ch)):
        pyttsx3.speak("Opening Whatsapp")
        os.system("whatsapp")
    elif(("media" in ch or "player" in ch or "wmplayer" in ch ) and ("not" not in ch)):
        pyttsx3.speak("Opening Windows media player")
        os.system("wmplayer")
    elif(("calculate" in ch or "calculator" in ch or "calculations" in ch) and ("not" not in ch)):
        pyttsx3.speak("Opening Calculator")
        os.system("calc.exe")
    elif(("paint" in ch or "draw" in ch or "sketch" in ch) and ("not" not in ch)):
        pyttsx3.speak("Opening Paint")
        os.system("mspaint.exe")
    elif("thanks" in ch or "thank you" in ch):
         pyttsx3.speak("You are welcome")
         print("You are welcome :)")
    elif("help" in ch):
        pyttsx3.speak("I can open Notepad , Google , Windows Media player , Calculator and Whatsapp")
        print("Notepad")
        print("Google")
        print("Windows Media Player")
        print("Calculator")
        print("Paint")
        print("Whatsapp")
    
    elif("do not" in ch):
        print("Done!")
    else:
        pyttsx3.speak("Sorry, I could not understand. Once type help to see whether the command is there or not ")
        
    
    pyttsx3.speak("How else can I help you")
    ch = input("How else can I help you ? ")
    if("stop" in ch):
        pyttsx3.speak("Thank you , Have a nice day")
        print("Thank you , Have a Nice day !")
        break
