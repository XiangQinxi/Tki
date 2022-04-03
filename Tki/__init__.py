from tkinter import *
from Tki.KiCore import *


class KiData(object):
    def __init__(self, InitialData: dict = {}):
        """
        :param InitialData:
        KiData是用于储存类里的一些数据，为字典数字格式。
        """
        self.MasterData = InitialData

    def SetData(self, DataName: str, DataValue: str):
        self.MasterData[DataName] = DataValue

    def GetData(self, DataName: str):
        return self.MasterData[DataName]

    def GetMasterData(self):
        return self.MasterData[self.MasterData]


class KiMisc(object):
    def __init__(self):
        self.Widget = Misc()


class KiCilpBoard(object):
    def __init__(self):
        self.Widget = None

    def CilpBoardAppend(self, String):
        """
        :param String:
        添加剪切板文字
        """
        self.Widget.clipboard_append(string=String)

    def CilpBoardClear(self):
        """
        清空剪切板文字
        """
        self.Widget.clipboard_clear()

    def CilpBoardGet(self):
        return self.Widget.clipboard_get()


class KiBasic(object):
    def __init__(self, Master: any = None, WigetName: str = ""):
        """
        KiBasic -基本组件，所有可视化组件的父类
                :param Master: 父组件
        """
        try:
            self.Widget = BaseWidget(Master, WigetName)
        except tkinter.TclError:
            pass

    def GridAnchor(self, Anchor=None):
        self.Widget.anchor(anchor=Anchor)

    def GridBBox(self, Column=None, Row=None, Column2=None, Row2=None):
        """
        :param Column:
        :param Row:
        :param Column2:
        :param Row2:
        返回边界的整数坐标元组此小部件的框由几何管理器网格控制。如果给定 COLUMN, ROW，则边界框适用于具有指定行和列 0 的单元格细胞。 如果给定边界框 COL2 和 ROW2从那个单元格开始。
        返回的整数指定左上角的偏移量
        主小部件中的角以及宽度和高度。
        """
        self.Widget.grid_bbox(column=Column, row=Row, col2=Column2, row2=Row2)

    def After(self, Time, Headle):
        """
        :param Time:
        :param Headle:
        After 以毫秒为单位，每隔一段事件执行一次事件，会返回一个Id，使用AfterCanel进行取消。
        Demo: Id = After(50, Func)  # 开启循环并获取返回ID
              AfterCanel(Id)  # 取消循环
        """
        try:
            self.AfterID = self.Widget.after(ms=Time, func=Headle)
        except TypeError as Error:
            print(Error)
        return self.AfterID

    def AfterCanel(self, AfterID: str):
        """
        :param AfterID: After的返回值。
        AfterCanel 取消After命令，需输入参数AfterID
        """
        try:
            self.Widget.after_cancel(id=AfterID)
        except TypeError as Error:
            print(Error + "\n请确认参数是否是字串符，并且是After的返回数值")

    def AfterIdle(self, Headle):
        """
        :param Headle:
        AfterIdle 如果 Tcl 主循环没有事件，会自动调用Headle函数。
        """
        try:
            self.Widget.after_idle(func=Headle)
        except TypeError as Error:
            print(Error + "\n请确认是否输入参数且为函数")

    def Destory(self):
        """
        Destory 销毁当前组件
        """
        self.Widget.destroy()

    def Anchor(self, Anchor=None):
        self.GridAnchor(Anchor)

    def Configure(self, Cnf):
        self.Widget.configure(cnf=Cnf)

    def CommandDelete(self, Name: str):
        self.Widget.deletecommand(Name)

    def UpDate(self):
        self.Widget.update()

    def Bell(self, Display: bool = True):
        """
        :param Display:
        播放系统应用，Display决定是否播放声音
        """
        self.Widget.bell(displayof=Display)

    def Bind(self, BindName=None, Headle=None, Add: bool = None):
        """
        :param BindName:
        :param Headle:
        :param Add:
        BindName为事件名称，Headle为事件函数，Add抉择是否将事件函数被附加到其他绑定函数或是否它将取代以前的功能。将返回一个标识符用来取消事件.
        """
        return self.Widget.bind(sequence=BindName, func=Headle, add=Add)

    def BindAll(self, BindName=None, Headle=None, Add: bool = None):
        """
        :param BindName:
        :param Headle:
        :param Add:
        BindName为事件名称，Headle为事件函数，Add抉择是否将事件函数被附加到其他绑定函数或是否它将取代以前的功能。将返回一个标识符用来取消事件,不同的是将绑定到所有组件上面
        """
        return self.Widget.bind(sequence=BindName, func=Headle, add=Add)

    def BindTags(self):
        return self.Widget.bindtags()

    def UnBind(self, BindName=None, HeadleFuncId=None):
        self.Widget.unbind(sequence=BindName, funcid=HeadleFuncId)

    def UnBindAll(self, BindName):
        self.Widget.unbind_all(sequence=BindName)

    def WaitWindowDestory(self, Window):
        self.Widget.wait_window()

    def BBox(self, Column=None, Row=None, Column2=None, Row2=None):
        self.GridBBox(Column, Row, Column2, Row2)

    def Quit(self):
        self.Widget.quit()

    def MainLoop(self):
        self.Widget.mainloop()


class KiGet(object):
    def __init__(self):
        self.Widget = None

    def GetClass(self):
        return self.Widget.winfo_class()

    def GetChild(self):
        return self.Widget.winfo_children()

    def GetContaining(self, RootX, RootY, DisplayOf=None):
        return self.Widget.winfo_containing(rootX=RootX, rootY=RootY, displayof=DisplayOf)

    def GetExists(self):
        return self.Widget.winfo_exists()

    def GetGeometry(self):
        return self.Widget.winfo_geometry()

    def GetHeight(self):
        return self.Widget.winfo_height()

    def GetScreenWidth(self):
        return self.Widget.winfo_screenwidth()

    def GetScreenHeight(self):
        return self.Widget.winfo_screenheight()

    def GetWidth(self):
        return self.Widget.winfo_width()

    def GetID(self):
        return self.Widget.winfo_id()

    def GetInterps(self, DisplayOf=0):
        return self.Widget.winfo_interps(displayof=DisplayOf)

    def GetManager(self):
        return self.Widget.winfo_manager()

    def GetName(self):
        return self.Widget.winfo_name()

    def GetParent(self):
        return self.Widget.winfo_parent()

    def GetPathName(self, ID, DisplayOf=0):
        return self.Widget.winfo_pathname(id=ID, displayof=DisplayOf)

    def GetPointerX(self):
        return self.Widget.winfo_pointerx()

    def GetPointerY(self):
        return self.Widget.winfo_pointery()

    def GetPointerXY(self):
        return self.Widget.winfo_pointerxy()

    def GetRootX(self):
        return self.Widget.winfo_rootx()

    def GetRootY(self):
        return self.Widget.winfo_rooty()

    def GetScreen(self):
        return self.Widget.winfo_screen()

    def GetToplevel(self):
        return self.Widget.winfo_toplevel()

    def GetX(self):
        return self.Widget.winfo_x()

    def GetY(self):
        return self.Widget.winfo_y()


class KiPack(object):
    def __init__(self):
        self.Widget = Pack()

    def PackWidget(self, Padx=0, Pady=0, iPadx=0, iPady=0,
                   Side=Side_Top, Anchor: str = Anchor_Nw, Fill: str = Fill_None, Expand=Expand_NO):
        self.Widget.pack(padx=Padx, pady=Pady, ipadx=iPadx, ipady=iPady,
                         anchor=Anchor, fill=Fill, expand=Expand, side=Side)

    def PackInfo(self):
        return self.Widget.pack_info()

    def PackForget(self):
        self.Widget.pack_forget()

    def PackConfigure(self, Padx=0, Pady=0, iPadx=0, iPady=0,
                      Side=Side_Top, Anchor: str = Anchor_Nw, Fill: str = Fill_None, Expand=Expand_NO):
        self.Widget.pack_configure(padx=Padx, pady=Pady, ipadx=iPadx, ipady=iPady,
                                   anchor=Anchor, fill=Fill, expand=Expand, side=Side)


class KiPlace(object):
    def __init__(self):
        self.Widget = Place()

    def PlaceWidget(self):
        self.Widget.place()


class KiObject(KiCilpBoard, KiBasic, KiGet, KiData):
    def __init__(self):
        super().__init__()
        self.Widget = None

    def SetWidget(self, Widget):
        self.Widget = Widget

    def GetWidget(self):
        return self.Widget
