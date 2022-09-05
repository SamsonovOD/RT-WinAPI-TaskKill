import win32api, win32con, win32gui
from pynput.keyboard import Key, Controller
from pprint import pprint
import psutil
import time
import ctypes
from ctypes import wintypes
user32 = ctypes.windll.user32
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
keyboard = Controller()
def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))
def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst
appwindows = get_app_list()
def Test(a, b):
	print(a, b)
# print(psutil.pids())
for p in psutil.process_iter():
	print(p)
	print(p.pid)
    parent = psutil.Process(i[0])
    for child in parent.children(recursive=True):  # or parent.children() for recursive=False
        child.kill()
    parent.kill()
h_wnd = user32.GetForegroundWindow()
print(h_wnd)
pid = wintypes.DWORD()
user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
print(pid.value)
for i in appwindows:
	# print(str(i[0])+": "+str(i[1]))
	if i[1] == 'C:\\Users\\RT-Admin\\Downloads\\Telegram Desktop\\Wi-Fi_Unidirect_UDP-50Mbps_TCP-Unlim_last_file_size_6_40.tst':
		print("Attempting to destroy " + str(i[0]))
		print(win32gui.GetWindowText(655870))
		print(win32gui.EnumChildWindows(655870, Test, 'a'))
		print(win32gui.DefWindowProc(i[0], win32con.WM_DESTROY, None, None))
		win32gui.SetForegroundWindow(i[0])
		time.sleep(0.1)
		pdhk=win32gui.GetWindowRect(i[0])
		h_x, h_y = win32api.GetCursorPos()
		click(pdhk[2]-22,pdhk[1]+18)
		win32api.SetCursorPos([h_x, h_y])
		keyboard.press(Key.right)
		keyboard.release(Key.right)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)