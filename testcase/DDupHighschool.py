# coding=utf-8

from time import sleep, time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.android import webdriver
from appium import webdriver

from testcase.BasePage import swipe_up, qq_share, is_activity_frame, is_login


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

    # 高校通览
    def test_highschool(self):
        is_activity_frame(self)
        # 判断登录状态
        is_login(self, '16666667788')
        print('\n 开始测试【高校通览】模块：')
        self.driver.find_element_by_xpath("//*[@text = '高校通览']").click()
        assert len(self.driver.find_elements_by_xpath("//*[@text = '大学名录']")) == 1
        # 用例以中国传媒大学为例
        i = 0
        n = 1
        for i in range(10):
            if len(self.driver.find_elements_by_xpath("//*[@text = '中国传媒大学']")) == 1:
                print('点击进入中国传媒大学')
                self.driver.find_element_by_xpath("//*[@text = '中国传媒大学']").click()
                sleep(2)
                assert len(self.driver.find_elements_by_xpath("//*[@text = '中国传媒大学']")) == 1
                assert len(self.driver.find_elements_by_id("com.nyc.ddup:id/iv_school_icon")) == 1
                # 大学详情分享
                print('大学详情页分享')
                qq_share(self)

                # 播放校园Vlog
                print('校园Vlog')
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_play').click()
                # self.driver.find_element_by_id('com.nyc.ddup:id/exo_pause').click()
                # self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
                self.driver.keyevent(4)

                # 学校官网和招生办
                print('查看学校官网和招生办')
                self.driver.find_element_by_id('com.nyc.ddup:id/ll_school_web').click()
                sleep(2)
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
                self.driver.find_element_by_id('com.nyc.ddup:id/ll_admission_office').click()
                sleep(2)
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()

                # 校园Vlog
                print('校园Vlog')
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_cover').click()
                sleep(2)
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_unlike').click()
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
                self.driver.find_element_by_xpath("//*[@text ='更多']").click()
                swipe_up(self, 1000, 1)
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_cover').click()
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_unlike').click()
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
                print('Vlog投诉')
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_more').click()
                self.driver.find_element_by_xpath("//*[@text = '投诉']").click()
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_violate_law_rule').click()
                swipe_up(self, 1000, 1)
                self.driver.find_element_by_id('com.nyc.ddup:id/tv_submit').click()
                self.driver.find_element_by_id('com.nyc.ddup:id/tv_confirm').click()

                print('Vlog下QQ分享功能测试')
                qq_share(self)
                swipe_up(self, 1000, 3)
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
                sleep(2)
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()

                # 校园图集
                print('校园图集测试')
                swipe_up(self, 1000, 1)
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_photo_3').click()
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_download').click()
                pic = self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']").text
                print('Toast提示' + pic)
                sleep(2)
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()

                # 校园问一问
                print('问一问')
                self.driver.find_element_by_id('com.nyc.ddup:id/tv_question_content').click()
                self.driver.find_element_by_id('com.nyc.ddup:id/tv_edit_answer').click()
                self.driver.find_element_by_id('com.nyc.ddup:id/et_content').send_keys('好吃又便宜')
                self.driver.find_element_by_id('com.nyc.ddup:id/tv_send').click()
                assert len(self.driver.find_elements_by_xpath("//*[@text = '好吃又便宜']")) == 1
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
                a1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_content')
                TouchAction(self.driver).long_press(a1).perform()
                self.driver.find_element_by_xpath("//*[@text = '删除']").click()
                d1 = self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']").text
                print('Toast提示' + d1)
                assert len(self.driver.find_elements_by_xpath("//*[@text = '还没有回答，快来抢沙发～']")) == 1
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
                self.driver.find_element_by_xpath("//*[@text ='更多']").click()
                self.driver.find_element_by_xpath("//*[@text ='发起提问']").click()
                self.driver.find_element_by_id('com.nyc.ddup:id/tv_cancel').click()
                print('取消提问')
                sleep(1)
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
                sleep(2)
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
                print('高校通览大学详情页测试通过')
                break
            else:
                swipe_up(self, 500, n)
                i += 1
        # 大学名录页面
        print('大学名录检索测试')
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_area').click()
        self.driver.find_element_by_xpath("//*[@text = '广东']").click()
        assert len(self.driver.find_elements_by_xpath("//*[@text = '中山大学']")) == 1
        print('大学名录检索测试ok')
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_type').click()
        self.driver.find_element_by_xpath("//*[@text = '综合类']").click()
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_level').click()
        self.driver.find_element_by_xpath("//*[@text = '985']").click()
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_batch').click()
        self.driver.find_element_by_xpath("//*[@text = '本科']").click()
        assert len(self.driver.find_elements_by_xpath("//*[@text = '深圳大学']")) == 1 and \
               len(self.driver.find_elements_by_xpath("//*[@text = '中山大学']")) == 1
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_batch').click()
        self.driver.find_element_by_xpath("//*[@text = '专科']").click()
        assert len(self.driver.find_elements_by_xpath("//*[@text = '没有符合条件的大学']")) == 1
        print('高校通览地区搜索功能ok')

        self.driver.find_element_by_id('com.nyc.ddup:id/iv_search_icon').click()
        self.driver.find_element_by_xpath("//*[@text = '请输入学校名称']").send_keys('安徽大学')
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_school_name').click()
        assert len(self.driver.find_elements_by_xpath("//*[@text = '安徽大学']")) >= 1
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_clear').click()
        assert len(self.driver.find_elements_by_xpath("//*[@text = '无内容']")) == 1
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_cancel').click()
        assert len(self.driver.find_elements_by_xpath("//*[@text = '没有符合条件的大学']")) == 1
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
        self.driver.find_element_by_xpath("//*[@text = '高校通览']").click()
        assert len(self.driver.find_elements_by_xpath("//*[@text = '清华大学']")) == 1
        print('搜索功能测试ok')
        print('【高校通览】模块测试通过')
