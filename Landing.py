from selenium import webdriver
import os
import pytesseract
from PIL import Image
from Main import username
from Main import password

pytesseract.pytesseract.tesseract_cmd = 'E:/python/Tesseract-OCR/tesseract.exe'
tessdata_dir_config = '--tessdata-dir "E:/python/Tesseract-OCR/tessdata"'

class DefineCode:

    def __init__(self, browser):
        browser.get_screenshot_as_file('E:/screenshot.png')
        self.im = Image.open('E:/screenshot.png')

    # 截取验证码图片
    def getCodeImage(self):
        self.im = self.im.crop((905, 260, 1000, 287))
        self.im.save('E:/code.png')

    #获取新验证码
    def getNewCode(self, browser):
        browser.implicitly_wait(3)
        newcode=browser.find_element_by_css_selector(".codeImg_btn")
        newcode.click()
        browser.implicitly_wait(3)
        browser.get_screenshot_as_file('E:/screenshot.png')
        self.im = Image.open('E:/screenshot.png')
        self.getCodeImage()
        self.code = pytesseract.image_to_string(self.im)

    # 获取四位验证码
    def getCode(self, browser):
        self.getCodeImage()
        self.code = pytesseract.image_to_string(self.im)
        while(not self.code.isdigit() or len(self.code)!=4):
            self.getNewCode(browser)
        return  self.code


class Land:
    def __init__(self, browser):
        # 学号
        self.input_username = browser.find_element_by_id('_easyui_textbox_input1')
        # 密码
        self.input_password = browser.find_element_by_id('_easyui_textbox_input2')
        # 验证码
        self.input_code = browser.find_element_by_id('_easyui_textbox_input3')
        # 登陆键
        self.enter_button = browser.find_element_by_id('btn_login')
        # 取得验证码
        self.definecode=DefineCode(browser)
        self.code=self.definecode.getCode(browser)

    def save_cookies(self, browser):
        browser.add_cookie({'name': username, 'value': password, 'code': self.code})
        cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]
        cookiestr = ';'.join(item for item in cookie)

    def clear_image(self):
        pic1 = 'E:/screenshot.png'
        pic2 = 'E:/code.png'
        if os.path.exists(pic1):
            os.remove(pic1)
        if os.path.exists(pic2):
            os.remove(pic2)

    def land(self, browser):
        while(not self.code.isalnum() or len(self.code)!=4):
            self.definecode.getNewCode(browser)

        # 输入学号
        self.input_username.send_keys(username)
        # 输入密码
        self.input_password.send_keys(password)
        # 输入验证码
        self.input_code.send_keys(self.code)
        # 确认登陆
        self.enter_button.click()
        # 延时等待
        browser.implicitly_wait(5)

        check=browser.find_element_by_css_selector(".alert_ok_btn")
        if(not check):
            # 保存cookies
            self.save_cookies(browser)
            # 清除缓存
            self.clear_image()
        else:
            check.click()
            browser.implicitly_wait(1)
            self.code = self.definecode.getCode(browser)
            self.land(browser)








