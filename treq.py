import time
import traceback

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
import geckodriver_autoinstaller


 # Check if the current version of geckodriver exists
                                     # and if it doesn't exist, download it automatically,
                                     # then add geckodriver to path

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

def my_proxy(port, user_name, password, ip_add):
    # print(user_name)
    geckodriver_autoinstaller.install()
    # headers = {'User-Agent': UserAgent().random}
    fp = webdriver.FirefoxProfile()
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http", str(ip_add))
    fp.set_preference("network.proxy.http_port", int(port))
    fp.set_preference("network.proxy.ssl", str(ip_add))
    # fp.
    # fp.set_preference("-headless")
    fp.set_preference("network.proxy.ssl_port", int(port))
    fp.set_preference("network.proxy.ftp", str(ip_add))
    fp.set_preference("network.proxy.ftp_port", int(port))
    fp.set_preference("network.proxy.socks", str(ip_add))
    fp.set_preference("network.proxy.socks_port", int(port))
    fp.set_preference("browser.cache.disk.enable", False)
    fp.set_preference("browser.cache.memory.enable", False)
    fp.set_preference("browser.cache.offline.enable", False)
    fp.set_preference("network.http.use-cache", False)
    fp.set_preference("general.useragent.override", UserAgent().random)
    fp.update_preferences()
    try:
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.get("https://ident.me/")
        wait(browser, 5).until(EC.alert_is_present())
        alert = browser.switch_to_alert()
        alert.send_keys(user_name + Keys.TAB + password)
        alert.accept()
        browser.get("https://ident.me/")
        time.sleep(5)
        # if browser.title=='Problem loading page':
        #     print("Here")
        #     browser.quit()
        # else:pass
        # browser.get("https://ident.me/")

    except Exception as e:
        print(e.__str__())
        traceback.print_exc()
        browser.quit()


import json
req=requests.get("https://nordvpn.com/wp-admin/admin-ajax.php?action=servers_recommendations&filters={%22country_id%22:228}")
json_convert=json.loads(req.text)
# print(json_convert)
for data in json_convert:
    try:
        server_name=data['hostname']
        print(server_name)
        browser=my_proxy(80, 'fbaileyiii@gmail.com', '213500DN', str(server_name))
        soup=BeautifulSoup(browser.page_source,'lxml')
        ip_add=soup.text
        print(ip_add)
        browser.quit()
        # main(ip_add,browser)
    except:
        pass