import win32gui

# Find the taskbar window
taskbar = win32gui.FindWindow("Shell_TrayWnd", None)

# Find the start button window
start_button = win32gui.FindWindowEx(taskbar, None, "Button", None)

# Hide the start button
win32gui.ShowWindow(start_button, 0)

exit()
import win32gui
import ctypes, win32con
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def getWallpaper():
    ubuf = ctypes.create_unicode_buffer(512)
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_GETDESKWALLPAPER,len(ubuf),ubuf,0)
    return ubuf.value

def setWallpaper(path):
    changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER,0,path,changed)

class StartRemover(QMainWindow):
    def __init__(self):
        super(StartRemover, self).__init__() 
        self.pic_label = QLabel(self)
        self.pic = QPixmap(r"C:\Users\Black\Downloads\Big_Sur_1.jpg")
        self.pic_label.setPixmap(self.pic)
        self.pic.size().setHeight(200)
        # Get the handle of the taskbar
        self.taskbar_hwnd = win32gui.FindWindow("Shell_TrayWnd", None)
        # Get the taskbar rectangle
        self.taskbar_rect = win32gui.GetWindowRect(self.taskbar_hwnd)
        self.setMinimumSize(5, 5)
        self.pic_label.setMinimumSize(5, 5)
        self.pic_label.setMaximumSize(35, 35)
        self.setMaximumSize(155, 155)
        self.setGeometry(self.taskbar_rect[0], self.taskbar_rect[1], 48, 35)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        # self.setwindowp
        # self.setWindowOpacity(0.5)
        self.show()
        # Start timer to check for start menu
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.checkStartMenu)
        self.timer.start(1) # check every 100ms
        
    def checkStartMenu(self):
        # Find start menu window handle
        start_menu_handle = win32gui.FindWindow("Shell_TrayWnd", None)
        if start_menu_handle != 0:
            # Start menu is open, activate this window
            # self.windowHandle().requestActivate()
            self.windowHandle().raise_()
        self.raise_()
        # if self is not self.isActiveWindow():
            # print("Please set the active window before  creating  a new window  for this  window (will be created if necessary).")
        # self.another = QWidget()
        # self.another.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartRemover()
    sys.exit(app.exec_())


18 * 12
# print(getWallpaper())


