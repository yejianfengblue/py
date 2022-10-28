from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from time import sleep

options = UiAutomator2Options()
options.platformVersion = '10'
options.udid='62f472779807'
options.no_reset=True
options.adb_exec_timeout=60
options.android_install_timeout=600
options.new_command_timeout=600

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

while True:
    try:
        account = driver.find_element(MobileBy.ID, value='com.tencent.mm:id/aip')
        TouchAction(driver).long_press(account).perform()
        sleep(1)
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, value='new UiSelector().textMatches("不再关注")').click()
        sleep(1)
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, value='new UiSelector().textMatches("不再关注")').click()
        sleep(5)
    except NoSuchElementException as e:
        print(e)
        print(driver.page_source)
    
# references    
# https://developer.android.com/reference/android/support/test/uiautomator/UiSelector#textmatches
