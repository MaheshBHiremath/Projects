# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:55:47 2021

@author: MaheshHiremath
"""
import pyttsx3
import PyPDF2

def listen_pdf():
    path_inp=input(r"Enter the file name with path: ")
    book = open(path_inp,'rb') #to read as binary data
    pdfreader = PyPDF2.PdfFileReader(book) #reading pdf
    pages = pdfreader.numPages 
    print("no of pages: ",pages)
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150) #to set speed percent, can be more than 100
    speaker.setProperty('volume', 0.8) # set volume from 0-1
    voices = speaker.getProperty('voices')
    for voice in voices: # to get the info. about various voices in our PC 
        print("Voice:")
        print("ID: %s" %voice.id)
        print("Name: %s" %voice.name)
        print("Age: %s" %voice.age)
        print("Gender: %s" %voice.gender)
        print("Languages Known: %s" %voice.languages)
        
    #to change voice set voice using setProperty()
    #male voice
    voice_id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    #female voice
    voice_id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    #setting voice
    voice_inp = int(input("Enter 1 for Male voice \nEnter 2 for female voice: "))
    
    if voice_inp==1:
        speaker.setProperty('voice', voice_id1)
    else:
        speaker.setProperty('voice', voice_id2)
    
    inp_page = int(input("Enter the page number to start: "))
    
    for i in range(inp_page,pages):
        page = pdfreader.getPage(inp_page) #to start from page no.    
        text = page.extractText()
        
        speaker.say(text)
        speaker.runAndWait()

    

listen_pdf()    