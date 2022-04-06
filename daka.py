import os
import time
import random
def daka():
    print(os.system('adb shell input keyevent 224'))
    time.sleep(3)
    print(os.system('adb shell input swipe 538 2313 559 1862'))
    time.sleep(5)
    print(os.system('adb shell input tap 179 1745'))
    time.sleep(10)
    print(os.system('adb shell input tap 517 2185'))
    time.sleep(5)
    print(os.system('adb shell input tap 112 858'))
    time.sleep(5)
    print(os.system('adb shell input tap 918 2144'))
    time.sleep(5)
    print(os.system('adb shell am force-stop com.alibaba.android.rimet'))
    pass
second = random.randint(0,60)
print(second)
time.sleep(second)
daka()
