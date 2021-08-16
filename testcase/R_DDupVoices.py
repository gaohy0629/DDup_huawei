# coding=utf-8
from telnetlib import EC
from time import sleep, time

from selenium.webdriver.android import webdriver
from appium import webdriver

# QQ登录方法
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from testcase.R_DDupCourse import is_login


def third_login(self):
    sleep(2)
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_user_home').click()
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_check_btn').click()
    self.driver.keyevent(4)
    self.driver.find_element_by_id('com.nyc.ddup:id/iv_login_qq').click()
    self.driver.find_element_by_id('com.tencent.mobileqq:id/fds').click()
    print("QQ登录成功")


# 上滑查看内容
def swipe_up(self, t, n):
    sleep(2)
    L = self.driver.get_window_size()
    x1 = L['width'] * 0.5
    y1 = L['height'] * 0.8
    y2 = L['height'] * 0.25
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

    # 开始测试万卷有声
    def test_voices(self):
        # 判断登录状态
        is_login(self, '16666667777')
        print('\n*****开始测试【万卷有声】模块：')
        self.driver.find_element_by_xpath("//*[@text = '万卷有声']").click()
        # 判断万卷有声标题收听量 简介显示是否正确
        if len(self.driver.find_elements_by_xpath("//*[@text = '青缃集•岑小岑教育悦读']")) == 1:
            print('万卷有声栏目标题正确')
        assert len(self.driver.find_elements_by_id("com.nyc.ddup:id/tv_count")) == 1
        v1 = self.driver.find_element_by_id("com.nyc.ddup:id/tv_count").text
        print('万卷有声收听量字段显示正确' + v1)
        assert len(self.driver.find_elements_by_xpath('//*[@text = "简介：读美文，读世界，读人生。含英咀华，破茧成蝶！"]')) == 1
        print('万卷有声简介显示正确')

        # 声音列表滑动正常
        print('声音列表测试')
        i = 0
        n = 1
        for i in range(10):
            if len(self.driver.find_elements_by_id('com.nyc.ddup:id/load_hint_view')) == 1:
                print('声音列表已经到底了')
                break
            else:
                swipe_up(self, 1000, n)
                print('又一次上滑了声音列表')
                i += 1
        swipe_down(self, 1000, i)

        # 判断单个声音的收听量是否正确
        print('收听量测试：')
        swipe_down(self, 1000, 1)
        sleep(1)
        s1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_listen_num').text
        print('收听量原来值是%s' % s1)
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_cover').click()
        sleep(2)  # 目的是等待一段时间后让声音详情全部加载出来
        self.driver.keyevent(4)  # 手机返回键
        sleep(1)
        swipe_down(self, 1000, 1)
        s2 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_listen_num').text
        print('收听量现在是%s' % s2)
        assert int(s1) + 2 == int(s2) or int(s1) + 1 == int(s2)
        print('收听量正确')

        # 声音列表下的播放条
        sleep(1)
        assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/blur_layout')) == 1
        assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/tv_play_progress')) == 1
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_play_pause').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_close').click()
        assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/iv_close')) != 1
        print('声音列表下的播放进度显示正常，栏目页测试通过')

        # 声音详情页
        print('声音详情页测试')
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_cover').click()
        sleep(2)
        self.driver.find_element_by_accessibility_id("鉴赏").click()
        if len(self.driver.find_elements_by_accessibility_id("【赏·涵泳志】")) == 1:
            print('点击鉴赏正确跳转到了鉴赏文稿页')

        i = 0
        n = 1
        for i in range(10):
            if len(self.driver.find_elements_by_accessibility_id("写评论")) == 1:
                print('页面已经下拉到底了')
                break
            else:
                swipe_up(self, 1000, n)
                i += 1
        assert len(self.driver.find_elements_by_accessibility_id("写评论")) == 1
        print('点击评论正确跳转到了评论页')
        # 发布评论待开发  self.driver.find_element_by_accessibility_id('写评论').click()

        self.driver.find_element_by_id('com.nyc.ddup:id/iv_play_pause').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_play_pause').click()
        i = 0
        n = 1
        for i in range(10):
            if len(self.driver.find_elements_by_accessibility_id('岑小岑')) == 1:
                print('声音详情页已经上滑到顶部了')
                break
            else:
                swipe_down(self, 500, n)
                i += 1

        assert len(self.driver.find_elements_by_accessibility_id('s3')) == 1
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_prev').click()
        s4 = self.driver.find_element_by_accessibility_id('散文-春回（作者：席慕蓉）').text
        print(s4)
        print('上一个按钮可以正常切换')
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_next').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_voice_list').click()
        swipe_up(self, 1000, 1)
        self.driver.find_element_by_xpath("//*[@text = '14']").click()
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_cancel').click()
        if len(self.driver.find_elements_by_accessibility_id("散文-我们仨（第二部：2.古驿道上相聚 下）（作者：杨绛）")) == 1:
            print("播放列表切换播放正常")
        # 声音分享到QQ
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_share').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/layout_share_qq').click()
        self.driver.find_element_by_id('com.tencent.mobileqq:id/text1').click()
        self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        self.driver.find_element_by_xpath("//*[@text = '返回DDup']").click()
        self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']")
        s5 = self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']").text
        print('Toast提示' + s5)
        # 分享到手机qq后打印toast
        # loc = '//*[contains(@text,"{}")]'.format("分享成功")
        # try:
        #     WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_elements_located((By.XPATH, loc)))
        #     e1 = self.driver.find_element_by_xpath(loc).text
        #     print(e1)
        # except:
        #     print('没有找到匹配的toast！')

    def teardown(self):
        sleep(5)
        self.driver.quit()