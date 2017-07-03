from win32com.client import Dispatch
from win32api import Sleep

while True:
    Sleep(30000)
    shell.SendKeys("{UP}")
    Sleep(1000)
    shell.SendKeys("{ENTER}")
