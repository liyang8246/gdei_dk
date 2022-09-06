from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

uid_list = [
    ('uid', 'pwd'),
    ('yyy', 'yyy')
]

def dk(uid,pwd):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    wd = webdriver.Chrome(service=Service(r'/root/chromedriver'),chrome_options=options)
    wd.get('https://tb.gdei.edu.cn/login')
    dl_uid = wd.find_element(By.NAME,'username')
    dl_pwd = wd.find_element(By.NAME,'password')

    dl_uid.clear()
    dl_pwd.clear()

    dl_uid.send_keys(uid)
    dl_pwd.send_keys(pwd)
    sleep(3)
    dl_btn = wd.find_element(By.ID,'btnSubmit')
    dl_btn.click()
    sleep(3)
    wd.switch_to.frame('iframe0')
    dk_btn = wd.find_element(By.XPATH, '//*[@id="dk"]')
    dk_btn.click()
    sleep(3)
    wd.close()

if __name__ == '__main__':
    for uid,pwd in uid_list:
        dk(uid,pwd)
