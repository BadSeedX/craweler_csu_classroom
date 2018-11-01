class Request:
    def __init__(self, browser):
        self.button=browser.find_element_by_name('异常申诉')

    def request(self, browser):
        self.button.click()
        if (not browser.find_elements_by_css_selector(".appealBtn.course_appeal")):
            print("未发现旷课记录")
            return
        node=browser.find_element_by_css_selector(".appealBtn.course_appeal")
        try:
            while node:
              node.click()
              text = browser.find_element_by_css_selector(".textbox-text.validatebox-text.textbox-prompt")
              text.send_keys('本节计划教学安排不在教室')
              sub_button = browser.find_element_by_css_selector(".panel_region.layout_south ")
              sub_button.click()
              browser.refresh()
              # browser.implicitly_wait(1)
              button = browser.find_element_by_name('异常申诉')
              button.click()
              if (not browser.find_elements_by_css_selector(".appealBtn.course_appeal")):
                  print("申请已成功提交!")
                  break;
              node = browser.find_element_by_css_selector(".appealBtn.course_appeal")
        except:
            print("未成功提交!")
            browser.close()





