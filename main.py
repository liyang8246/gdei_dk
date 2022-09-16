from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from uid import uid_list
import platform
from mail import sendmail

def dk(uid,pwd):
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    if platform.system() == 'Linux':
        opt.add_argument('--no-sandbox')
        opt.add_argument('--disable-gpu')
        opt.add_argument('--disable-dev-shm-usage')
        wd = webdriver.Chrome(service=Service(r'chromedriver'),chrome_options=opt)
    elif platform.system() == 'Windows':
        wd = webdriver.Chrome(service=Service(r'.\chromedriver.exe'),chrome_options=opt)
    else:
        print('???')
    wd.get('https://tb.gdei.edu.cn/login')
    print('start succeeded')

    dl_uid = wd.find_element(By.NAME,'username')
    dl_pwd = wd.find_element(By.NAME,'password')
    dl_uid.clear()
    dl_pwd.clear()
    dl_uid.send_keys(uid)
    dl_pwd.send_keys(pwd)
    dl_btn = wd.find_element(By.ID,'btnSubmit')
    dl_btn.click()
    print('login succeeded')
    sleep(3)
    
    wd.switch_to.frame('iframe0')
    dk_btn = wd.find_element(By.XPATH, '//*[@id="dk"]')
    dk_btn.click()
    print('cheakin succeeded')
    sleep(1)

    wd.close()

if __name__ == '__main__':
    for uid,pwd,mail in uid_list:
        try:
            dk(uid,pwd)
            print(uid,'checkin completed')
            sendmail(mail,1)
        except:
            sendmail(mail,0,'肯定不是我的问题\n去找李洋修服务器\n记得打卡')
