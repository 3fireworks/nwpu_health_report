import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

chrome_service = Service("/usr/bin/chromedriver")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(service = chrome_service, options=chrome_options)

# open nwpu
browser.get('https://uis.nwpu.edu.cn/cas/login?service=https://ecampus.nwpu.edu.cn/')
browser.maximize_window()

# login
browser.find_element(By.CSS_SELECTOR, "#vue_main > div:nth-child(2) > div.sw-login.sw-cloud-platform-nwpu-login > div > div:nth-child(2) > div:nth-child(3) > div > div > div:nth-child(1) > ul > li:nth-child(3)").click()
username = browser.find_element(By.ID, "username")
username.send_keys(USERNAME)
password = browser.find_element(By.ID, "password")
password.send_keys(PASSWORD)
browser.find_element(By.CSS_SELECTOR, "#fm1 > div:nth-child(4) > div > input.el-button.el-button--primary.el-button--medium.is-round").click()
time.sleep(1)

def page_is_loaded(browser):
    return browser.find_element(By.TAG_NAME, "body") != None

browser.get('https://yqtb.nwpu.edu.cn/wx/ry/jrsb_xs.jsp')
wait = ui.WebDriverWait(browser, 10)
wait.until(page_is_loaded)

browser.find_element(By.LINK_TEXT, "提交填报信息").click() # 提交填报信息

qrxx = browser.find_element(By.CSS_SELECTOR, "#qrxx_div > div.weui-cells.weui-cells_form > div.weui-cells.weui-cells_checkbox > label > div.weui-cell__hd > i") # 核实按钮
hidden_qrxx = browser.find_element(By.CSS_SELECTOR, "#qrxx_div > div.weui-cells.weui-cells_form > div.weui-cells.weui-cells_checkbox > label") # 核实按钮上级
ActionChains(browser).move_to_element(qrxx).click(hidden_qrxx).perform() # 事件链点击
browser.find_element(By.ID, "save_div").click() # 确认提交
time.sleep(1)
    
browser.quit()
