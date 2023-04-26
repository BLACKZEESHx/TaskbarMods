import win32gui
import winreg
import pyautogui

path = winreg.HKEY_CURRENT_USER

def set_color(r, g, b):
    key = winreg.OpenKeyEx(path, 'Software\\Microsoft\\Windows\\DWM', 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, 'AccentColor', 0, winreg.REG_DWORD, (b << 16) | (g << 8) | r)
    winreg.CloseKey(key)


# set_color(55, 55, 55)
def Make_Taskbar_Transparent(Enable=True):
    if Enable:
        color_key = winreg.OpenKeyEx(path, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(color_key, 'ColorPrevalence', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(color_key)
        ex_advance = winreg.OpenKeyEx(path, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\")
        Create_Taskbar_transparent_key =  winreg.CreateKey(ex_advance, "Advanced")
        winreg.SetValueEx(Create_Taskbar_transparent_key, "TaskbarAcrylicOpacity", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(Create_Taskbar_transparent_key)


# Get the handle of the taskbar
hwnd = win32gui.FindWindow("Shell_TrayWnd", None)

# Get the taskbar rectangle
taskbar_rect = win32gui.GetWindowRect(hwnd)

# Calculate the center of the taskbar
taskbar_center_x = (taskbar_rect[0] + taskbar_rect[2]) // 2
taskbar_center_y = (taskbar_rect[1] + taskbar_rect[3]) // 2

# Move the mouse to the center of the taskbar
pyautogui.FAILSAFE = False

pyautogui.moveTo(x=taskbar_center_x, y=taskbar_center_y)

# Right-click to open the context menu
pyautogui.click(button='right')
pyautogui.click(842, 236)
pyautogui.click(1139, 304)
pyautogui.moveTo(1109, 750)
pyautogui.dragRel(-974, 0, duration=1)
pyautogui.moveTo(54, 750)
pyautogui.dragRel(438, 0, duration=1)
pyautogui.click(264, 750,button='right')
pyautogui.click(326, 165)
pyautogui.click(264, 750,button='right')
pyautogui.click(389, 690)
