import tkinter
import customtkinter
from tinker import tkk

## Fix the library import Bugs

class myHydra:
    
    def __init__(self,name):
        self.name = name

    def popup(): 
        window = tkinter.Tk()
        window.title("Hydra")
        window.geometry("500x300")

        def close_window():
            window.destroy()
        def disable_event():
            pass
        def spawn():
            hydra_one = myHyrda("twins");
            myHydra.popop();
            myHydra.popup();

btn = tkk.Button(window, text = "FAIL", command = close_window)
btn.pack();

window.protocol("WM_DELETE_WINDOW", spawn);
window.mainloop(); 

## Create identical window again :)

class myHydra:
    
    def __init__(self,name):
        self.name = name

    def popup(): 
        window = tkinter.Tk()
        window.title("Hydra")
        window.geometry("500x300")

        def close_window():
            window.destroy()
        def disable_event():
            pass
        def spawn():
            hydra_one = myHyrda("twins");
            myHydra.popop();
            myHydra.popup();

btn = tkk.Button(window, text = "FAIL", command = close_window)
btn.pack();

## Spawn Hydra pups

