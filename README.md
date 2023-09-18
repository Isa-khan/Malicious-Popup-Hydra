# Hydra Project

## Description

The Hydra project is a simple Python application using the tkinter library for creating and managing multiple windows. This project demonstrates the creation of multiple windows and the ability to close and spawn new windows.

**Note:** There are a few issues in the provided code that need to be fixed, which are described below in the "Fixes" section.

## Fixes

1. **Library Imports:** The import statements at the beginning of the code have some typos and incorrect module names. These need to be fixed for the code to work properly.

2. **Button Command:** The button's command attribute should point to a function, but it currently references a non-existent function. This needs to be corrected.

3. **Class Naming:** There is a naming inconsistency between the class definition and the class instantiation. The class is defined as `myHydra`, but it is instantiated as `myHyrda`. This inconsistency should be fixed.

4. **Function Definitions:** The `popup` and `spawn` functions are missing the `self` parameter in their definitions within the `myHydra` class. They should be defined as `def popup(self):` and `def spawn(self):`.

## Usage

To use this project, follow these steps after applying the fixes mentioned above:

1. Import the necessary libraries:
   - `import tkinter`
   - `import customtkinter`
   - `from tkinter import ttk as tkk`

2. Create an instance of the `myHydra` class and pass a name as a parameter to the constructor.

3. Call the `popup` method to create a window with a "FAIL" button.

4. When the "FAIL" button is clicked, the window will be closed.

5. To spawn a new window, call the `spawn` method.

6. The program will continue to create identical windows as long as the "FAIL" button is clicked.

## Example

```python
import tkinter
import customtkinter
from tkinter import ttk as tkk

class myHydra:
    
    def __init__(self, name):
        self.name = name

    def popup(self): 
        window = tkinter.Tk()
        window.title("Hydra")
        window.geometry("500x300")

        def close_window():
            window.destroy()
            
        def spawn():
            hydra_one = myHydra("twins")
            hydra_one.popup()

        btn = tkk.Button(window, text="FAIL", command=close_window)
        btn.pack()

        window.protocol("WM_DELETE_WINDOW", spawn)
        window.mainloop()
```

# Create an instance of myHydra and start the application
hydra = myHydra("main")
hydra.popup()
