# from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#
# binary=FirefoxBinary("/usr/bin/firefox")
#
# browser=webdriver.Firefox(executable_path='driver/geckodriver',firefox_profile=fp)
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver


def from_browser():
    # from pyvirtualdisplay import Display
    # display = Display(visible=0, size=(1024, 768))
    # display.start()
    # # vdisplay = xvfbwrapper.Xvfb()
    # vdisplay.start()
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.alert import Alert
    from selenium.webdriver.support.ui import WebDriverWait as wait
    from selenium.webdriver.support import expected_conditions as EC, expected_conditions
    # launch stuff inside virtual display here

    # vdisplay.stop()
    pri = '--proxy-server=185.164.56.246:80'
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument('--disable-notifications')
    chromeoptions.add_argument('--disable-dev-shm-usage')
    chromeoptions.add_argument('--shm-size=2g')
    chromeoptions.add_argument('--no-sandbox')
    chromeoptions.add_argument(pri)
    # chromeoptions.add_argument('--headless')
    chromeoptions.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(executable_path="driver/chromedriver", chrome_options=chromeoptions)
    browser.get("https://ident.me")
    browser.switch_to_alert()

    browser.find_element_by_id("userID").sendKeys("userName")

    browser.find_element_by_id("password").sendKeys("myPassword")

    browser.switch_to_alert()

    browser.switch_to_alert().defaultContent()
    # browser.switchTo().alert().sendKeys("guru99")
    # driver.switchTo().alert().accept()
    # driver.switchTo().alert().sendKeys("guru99")
    # driver.switchTo().alert().accept()


    # wait(browser, 5).until(EC.alert_is_present())
    # alert = browser.switch_to_alert()
    # alert.send_keys("hrnbwqcz-9" + Keys.TAB + "tph7ve0nlu24")
    # time.sleep(5)
    # alert.accept()

    return browser
# from tbselenium.tbdriver import TorBrowserDriver
# with TorBrowserDriver("/path/to/TorBrowserBundle/") as driver:
#     driver.get('https://check.torproject.org')

from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os

torexe = os.popen(r'/home/rana/.var/app/com.github.micahflee.torbrowser-launcher/data/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/TorBrowser/Tor/tor')
profile = FirefoxProfile(r'/home/rana/.var/app/com.github.micahflee.torbrowser-launcher/data/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/TorBrowser/Data/Browser/profile.default')
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
profile.set_preference("network.proxy.socks_remote_dns", False)
# profile.set_preference("javascript.enabled",True)
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile= profile, executable_path=r'driver/geckodriver')
driver.get("https://www.facebook.com/ChristiaNetcom/")
# profile_id = re.search(r"page_id=[0-9]+", result)
# profile_id = re.search(r"[0-9]+", profile_id.group()).group()
# print(profile_id)
# time.sleep(50)
# add={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# driver.add_cookie(add)
# from tbselenium.tbdriver import TorBrowserDriver
# with TorBrowserDriver("/home/rana/.var/app/com.github.micahflee.torbrowser-launcher/data/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/firefox/") as driver:
#     driver.get('https://check.torproject.org')


# from tbselenium.tbdriver import TorBrowserDriver
# import tbselenium.common as cm
# from tbselenium.utils import launch_tbb_tor_with_stem
#
# launch_tbb_tor_with_stem("/home/rana/Fraz_Work/tor-browser_en-US/Browser/firefox") # I think you can remove this, but maybe some future usages need that
# with TorBrowserDriver("/home/rana/.var/app/com.github.micahflee.torbrowser-launcher/data/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/firefox", tor_cfg=cm.USE_STEM) as driver:
#     driver.load_url("https://check.torproject.org", wait_on_page=3, wait_for_page_body=True)
#     print(driver.find_element_by("h1.on").text)
#     print(driver.find_element_by(".content > p").text)
# from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# profile=webdriver.FirefoxProfile(r'/home/rana/.var/app/com.github.micahflee.torbrowser-launcher/data/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/TorBrowser/Data/Browser/profile.default/')
# binary =FirefoxBinary(r'/home/rana/.var/app/com.github.micahflee.torbrowser-launcher/data/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/firefox/')
# #browser = binary.launch_browser(profile)
# profile.set_preference('network.proxy.type', 1)
# profile.set_preference('network.proxy.socks', '127.0.0.1')
# profile.set_preference('network.proxy.socks_port', 9150)
# browser=webdriver.Firefox(firefox_binary=binary,firefox_profile=profile,executable_path="driver/geckodriver")
# browser.get("http://yahoo.com")
# browser.save_screenshot("/Users/admin/Pictures/screenshot.png")
# browser.close()