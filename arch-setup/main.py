"""
This project is for post install of arch linux
"""

import os
import sys
import core

def main():
    """
    Main function
    """
    if os.geteuid() != 0:
        print("This script must be run as root")
        sys.exit(1)
   
    printer = core.Printer()
    term = core.Term()

    printer.print_bold(printer.colourise("Welcome to the Arch Linux Post Install Script", "blue"))

    
 
if __name__ == "__main__"
    main()
