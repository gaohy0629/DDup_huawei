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


# 上滑查看更多
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


# 向右滑动
def swipe_right(self, t, n):
    L = self.driver.get_window_size()
    x3 = L['width'] * 0.8
    y3 = L['height'] * 0.6
    x4 = L['width'] * 0.1
    i = 0
    for i in range(n):
        self.driver.swipe(x4, y3, x3, y3, t)
        sleep(1)


# 下滑（下拉刷新）
def swipe_down(self, t, n):
    L = self.driver.get_window_size()
    x1 = L['width'] * 0.5
    y1 = L["height"] * 0.3
    y2 = L["height"] * 0.6
    i = 0
    for i in range(n):
        self.driver.swipe(x1, y1, x1, y2, t)
        sleep(3)


# 登录方法
def login(self):
    self.driver.implicitly_wait(5)
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_user_home').click()
    self.driver.find_element_by_xpath("//*[@text = '请输入手机号']").send_keys('16666667708')
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_check_btn').click()
    self.driver.find_element_by_id('com.nyc.ddup:id/tv_fetch_code').click()
    self.driver.find_element_by_id('com.nyc.ddup:id/et_code').send_keys(246810)
    self.driver.find_element_by_id('com.nyc.ddup:id/tv_login_btn').click()


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

    # 公益课程用例
    def test_course(self):
        print('【公益课程】模块测试→ ')
        # 判断是否有启动页
        is_start_page(self)
        # 判断首页是否有活动弹框，有弹框就点击关闭，没有就打印“没有弹框
        is_activity_frame(self)
        # 判断app的登录状态
        is_login(self, '16666667788')

        self.driver.find_element_by_xpath("//*[@text = '公益课程']").click()
        # 搜索功能
        print('搜索功能测试：')
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_search_bar').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/et_search_input').send_keys('错别字')
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_text').click()
        sleep(2)
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_lesson_title').click()
        back(self)
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_cancel').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_cancel').click()
        print('搜索功能完成测试')
        sleep(5)
        # 热门课程
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.nyc.ddup:id/rv_hot_courses']/android.view.ViewGroup[2]").click()
        sleep(2)
        swipe_up(self, 1000, 2)
        sleep(3)
        back(self)

        # 以语文课程为例
        print('语文课程详情页测试： ')
        self.driver.find_element_by_id('com.nyc.ddup:id/fl_subject_chinese').click()
        self.driver.find_element_by_xpath("//*[@text = '语言积累与运用']").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@text='火眼金睛识错字' and contains(@resource-id,'com.nyc.ddup:id/tv_lesson_desc')]").click()
        # 课程分享
        qq_share(self)
        self.driver.find_element_by_id('com.nyc.ddup:id/cl_lesson_director').click()
        sleep(2)
        back(self)
        self.driver.find_element_by_id('com.nyc.ddup:id/cl_lesson_teacher').click()
        sleep(2)
        # 上滑查看老师更多课程
        swipe_up(self, 1000, 2)
        back(self)
        # 判断该课程是否加入到学习计划中
        find_item(self, "//*[@text = '加入学习']")
        # 点击进入课程播放页面 播放暂停视频 试卷 课程分享 以及视频反馈投诉
        print('开始播放课程')
        self.driver.tap([(471, 305), (609, 443)], 1000)
        sleep(2)
        # 引导页
        source = self.driver.page_source
        if 'com.nyc.ddup:id/iv_i_known' in source:
            var = self.driver.find_element_by_id('com.nyc.ddup:id/iv_i_known')
            var.click()
            print('点击引导页我知道了')
        else:
            print('课程播放页面没有引导页了')

        self.driver.find_element_by_id('com.nyc.ddup:id/exo_pause').click()
        # 试卷和答题卡(前提是引导页都已经点击过了)
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_video_exam').click()
        if len(self.driver.find_elements_by_xpath("//*[@text = '开始答题']")) == 1:
            self.driver.find_element_by_xpath("//*[@text = '开始答题']").click()
            swipe_left(self, 1000, 3)
            self.driver.find_element_by_xpath("//*[@text = '答题卡']").click()
            sleep(2)
            self.driver.find_element_by_xpath("//*[@text = '提交练习并查看报告']").click()
            self.driver.find_element_by_xpath("//*[@text = '交卷']").click()
            back(self)
            print('答题完成，回到课程播放页面')
        elif len(self.driver.find_elements_by_xpath("//*[@text = '继续']")) == 1:
            self.driver.find_element_by_xpath("//*[@text = '继续']").click()
            swipe_left(self, 1000, 2)
            self.driver.find_element_by_xpath("//*[@text = '答题卡']").click()
            self.driver.find_element_by_xpath("//*[@text = '提交练习并查看报告']").click()
            self.driver.find_element_by_xpath("//*[@text = '交卷']").click()
            back(self)
            print('继续答题完成，回到课程播放页面')
        elif len(self.driver.find_elements_by_xpath("//*[@text = '练习报告']")) == 1:
            self.driver.find_element_by_xpath("//*[@text = '查看解析']").click()
            sleep(2)
            back(self)
            sleep(2)
            back(self)
            print('查看报告完成，回到课程播放页面')

        # 试卷和答题卡(需要判断是否有引导页)
        # self.driver.find_element_by_id('com.nyc.ddup:id/iv_video_exam').click()
        # if len(self.driver.find_elements_by_xpath("//*[@text = '开始答题']")) >= 1:
        #     self.driver.find_element_by_xpath("//*[@text = '开始答题']").click()
        #     if len(self.driver.find_elements_by_id('com.nyc.ddup:id/iv_i_known')) >= 1:
        #         self.driver.find_element_by_id('com.nyc.ddup:id/iv_i_known').click()
        #     else:
        #         print('答题页面没有引导页')
        #     print('第一次答题')
        #     swipe_left(self, 1000, 3)
        #     self.driver.find_element_by_xpath("//*[@text = '答题卡']").click()
        #     if len(self.driver.find_elements_by_id('com.nyc.ddup:id/iv_i_known')) >= 1:
        #         self.driver.find_element_by_id('com.nyc.ddup:id/iv_i_known').click()
        #         self.driver.find_element_by_xpath("//*[@text = '提交练习并查看报告']").click()
        #         self.driver.find_element_by_xpath("//*[@text = '交卷']").click()
        #         back(self)
        #         print('答题完成，回到课程播放页面')
        #     else:
        #         print('答题卡页面没有引导页')
        # elif len(self.driver.find_elements_by_xpath("//*[@text = '练习报告']")) >= 1:
        #     self.driver.find_element_by_xpath("//*[@text = '查看解析']").click()
        #     back(self)
        #     print('习题已完成，查看报告')
        # elif len(self.driver.find_elements_by_xpath("//*[@text = '继续']")) >= 1:
        #     self.driver.find_element_by_xpath("//*[@text = '继续']").click()
        #     swipe_left(self, 1000, 2)
        #     self.driver.find_element_by_xpath("//*[@text = '答题卡']").click()
        #     if len(self.driver.find_elements_by_id('com.nyc.ddup:id/iv_i_known')) >= 1:
        #         self.driver.find_element_by_id('com.nyc.ddup:id/iv_i_known').click()
        #         self.driver.find_element_by_xpath("//*[@text = '提交练习并查看报告']").click()
        #         self.driver.find_element_by_xpath("//*[@text = '交卷']").click()
        #         back(self)
        #         print('答题完成，回到课程播放页面')
        #     else:
        #         print('答题卡页面没有引导页')

        # 点击课程分享
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_video_share').click()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@text = 'QQ']").click()
        self.driver.find_element_by_id('com.tencent.mobileqq:id/ivTitleBtnLeftButton').click()
        sleep(3)
        # 视频反馈
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_video_more').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/exo_content_frame').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_video_more').click()
        self.driver.find_element_by_xpath("//*[@text ='视频反馈']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@text = '声音有误']").click()
        sleep(2)
        self.driver.find_element_by_id('com.nyc.ddup:id/et_feedback_message').send_keys('版本测试中，请忽略，谢谢')
        sleep(2)
        self.driver.find_element_by_xpath("//*[@text = '提交']").click()  # 感谢您的反馈，我们会努力进步的
        print('视频反馈成功')

        # 投诉
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_video_more').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_report_video').click()
        self.driver.find_element_by_xpath("//*[@text = '违法违规']").click()
        swipe_up(self, 1500, 1)
        self.driver.find_element_by_id('com.nyc.ddup:id/et_phone').send_keys('16666667708')
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_submit').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_confirm').click()
        back(self)
        print('投诉成功了')

        # 退出播放
        sleep(5)
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_cancel').click()
        back(self)
        back(self)
        back(self)
        sleep(2)
        print('回到公益课程播放tab页')


    def teardown(self):
        sleep(5)
        self.driver.quit()
