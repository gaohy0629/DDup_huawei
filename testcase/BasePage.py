# coding=utf-8
from telnetlib import EC
from time import sleep, time

import selenium
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.android import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#  封装了返回方法
def back(self):
    bc = self.driver.find_element_by_id('com.nyc.ddup:id/iv_back')
    bc.click()


# 上滑
def swipe_up(self, t, n):
    L = self.driver.get_window_size()
    x1 = L['width'] * 0.65
    y1 = L['height'] * 0.75
    y2 = L['height'] * 0.25
    i = 0
    for i in range(n):
        self.driver.swipe(x1, y1, x1, y2, t)


# 左滑
def swipe_left(self, t, n):
    L = self.driver.get_window_size()  # 获取屏幕尺寸大小，然后打印出来
    x1 = L['width'] * 0.75
    x2 = L['width'] * 0.25
    y1 = L['height'] * 0.5
    i = 0
    for i in range(n):
        self.driver.swipe(x1, y1, x2, y1, t)
        sleep(3)


# 右滑
def swipe_right(self, t, n):
    L = self.driver.get_window_size()
    x3 = L['width'] * 0.8
    y3 = L['height'] * 0.6
    x4 = L['width'] * 0.1
    i = 0
    for i in range(n):
        self.driver.swipe(x4, y3, x3, y3, t)
        sleep(1)


# 下滑（包括下拉刷新）
def swipe_down(self, t, n):
    L = self.driver.get_window_size()
    x1 = L['width'] * 0.5
    y1 = L["height"] * 0.3
    y2 = L["height"] * 0.6
    i = 0
    for i in range(n):
        self.driver.swipe(x1, y1, x1, y2, t)
        sleep(3)


# 登录
def login(self):
    self.driver.implicitly_wait(5)
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_user_home').click()
    self.driver.find_element_by_xpath("//*[@text = '请输入手机号']").send_keys('16666667708')
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_check_btn').click()
    self.driver.find_element_by_id('com.nyc.ddup:id/tv_fetch_code').click()
    self.driver.find_element_by_id('com.nyc.ddup:id/et_code').send_keys(246810)
    self.driver.find_element_by_id('com.nyc.ddup:id/tv_login_btn').click()


# QQ第三方登录
def third_login(self):
    sleep(2)
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_user_home').click()
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_check_btn').click()
    self.driver.keyevent(4)
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_login_qq').click()
    self.driver.find_element_by_id('com.tencent.mobileqq:id/fds').click()
    print("QQ登录成功")


# 退出登录
def logout(self):
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_user_home').click()
    self.driver.find_element_by_id('com.nyc.ddup:id/ll_setting').click()
    sleep(2)
    swipe_up(self, 2000, 1)
    sleep(2)
    self.driver.find_element_by_id('com.nyc.ddup:id/tv_logout').click()
    sleep(2)
    var = self.driver.find_element_by_xpath("//*[@text = '确定']")
    var.click()
    print('退出登录了')


# 登录状态判断
def is_login(self, phone):
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_user_home').click()
    try:
        self.driver.find_element_by_xpath("//*[@text = '请输入手机号']").send_keys(phone)
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_check_btn').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_fetch_code').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/et_code').send_keys(246810)
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_login_btn').click()
        print('判断app的登录状态：未登录，现在已登录成功,账号为' + phone)
        sleep(2)
    except NoSuchElementException:
        u1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_name').text
        print('判断app的登录状态：已登录状态，用户名是' + u1)
        back(self)


# 查看元素是否存在
def find_item(self, el):
    source = self.driver.page_source
    if el in source:
        var = self.driver.find_element_by_xpath("//*[@text = '加入学习']")
        var.click()
        print('已经将该课程加入到学习中心了')
    else:
        print('已加入学习中心了')


# QQ分享
def qq_share(self):
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_share').click()
    self.driver.find_element_by_id('com.nyc.ddup:id/tv_cancel').click()
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_share').click()
    self.driver.find_element_by_id('com.nyc.ddup:id/layout_share_qq').click()
    self.driver.find_element_by_id('com.tencent.mobileqq:id/text1').click()
    self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
    self.driver.find_element_by_xpath("//*[@text = '返回DDup']").click()
    loc = self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']").text
    print('Toast提示' + loc)


# 判断是否有活动弹框
def is_activity_frame(self):
    def loaded(driver):
        if len(self.driver.find_elements_by_id('com.nyc.ddup:id/iv_cover')) >= 1:
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_close').click()
            print('活动弹框已关闭')
            return True
        else:
            return False

    try:
        WebDriverWait(self, 10).until(loaded)
    except:
        print('没有活动弹框')


# 判断是否有启动页
def is_start_page(self):
    def loaded(driver):
        if len(self.driver.find_elements_by_id('com.nyc.ddup:id/tv_time_count')) >= 1:
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_time_count').click()
            print('启动页配置了，点击跳过了启动页')
            return True
        else:
            return False

    try:
        WebDriverWait(self, 10).until(loaded)
    except:
        print('没有启动页')


# Toast获取
def is_toast1(self, message):
    try:
        toast_loc = (By.XPATH, '//*[contains(@text, "{}")]'.format(message))
        ele = WebDriverWait(self.driver, 10, 0.1).until(
            lambda x: x.find_element(*toast_loc).text)
        print(ele)
    except:
        print('no Toast~')


# toast获取方法2
def is_toast2(self, message2):
    loc = '//*[contains(@text, "{}")]'.format(message2)
    try:
        WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, loc)))
        ele = self.driver.find_element_by_xpath(loc).text
        print(ele)
    except:
        print('no toast~~')


#  封装了返回方法
def back(self):
    bc = self.driver.find_element_by_id('com.nyc.ddup:id/iv_back')
    bc.click()


# 发布评论
def work_comment(self, keyword):
    if int(self.driver.find_element_by_id('com.nyc.ddup:id/tv_comment_num').text) == 0:
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_comment').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/et_content').send_keys(keyword)
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_send').click()
        loc = self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']").text
        print('第一个评论发布成功，Toast提示 ' + loc)
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
        e1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_comment_content')
        TouchAction(self.driver).long_press(e1).perform()
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_item').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_close').click()
    else:
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_comment').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_submit_comment').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/et_content').send_keys(keyword)
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_send').click()
        loc = self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']").text
        print('Toast提示 ' + loc + ',没抢到沙发.')
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
        e1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_comment_content')
        TouchAction(self.driver).long_press(e1).perform()
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_item').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_close').click()