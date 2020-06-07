## Logging into Jio Career app successful
# from appium import webdriver
# import time
#
# desired_cap={
#   "deviceName": "9LUWJV9LLBQ4FUVC",
#   "platformName": "Android",
#   "app": "C:\\Program Files\\Appium\\apk_path\\Jio.apk.apk"
# }
# driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
# driver.implicitly_wait(30)
#
# driver.find_element_by_id("com.ril.jiocareers:id/etUsername").send_keys("arundruk@gmail.com")
# driver.find_element_by_id("com.ril.jiocareers:id/etPassword").send_keys("Arun@1234")
# time.sleep(8)
# driver.find_element_by_id("com.ril.jiocareers:id/btnLogin").click()

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

desired_cap={
  "deviceName": "9LUWJV9LLBQ4FUVC",
  "platformName": "Android",
  #"app": "C:\\Program Files\\Appium\\apk_path\\Flipkart.apk",
  # "noReset" : "true",
   "appPackage": "com.flipkart.android",
  # "appWaitActivity" :"com.flipkart.android.activity.HomeFragmentHolderActivity"
    "appActivity" :"com.flipkart.android.activity.HomeFragmentHolderActivity"
}
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)
time.sleep(5)
driver.find_element_by_id("com.google.android.gms:id/cancel").click()
time.sleep(5)
driver.find_element_by_id("com.flipkart.android:id/custom_back_icon").click()
time.sleep(5)
# driver.find_element_by_id("com.flipkart.android:id/search_widget_textbox").send_keys("Microtek UPS")
# Search_element=driver.find_element_by_xpath("//android.widget.LinearLayout[@content-desc='Search on flipkart']/android.widget.TextView")
# Search_element.send_keys("Microtek ups")
# driver.execute_script("mobile:performEditorAction",{'action':'search'})

# driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Drawer']").click()
# driver.find_element_by_xpath("//android.widget.TextView[@text='Electronics']").click()
# #Electronics_search=driver.find_element_by_id("com.flipkart.android:id/search_icon")
# driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='Search']").click()
# driver.find_element_by_id("com.flipkart.android:id/search_autoCompleteTextView").send_keys("Microtek UPS")
# driver.execute_script("mobile:performEditorAction",{'action':'search'})
# driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()

for i in range(15):
    TouchAction(driver).press(x=444, y=1720).move_to(x=477, y=86).release().perform()
    time.sleep(3)

#new TouchAction(driver))
  # .press({x: 444, y: 1720})
  # .moveTo({x: 477: y: 586})
  # .release()
  # .perform()


