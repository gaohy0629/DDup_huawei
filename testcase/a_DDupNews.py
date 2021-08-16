# coding=utf-8
import os
from telnetlib import EC
from time import sleep, time

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.mobilecommand import MobileCommand
from selenium.webdriver.android import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 登录方法
from testcase.R_DDupCourse import is_login, qq_share, back, is_activity_frame


def login(self):
    sleep(2)
    self.driver.find_element_by_xpath("//*[@text = '请输入手机号']").send_keys('16666667708')
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_check_btn').click()
    self.driver.find_element_by_id('com.nyc.ddup:id/tv_fetch_code').click()
    self.driver.find_element_by_id('com.nyc.ddup:id/et_code').send_keys(246810)
    self.driver.find_element_by_id('com.nyc.ddup:id/tv_login_btn').click()


# 上滑查看内容
def swipe_up(self, t, n):
    sleep(2)
    L = self.driver.get_window_size()
    x1 = L['width'] * 0.5
    y1 = L['height'] * 0.8
    y2 = L['height'] * 0.2
    i = 0
    for i in range(n):
        self.driver.swipe(x1, y1, x1, y2, t)
        sleep(1)


# 左滑查看内容
def swipe_left(self, t, n):
    L = self.driver.get_window_size()
    x3 = L['width'] * 0.8
    y3 = L['height'] * 0.6
    x4 = L['width'] * 0.1
    i = 0
    for i in range(n):
        self.driver.swipe(x3, y3, x4, y3, t)
        sleep(1)


# 下滑查看更多内容
def swipe_down(self, t, n):
    sleep(2)
    L = self.driver.get_window_size()
    x1 = L['width'] * 0.5
    y1 = L['height'] * 0.2
    y2 = L['height'] * 0.8
    i = 0
    for i in range(n):
        self.driver.swipe(x1, y1, x1, y2, t)
        sleep(1)


def is_toast2(self, message2):
    loc = "//*[contains(@text, '{}')]".format(message2)
    try:
        WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, loc)))
        ele = self.driver.find_element_by_xpath(loc).text
        print('Toast提示 ' + ele)
    except:
        print('no toast!')


class TestDDup:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['version'] = '10.0'
        caps['deviceName'] = 'XSENW19B29002179'
        caps['appPackage'] = 'com.nyc.ddup'
        caps['appActivity'] = '.activity.SplashActivity'
        caps['noReset'] = 'True'
        # caps['automationName'] = 'uiautomator1'
        caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(20)


    #  招考热讯模块自动化脚本
    def test_news(self):
        print('\n 开始测试【招考热讯】模块：')
        is_activity_frame(self)
        # 判断是否登录状态
        is_login(self, '16666667788')
        self.driver.find_element_by_xpath("//*[@text = '招考热讯']").click()
        # 资讯列表
        print('1、资讯列表开始测试')
        swipe_up(self, 500, 3)
        swipe_left(self, 500, 4)
        self.driver.find_element_by_xpath("//*[@text = '职高招考']").click()
        self.driver.find_element_by_xpath("//*[@text = '高考招考']").click()
        i = 0
        n = 1
        for i in range(10):
            if len(self.driver.find_elements_by_id('com.nyc.ddup:id/load_hint_view')) == 1:
                print('高考招考资讯已经下拉到底,没有更多了')
                break
            else:
                swipe_up(self, 500, n)
                i += 1
        swipe_down(self, 500, i + 1)
        print('资讯列表测试通过')

        # banner页
        print('2、开始测试banner详情页')
        sleep(2)
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_image').click()
        print('检测banner资讯详情是否收藏')
        try:
            cl = self.driver.find_element_by_xpath("//android.view.View[@content-desc='收藏']")
            cl.click()
            is_toast2(self, '成功')
        except:
            print('该资讯状态是已收藏')
            self.driver.find_element_by_xpath("//android.view.View[@content-desc='已收藏']").click()
            is_toast2(self, '取消')
        self.driver.keyevent(4)
        # 发布评论脚本待添加 self.driver.find_element_by_accessibility_id("写评论").click()
        # 资讯分享 QQ好友分享 待开发

        # 资讯分享 微信好友分享(前提是手机已安装登录微信)
        # print('资讯分享到微信好友')
        # self.driver.find_element_by_accessibility_id("微信好友").click()
        # self.driver.find_element_by_xpath("//*[@text ='文件传输助手']").click()
        # self.driver.find_element_by_xpath("//*[@text ='分享']").click()
        # self.driver.find_element_by_xpath("//*[@text ='返回DDup移动端']").click()
        # print('微信好友快捷分享成功')

        # 搜索功能
        print('3、开始测试搜索功能')
        self.driver.find_element_by_id('com.nyc.ddup:id/et_search_input').click()
        sleep(2)
        self.driver.find_element_by_id('com.nyc.ddup:id/et_search_input').send_keys('宁波')
        sleep(2)
        # 点击其中一条搜索联想结果
        self.driver.find_element_by_xpath("//*[@text ='全！宁波市区“摇号”招生出结果了！']").click()
        sleep(2)
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_news_title').click()
        swipe_up(self, 500, 3)
        self.driver.keyevent(4)  # 手机返回键
        self.driver.find_element_by_id("com.nyc.ddup:id/tv_cancel").click()
        # 点击搜索按钮查看搜索结果
        sleep(2)
        self.driver.find_element_by_id('com.nyc.ddup:id/et_search_input').click()
        sleep(2)
        self.driver.find_element_by_id('com.nyc.ddup:id/et_search_input').send_keys('宁波')
        sleep(2)
        self.driver.keyevent(66)
        self.driver.press_keycode(66)  # 输入法切换成了搜狗，该代码是点击键盘上的enter按钮
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.nyc.ddup:id/rv_item_list']/android.view.ViewGroup[1]").click()
        swipe_up(self, 500, 3)
        self.driver.keyevent(4)  # 手机返回键
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_close').click()
        self.driver.find_element_by_id("com.nyc.ddup:id/tv_cancel").click()
        print('搜索功能测试通过')

        # 收藏夹列表  取消收藏
        print('4、开始测试收藏夹功能')
        # 收藏资讯
        sc1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_news_title').text
        print(sc1)
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_news_title').click()
        sleep(2)
        if len(self.driver.find_elements_by_accessibility_id("收藏")) == 1:
            self.driver.find_element_by_accessibility_id("收藏").click()
            print('资讯收藏成功了')
            self.driver.keyevent(4)
            self.driver.find_element_by_id('com.nyc.ddup:id/ll_collection').click()
            text2 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_news_title').text
            assert sc1 == text2
        else:
            print("该资讯已被收藏了")
            # 取消收藏再收藏
            self.driver.find_element_by_accessibility_id("已收藏").click()
            sleep(5)
            self.driver.find_element_by_accessibility_id("收藏").click()
            self.driver.keyevent(4)
            sleep(3)
            self.driver.find_element_by_id('com.nyc.ddup:id/ll_collection').click()
            sleep(3)
            text3 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_news_title').text
            assert text1 == text3

        # 点击进入收藏列表第一条资讯详情页
        sleep(2)
        text4 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_news_title').text
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.nyc.ddup:id/rv_item_list']/android.view.ViewGroup[1]").click()
        sleep(2)
        # 验证该资讯详情页状态是否为已收藏
        assert len(self.driver.find_elements_by_xpath("//android.view.View[@content-desc='已收藏']")) == 1
        self.driver.keyevent(4)  # 手机返回键
        # 长按取消收藏
        e1 = self.driver.find_element_by_xpath("//*[@resource-id='com.nyc.ddup:id/rv_item_list']/android.view"
                                               ".ViewGroup[1]")
        TouchAction(self.driver).long_press(e1).perform()
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_confirm').click()
        assert text4 != 1
        print('该资讯已通过长按方式取消收藏了')
        print('收藏功能测试通过')

    def teardown(self):
        sleep(5)
        self.driver.quit()
