from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

def start():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome("D:\\chromedriver\\chromedriver.exe",chrome_options=chrome_options)
    link = "link"



    driver.get(link)
    driver.maximize_window()
    time.sleep(1011)
start()