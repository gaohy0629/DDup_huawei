# coding=utf-8
from time import sleep, time


from selenium.webdriver.android import webdriver
from appium import webdriver

from testcase.BasePage import is_activity_frame, is_login, swipe_down, back, work_comment, qq_share, swipe_up, login


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


    def test_find(self):
        print('\n测试【发现】模块')
        # 查看是否有启动页
        is_activity_frame(self)
        # 判断登录状态
        is_login(self, '16666667733')
        print('开始测试发现下的广场： ')
        self.driver.find_element_by_xpath("//*[@text = '发现']").click()
        # 下拉刷新
        sleep(5)
        swipe_down(self, 1000, 1)
        # 作品列表页第一个作品操作：作品点赞，查看个人主页
        t1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_like_num').text
        print('列表第一个作品的获赞数为 ' + t1)
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
        t2 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_like_num').text
        assert t1 != t2
        print('对作品点赞成功')
        t3 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_user_name').text
        print('该作品的作者是 ' + t1)
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_user_icon').click()
        t4 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_name').text
        assert t3 == t4
        back(self)
        print('成功进入作者个人主页')

        # 切换作品分类
        self.driver.find_element_by_xpath("//*[@text = 'UP微课堂']").click()
        print('切换分类正常')
        # 进入作品详情页
        t7 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').text
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_cover').click()
        sleep(1)
        t8 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').text
        assert t7 == t8
        print('成功进入作品详情页')
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_unlike').click()
        # 作品发布评论
        work_comment(self, '很赞')
        # 作品分享
        qq_share(self)
        # 关注
        try:
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_focus_btn').click()
            gz = self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']").text
            print("Toast提示" + gz)
        except:
            print('已经关注过作者了')
        # 上下滑动作品详情
        swipe_down(self, 500, 1)
        # hd = self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']").text
        # print("Toast提示" + hd)
        swipe_up(self, 500, 3)
        t9 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').text
        assert t9 != t8
        print('上下滑动作品详情页正常')
        back(self)
        # 作品列表滑动
        sleep(3)
        swipe_up(self, 1000, 3)
        back(self)
        print('回到首页，【广场】模块测试完成！')

        print('开始测试发现广场下的关注： ')
        self.driver.find_element_by_xpath("//*[@text = '发现']").click()
        self.driver.find_element_by_xpath("//*[@text = '关注']").click()
        try:
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_login_btn').click()
            login(self)
            print('登录账号成功')
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_unlike').click()
            work_comment(self, '真实的教育')
            qq_share(self)
            back(self)
            t1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_see_num').text
            print('该条动态的观看人数是' + t1)
        except:
            print('已经登录了')
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_unlike').click()
            work_comment(self, '真实的教育')
            qq_share(self)
            back(self)
            t1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_see_num').text
            print('该条动态的观看人数是' + t1)
        # 发布动态
        print('发布动态')
        self.driver.find_element_by_id('com.nyc.ddup:id/ic_add_dynamic').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/et_content').send_keys('你是沿途，有青山举杯')
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_tag_name').click()  # 进入选择话题
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_root').click()  # 选择话题
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_add_media').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_choose_album').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_select').click()  # 默认取相册第一张图片
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_complete').click()
        self.driver.find_element_by_xpath("//*[@text = '发布']").click()
        assert len(self.driver.find_elements_by_xpath("//*[@text = '你是沿途，有青山举杯']")) >= 1
        print('文本+图片动态发布成功')
        sleep(3)
        # 查看动态详情页
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').click()
        # 动态详情页面各元素是否存在
        assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/iv_user_icon')) >= 1
        assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/tv_user_name')) >= 1
        assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/tv_time')) >= 1
        back(self)
        sleep(3)
        # 话题详情页
        t1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_tag_name').text
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_tag_name').click()
        t2 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_topic').text
        assert t1 == t2
        print('正确进入话题【' + t2 + '】详情页中')
        t3 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_see_num').text
        print('话题' + t1 + '浏览次数是' + t3)
        swipe_down(self, 1000, 1)
        t4 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_see_num').text
        print(t4)
        print('话题浏览数正常')
        # 立即发布
        self.driver.find_element_by_xpath("//*[@text = '立即发布']").click()
        sleep(5)
        t5 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_tag_name').text
        assert t1 == t5
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_cancel').click()
        back(self)
        sleep(3)
        back(self)

    def test_teardown(self):
        sleep(5)
        self.driver.quit()





