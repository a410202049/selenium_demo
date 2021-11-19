# 在服务器安装谷歌浏览器
sudo apt-get install libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb # Might show "errors", fixed by next line
sudo apt-get install -f
google-chrome --version # 查看版本

# 根据不同版本浏览器 下载对应驱动程序
Chrome：https://sites.google.com/a/chromium.org/chromedriver/downloads

Mirror: https://npm.taobao.org/mirrors/chromedriver

# 设置驱动可执行权限
chmod +x /opt/xunyou/bigdata/chromedriver/chromedriver

# 注意事项
linux上查看网页中文显示不出来的问题，需要在服务器上安装 中文字体
把msyh.ttf（微软雅黑拷贝到服务器） /usr/share/fonts/ 下
执行：fc-cache -fv
fc-list 查看系统字体
即可


# 参考代码

from selenium import webdriver
chromedriver_path = current_app.config.get('CHROME_DRIVER_PATH')
print(chromedriver_path)
kpi_pic_path = current_app.config.get('KPI_PIC_PATH')

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 设置无界面  可选
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(chromedriver_path, options=options)
browser.set_window_size(1300, 650)
url = url_for('quality_view.system_client_quality_chart', _external=True)
browser.get(url)
time.sleep(5)
# 保存截图
browser.save_screenshot(kpi_pic_path)