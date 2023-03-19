import pyautogui as pag
import time
def start_call():
    time.sleep(5)
    pag.click(1727,100)
def stop_call():
    pag.click(1036, 814)
    time.sleep(5)
    pag.click(1520,165)
for x in range(30):
    start_call()
    time.sleep(20)
    stop_call()
    print(f"Its {x} loop")
