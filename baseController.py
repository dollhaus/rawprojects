#import myUsb
import json
import hashlib
import random
import unittest
from subprocess import call
import webbrowser
import os
import sys
import requests
import time
 
# stores all current data
currentData = []
# Stores the current hash value
currentHash = []
# Stores users hash number (For programming visiting device)
newUserHash = ''
# For hash output
hashOut = ''
# Hashes stored here with objectives as key value pairs
hashList = []
recordList = []

test = False
 
# Uses Requests to fetch HTML from static host: https://2.python-requests.org//en/latest/
print("Fetching HTML template")
wpgMessage = (requests.get('https://raw.githubusercontent.com/r0tekatze/rawprojects/master/wpghome.html')).text



 
wpg = open("results.html", 'w+')
# Writes data into JSON object
# Currently unused (need to work out for C side of things)
def prepare(data):
    with open(packedData, 'w') as i:
        json.dump(data, i)
 
def setTestConditions():
    currentData = "D131353C3A945738C1F810138B99C3105E77EB69A2303E72915FE3397C78A963", "D131353C3A945738C1F810138B99C3105E77EB69A2303E72915FE3397C78A963", "D131353C3A945738C1F810138B99C3105E77EB69A2303E72915FE3397C78A963"
    hashData = "This is a test hash code, generated " + time.strftime("%d/%m/%Y"), "This is a test has code, generated " + time.strftime("%d/%m/%Y"),"This is a test has code, generated " + time.strftime("%d/%m/%Y")
    hashList = "D131353C3A945738C1F810138B99C3105E77EB69A2303E72915FE3397C78A963", "D131353C3A945738C1F810138B99C3105E77EB69A2303E72915FE3397C78A963", "D131353C3A945738C1F810138B99C3105E77EB69A2303E72915FE3397C78A963"


 
# Send data to html page and display page
def display():
    try:       
        if (test):
            print("Setting test conditions\r\n")
            setTestConditions()

        print("trying...")
        blockData = currentData
        wpgHashes = hashData
        wpgHashList = hashList
        print("vars assigned")
        contents = wpgMessage.format(**locals())
        print("vars formatted")
        browseLocal(contents)
    except:
        e=exc_info()[0]
        print(e)
 
 
# Prepares web page for display
def browseLocal(webpageText = wpgMessage, filename='currentDataWPG.html'):
        '''Starts a webbrowser on a local file containing the text
        with given filename.'''
        strToFile(webpageText, filename)
        try:
            call(['epiphany-browser',filename])
        except:
            print(sys.exc_info())
 
 
# Writes string to a file
def strToFile(data, filename):
    outFile = open(filename, 'w+')
    outFile.write(data)
    outFile.close()
 
# Write the session objectives and return as a hashnumber
# Also adds unhashed objectives to a dict obj
def writeSessionObj():
    tempObj = ''
    newSessionObj = input("\nInput session objectives for this session:\n")
    print("ok input")
    hashList.append(hashIt(newSessionObj))
 
 
# This hash function is theoretically insecure in this manner of use
def writeUserHash():
    first = input("Input Users Name \n")
    second = str(random.randint(1000000000,9999999999))
    newUserHash = (hashIt((first+second)))
 
 
def hashIt(data):
    try:
        print("Trying to hash")
        handler = hashlib.sha256()
        handler.update(str(data).encode('utf-8'))
        hashOut = bytes(handler.hexdigest(), 'utf-8')
        print("I hashed it!: \n", hashOut)
    except Exception as f:
        print("I ain't done a hash!\n", str(f))
 
# Future functionality is intended to modify this script and allow rewriting of the microbit on the fly
# def writeToMicrobit(data):
    # Need to find out how to write data to microbit with python
   
    # Treat this like a document?
    """import microbit
    import radio
 
    # turn radio on
    radio.on()
    # set channel, power to max, assign group
    radio.config(channel=7, power=10, group=1)
 
    tX = radio.send()
    rX = radio.receive()
    dict currentBlock = []
 
    # While loop to send beacon signal
    while rX == False:
        tX = "SYN"
    if  rX == "ACK":
        # Placeholder in use here
        tX = '%s' % (data)
    # Wrong, work out how to actually validate for a 32bit string
    elif type(rX) == str && len(rX) == 32:
        # Needs code to validate
        # store new block in dict obj
        currentBlock = rX
    else:
        # Ensure that the script returns to sending signal code
        return"""
 
def quitProg():
    try:
        sys.exit()
    except:
        os._exit(1)
 
def sesObj():
    writeSessionObj()
    for i in hashList:
        myUsb.send(i)
        recordList.append(i)
        hashList.remove(i)
 
 
def genHash():
    writeUserHash()
 
 
 
print("ok so far, now for the main act!")
def main():
   
    print("First Main, ok")
    try:
        print("trying")
        while myUsb.mbit.read():
            print("Connection alive!")
    except Exception as e:
        print("\nUSB Connection error!\n" + str(e))
    print("Second Main, ok")
                 
    print("Trying to give the user a choice...")
    while True:
        try:
            choice = input("Select Option:\n 1 - Write session objectives\n 2 - Read block data\n 3 - Generate user hashes for visitor tags \n 0 - Exit \n")
            if choice == "0":
                quitProg();
            elif choice == "1":
                sesObj()
            elif choice == "2":
                display(data=currentData, hashData=currentHash, aHashList=hashList)
            elif choice == "3":
                genHash()
            elif choice == "4":
                test = True
            else:
                print("That isn't an available option")
        except Exception as g:
            print("An error occurred", repr(g)) #should implement proper logging here and evaluate the catch
            return True
       
        datalist = []
    while True:
        item = myUsb.incoming.get()
        datalist.append(item)
        myUsb.incoming.task_done()
    myUsb.incoming.join()
    for j in datalist:
            currentData.append(j)
main()
"""
TO DO:
Include method of writing hashcode to visitor microbit
"""
# ============================================UNIT TESTS==============================================
# class unitTests(unittest.TestCase):
#   """docstring for writeSessio"""
#   def testHash(self):
#       try:
#           self.assertEqual(writeUserHash("this"), 1EB79602411EF02CF6FE117897015FFF89F80FACE4ECCD50425C45149B148408)
#           print("Hashes test ok")
       
#       except:
#           print("Hash tests fail D:")