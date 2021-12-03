#!python
"""
#mclip2.py
#Clip board app with features for adding and deleting phrases
#Uses pyperclip, sys, and shelve modules
#Uses shelve file "mclip2phrases"
"""

import sys
import pyperclip
import shelve
import pyinputplus
import os
import re

prohibitedKeys = [ "add", "list", "delete", "update", "clear",'i']

def AddPhrase():
    shelfFile = shelve.open('mclip2phrases')
    existingPhrases = shelfFile['phrases']
    shelfFile.close()
    newKey = pyinputplus.inputStr("New key: ", blockRegexes = [(".* .*")])
    while newKey in existingPhrases.keys() or newKey in prohibitedKeys:
        print("That is already a key or prohibited key.")
        print("Here is the list of existing keys and phrases.")
        ListPhrases()
        newKey = pyinputplus.inputStr("New key: ", blockRegexes = [(".* .*")])
    newPhrase = pyinputplus.inputStr("New associated phrase: ")
    shelfFile = shelve.open('mclip2phrases')
    myPhrases = shelfFile['phrases']
    myPhrases.update({newKey:newPhrase})
    shelfFile['phrases'] = myPhrases
    shelfFile.close()

def DeletePhrase():
    shelfFile = shelve.open('mclip2phrases')
    existingPhrases = shelfFile['phrases']
    shelfFile.close()
    keyToDelete = pyinputplus.inputStr("Key to delete: ", blockRegexes = [(".* .*")])
    while keyToDelete not in existingPhrases.keys():
        print("That is not an existing key.")
        print("Here is the list of existing keys and phrases.")
        ListPhrases()
        keyToDelete = pyinputplus.inputStr("Key to delete: ", blockRegexes = [(".* .*")])
    phraseToDelete = existingPhrases[keyToDelete]
    existingPhrases.pop(keyToDelete)
    shelfFile = shelve.open('mclip2phrases')
    shelfFile['phrases'] = existingPhrases
    shelfFile.close()
    print("Deleted key/phrase %s/%s" % (keyToDelete, phraseToDelete) )

def ListPhrases():
    #can improve using pprint
    shelfFile = shelve.open('mclip2phrases')
    existingPhrases = shelfFile['phrases']
    shelfFile.close()
    for k in existingPhrases:
        print("%s, %s" % (k, existingPhrases[k]) )

def UpdatePhrase():
    shelfFile = shelve.open('mclip2phrases')
    existingPhrases = shelfFile['phrases']
    shelfFile.close()
    keyToUpdate = pyinputplus.inputStr("Key to update: ", blockRegexes = [(".* .*")])
    while keyToUpdate not in existingPhrases.keys():
        print("That is not an existing key.")
        print("Here is the list of existing keys and phrases.")
        ListPhrases()
        keyToUpdate = pyinputplus.inputStr("Key to update: ", blockRegexes = [(".* .*")])
    print("Key to be updated: %s" % keyToUpdate )
    updatedPhrase = pyinputplus.inputStr("Updated phrase: ")
    existingPhrases[keyToUpdate] = updatedPhrase
    shelfFile = shelve.open('mclip2phrases')
    shelfFile['phrases'] = existingPhrases
    shelfFile.close()
    print("Updated phrase to: %s" % (updatedPhrase))
    

def CopyPhrase(keyToReference):
    shelfFile = shelve.open('mclip2phrases')
    existingPhrases = shelfFile['phrases']
    shelfFile.close()
    if keyToReference in existingPhrases:
        pyperclip.copy(existingPhrases[keyToReference])
        print("Text for \"" + keyToReference + "\" copied to clipboard.")
    else:
        print("No text for " + keyToReference + ".")

def ClearPhrases():
    print("TODO: clear all phrases")
    print("Don't actually do this. It's stupid")

def initialize():    
    shelfFile = shelve.open('mclip2phrases')
    shelfFile["phrases"] = {
        "agree" : "That works for me.",
        "busy" : "Can we do another time?",
        "no" : "Thanks, but I'm not interested right now."}
    shelfFile.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python mclip.py [command] - copy phrase text or update commands")
        sys.exit() #kill program if no first argument
        
    userInput = sys.argv[1] #this gets the first argument from the command line argv

    if userInput == 'i':
        initialize()
    elif userInput == "add":
        AddPhrase()
    elif userInput == "delete":
        DeletePhrase()
    elif userInput == "list":
        ListPhrases()
    elif userInput == "update":
        UpdatePhrase()
    elif userInput == "clear":
        ClearPhrases()
    else:
        CopyPhrase(userInput)
