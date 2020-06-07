#import uiautomator
#from uiautomator import Device
#d= Device('9LUWJV9LLBQ4FUVC', adb_server_host='192.168.43.128', adb_server_port=5037)
# from uiautomator import device
#
# device(textMatches="Gallery").click()
from appium import webdriver

desired_cap={
  "deviceName": "9LUWJV9LLBQ4FUVC",
  "platformName": "Android",
 # "app": "C:\\Program Files\\Appium\\apk_path\\cris.org.in.prs.ima.2.1.12.apk"
  "app": "C:\\Program Files\\Appium\\apk_path\\Flipkart.apk"
}
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

