import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    ROOT_PATH = os.path.dirname(__file__)
    # 谷歌浏览器驱动
    # CHROME_DRIVER_PATH = '/root/NS/chromedriver'
    CHROME_DRIVER_PATH = 'D:/workspace/NS/chromedriver.exe'
    print(CHROME_DRIVER_PATH)

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # 无头模式
    options.add_argument('--no-sandbox')  # 绕过系统安全, 去沙盒
    # options.add_argument('--disable-gpu')  # 不弹出界面, Windows
    # options.add_argument('--disable-dev-shm-usage')  # Linux
    options.add_argument('--disable-extensions')  # 禁用扩展
    options.add_argument('disable-cache')  # 禁用缓存
    options.add_argument('disable-infobars')
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 关闭浏览器日志 DevTools...

    s = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://nftsea.one/JI6IP2X')

    eth_address = "0x2b6ed29a95753c3ad948348e3e7b1a251080ffb9"

    time.sleep(3)
    # 找到输入框并输入查询内容
    input_elem = driver.find_element(By.NAME, 'address')
    input_elem.send_keys(eth_address)
    # 提交按钮
    btn_elem = driver.find_element(By.XPATH, '//*[@id="airdrop-form"]/div/button')
    driver.execute_script("arguments[0].click();", btn_elem)
    time.sleep(3)
    print("------填写完成--------")
    filename = 'page_source.txt'
    with open(filename, 'w', encoding='utf-8') as file_object:
        file_object.write(driver.page_source)

    # driver.quit()


