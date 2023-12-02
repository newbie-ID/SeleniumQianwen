from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def askQianWen(question, isVisible):
    # question:询问的问题，isVisible:自动化过程是否可见
    options = webdriver.ChromeOptions()
    # 下面的函数让Chrome在后台模式下运行
    if (not isVisible):
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
    # 打开保存的cookie文件
    with open(r'.\cookies', mode='r') as f:
        cookies_file = f.read()
    # 将读取的文件转为json格式
    cookie_list = json.loads(cookies_file)
    # Chrome打开浏览器
    browser = webdriver.Chrome(options=options)
    # 输入网址
    page_url = 'https://qianwen.aliyun.com/'
    browser.get(page_url)
    # 网页加载cookie
    for cookie in cookie_list:
        browser.add_cookie(cookie)
    # 需要刷新网页才能登录
    browser.refresh()
    # 再输入一次网址即可显示登录成功
    browser.get(page_url)
    # 等待页面加载出来 网速慢可以提高一些
    time.sleep(1)
    # 找到文本框
    text = browser.find_element(By.ID, "primary-textarea")
    # 输入文字
    text.send_keys(question)
    # 打入Enter
    text.send_keys(Keys.ENTER)
    # 等到输出完再继续
    WebDriverWait(browser, 120, poll_frequency=1, ignored_exceptions=None).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.icon--KHqHhnt1'))
    )
    # 提取答案
    answer = browser.find_element(By.CSS_SELECTOR, '.content--BiTVEwIO')
    return answer.text
