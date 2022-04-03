from tkinter import *
from Tki import *

class KiWidget(KiObject, KiPack):
    def __init__(self):
        super().__init__()
        try:
            self.Widget = Widget()
        except TypeError:
            pass

    def Init(self):
        self.SetRelief(Relief_Ridge)

    def SetMaster(self, Master):
        self.Widget.configure(master=Master)

    def SetRelief(self, Relief):
        self.Widget.configure(relief=Relief)

    def SetBackGround(self, Background):
        self.Widget.configure(background=Background)

    def SetBorder(self, Border):
        self.Widget.configure(Border)


class KiWindow(KiWidget):
    def __init__(self):
        super().__init__()
        self.Widget = Tk()
        self.SetTitle("Tki")
        self.Resize(500, 500)
        self.Init()

    def SetMaxSize(self, Width, Height):
        self.Widget.maxsize(Width, Height)

    def SetMinSize(self, Width, Height):
        self.Widget.minsize(Width, Height)

    def SetTitle(self, Title: str):
        self.Widget.title(string=Title)

    def SetIcon(self, Icon):
        self.Widget.iconbitmap(bitmap=Icon)

    def Quit(self):
        self.Widget.quit()

    def Resize(self, Width: int, Height: int):
        self.Widget.geometry(f"{Width}x{Height}")

    def Center(self):
        X = round(int(self.GetScreenWidth())/2) + round(int(self.GetWidth())/2)
        Y = round(int(self.GetScreenHeight())/2) + round(int(self.GetHeight())/2)
        self.Move(X, Y)

    def Move(self, X: int = None, Y: int = None):
        self.Widget.geometry(f"+{X}+{Y}")

    def UpDate(self):
        self.Widget.update()

    def Run(self):
        self.MainLoop()


class KiButton(KiWidget):
    def __init__(self, Master: KiWidget = None, Text: str = EmptyString, Command=EmptyFunc,
                 ActiveBackground: str = "white", ActiveForeground: str = "black"):
        super().__init__()
        self.Widget = Button(master=Master.GetWidget(), text=Text, command=Command,
                             activebackground=ActiveBackground, activeforeground=ActiveForeground,)
        self.Init()

    def Flash(self):
        self.Widget.flash()


Window = KiWindow()
Window.SetMaxSize(500, 500)
Button = KiButton(Window, "asdasd")
Button.PackWidget()
Window.Run()