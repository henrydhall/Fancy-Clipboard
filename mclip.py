#! python
# mclip.py - A multi-clipboard program.

import sys
import pyperclip

TEXT  = {
    "agree" : "That works for me",
    "busy" : "Can we do another time?",
    "no" : "Thanks, but I'm not interested right now"
          }

if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")

keyphrase = sys.argv[1] #this gets the first argument from the command line argv

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for \"" + keyphrase + "\" copied to clipboard.")
else:
    print("No text for " + keyphrase + ".")

print("Exiting")
