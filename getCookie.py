# 导入需要的库
from selenium import webdriver
import json, os, time

# 选择保存目录
outdir = r'.'
# 登录的网址
douban_url = 'https://qianwen.aliyun.com/'

# 启动浏览器
browser = webdriver.Chrome()

# 浏览器打开网页
browser.get(douban_url)
# 等待30秒时间登录
time.sleep(30)
# 浏览器登录后获取cookie
cookies = browser.get_cookies()
# 将cookies保存在本地
with open(os.path.join(outdir, 'cookies'), mode='w') as f:
    f.write(json.dumps(cookies))
# 关闭浏览器
browser.close()
