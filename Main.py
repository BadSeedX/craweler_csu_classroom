from selenium import webdriver
import Landing
import Request

username = '0902170323'
password = '199904'


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.get('http://classroom.csu.edu.cn/')
    # 登陆
    land=Landing.Land(browser)
    land.land(browser)
    # 发送请求
    request=Request.Request(browser)
    request.request(browser)
    # 关闭
    browser.implicitly_wait(5)
    browser.close()