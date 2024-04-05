'''
    @author: Francesco Suma

    @version: 1.0

    @date: 05 - 04 - 2024

    @project: Alphabet Translator
'''

import prints as pts #file that deals with printing Alphabet Translator
import morseTranslator as mT #morse code translation takes place in this file
import NATOTranslator as NT #The translation into the NATO alphabet is done in this file
import os

def clear_terminal():
    # Checking the operating system to determine the correct command to clean the terminal
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def get_valid_input(prompt, valid_options):
    while True:
        try:
            choice = input(prompt)
            if choice in valid_options:
                return choice
            else:
                raise ValueError
        except ValueError:
            clear_terminal()
            pts.printAT()
            print("\033[1m - - - Invalid choice - - -\033[0m")
            print("\033[1mPlease enter a valid option.\033[0m")

def main():
    pts.printAT()

    choice = get_valid_input("\033[1mType:\n\n  1) to translate to morse code\n\n  2) to translate into NATO alphabet\n\n    > \033[0m", ['1', '2'])
    pts.printLine()

    phrase = input("\033[1mEnter the string to be translated:\n\n  > \033[0m").upper()

    pts.printLine()

    print("\033[1mResult: \033[0m")
    print()

    if choice == '1':
        mT.morseTranslator(phrase)
    elif choice == '2':
        NT.NATOTranslator(phrase)

    pts.printLine()

    choice = get_valid_input("\033[1mDo you want to run the program again? \n\n y -> yes \n\n n -> no \n\n  > \033[0m", ['y', 'n'])
    pts.printLine()

    if choice == 'y':
        clear_terminal()
        main()
    else:
        pts.printEND()

if __name__ == "__main__":
    main()