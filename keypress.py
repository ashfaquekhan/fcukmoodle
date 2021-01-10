from pynput import keyboard
from pynput.keyboard import Controller
import pyperclip as pc 
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hello!!")
print(ascii_banner)
kibord = Controller()
def on_release(key):
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.f9: 
        cptext = pc.paste()     
        kibord.type(cptext)
        print(cptext)

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
