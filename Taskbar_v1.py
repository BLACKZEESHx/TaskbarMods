import winshell
import winreg
import psgshortcut.gui
import os
import subprocess
import asyncio
import time
import shutil
import struct

desktop = winshell.desktop()
path = winreg.HKEY_CURRENT_USER


def Make_Taskbar_Transparent(Enable=True):
    if Enable:
        color_key = winreg.OpenKeyEx(
            path, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(color_key, 'ColorPrevalence', 0, winreg.REG_DWORD, 0)
        blury = winreg.SetValueEx(
            color_key, "EnableTransparency", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(blury)
        winreg.CloseKey(color_key)
        ex_advance = winreg.OpenKeyEx(
            path, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\")
        Create_Taskbar_transparent_key = winreg.CreateKey(
            ex_advance, "Advanced")
        winreg.SetValueEx(Create_Taskbar_transparent_key,
                          "TaskbarAcrylicOpacity", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(Create_Taskbar_transparent_key)


async def is_start_killer_open():
    sysbit = struct.calcsize("P") * 8

    if sysbit == 64:
        subprocess.run(["taskkill", "/f", "/im", "StartKiller.exe"], shell=True)
        await asyncio.sleep(1)
        os.startfile(r"Start\startkiller-portable\64\StartKiller.exe")

    if sysbit == 32:
        subprocess.run(["taskkill", "/f", "/im", "StartKiller.exe"], shell=True)
        await asyncio.sleep(1)
        os.startfile(r"Start\startkiller-portable\32\StartKiller.exe")

    print(sysbit)


async def Start_shortcut_creator():
    if not (os.path.exists(desktop + "\\Start.lnk")):
        psgshortcut.gui.create_shortcut_exe_or_other(arguments=f"{os.path.abspath(os.getcwd())}\\Start\\start.vbs",
                                                        target="wscript",
                                                        icon=f"{os.path.abspath(os.getcwd())}\\Start\\Windows 10X.ico",
                                                        new_name="Start")
        asyncio.sleep(5)
        shutil.move("Start.lnk",
                f"{desktop}\\Start.lnk")


if __name__ == "__main__":
    os.startfile("Start\\CenterTaskbar.exe")
    # asyncio.run(Make_Taskbar_Transparent())
    asyncio.run(is_start_killer_open())
    asyncio.run(Start_shortcut_creator())
# End Windows Explorer task
# subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], shell=True)


# Start Windows Explorer task
# subprocess.run(["explorer.exe"], shell=True)
