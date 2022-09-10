"""
This project started during my job app process, site like WorkDay 
have this skills section where you have to type each one of your skills
and you can't bulk import them in like a comma separated list, so I made
this tool:

Pass a csv file (doesn't need to be .csv, just a text file separated by commas)
as a command line arg, and press ESC when you want to print the next line, program
will automatically press ENTER for you after typing the string
"""

from pynput.keyboard import Key, Listener, Controller
import sys
import pyperclip

def on_press(key):
    
    # Press caps lock key to exit program
    if key == exit_key:
        print('Exiting program... Goodbye!')  
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    if k == 'esc':
        try:
            # Retrieve next string to type from iterator obj
            current_line = next(lines_iter)
            print(current_line)
            
            # Copy content to clipboard (directly typing with pynput is too slow)
            pyperclip.copy(current_line)

            # Paste content from keyboard
            keyboard.press(Key.ctrl_l)
            keyboard.press('v')
            keyboard.release(Key.ctrl_l)
            keyboard.release('v')
            
            # Presses ENTER key after typing
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

        except StopIteration:
            print('Done typing all lines in loaded file! Exiting program...')
            return False

if __name__ == '__main__':

    # Used to output strings from keyboard
    keyboard = Controller()

    # Assume content is stored in .csv file (comma separated)
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split(',')
        lines_iter = iter(lines)

    print('AUTOLOADER READY')

    # Start listening on a separate thread
    exit_key = Key.caps_lock
    with Listener(on_press=on_press) as listener:
        listener.join()