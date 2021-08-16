# coding=utf-8
from telnetlib import EC
from time import sleep, time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.android import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# QQ登录方法
from testcase.BasePage import back, swipe_up, swipe_down, swipe_left
from testcase.R_DDupCourse import is_login, qq_share
from testcase.DDupFind import work_comment

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

    # 我的模块
    def test_personalcenter(self):
        print('\n【个人中心】模块开始测试：')
        # 判断登录状态
        is_login(self, '16666667700')
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_user_home').click()
        # 修改个性签名
        print('开始修改个性签名')
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_edit_sign').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_clear').click()
        e1 = self.driver.find_element_by_id('com.nyc.ddup:id/et_sign').send_keys("备战高考，绝不松懈！")
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_save').click()
        assert "备战高考，绝不松懈！" in self.driver.find_element_by_id('com.nyc.ddup:id/tv_user_sign').text
        print('个性签名修改成功')

        # 个人主页
        print('*****开始测试个人主页')
        self.driver.find_element_by_id('com.nyc.ddup:id/cl_top').click()
        assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/iv_user_icon')) == 1
        assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/tv_name')) == 1
        name = self.driver.find_element_by_id('com.nyc.ddup:id/tv_name').text
        print('用户名是'+ name +'。')
        assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/tv_user_sign')) == 1
        sign = self.driver.find_element_by_id('com.nyc.ddup:id/tv_user_sign').text
        print('我的个性签名是' + sign)
        assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/tv_praise')) == 1
        praise = self.driver.find_element_by_id('com.nyc.ddup:id/tv_praise_count').text
        print('我获得了' + praise + '个赞。')
        assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/tv_attention')) == 1
        attention = self.driver.find_element_by_id('com.nyc.ddup:id/tv_attention_count').text
        print('我关注了' + attention + '个作者。')
        assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/tv_fans')) == 1
        fans = self.driver.find_element_by_id('com.nyc.ddup:id/tv_fans_count').text
        print('我有' + fans + '个粉丝。')
        # 动态列表  判断列表数量情况 1、空  2、不为空（分一页和多页情况）
        if len(self.driver.find_elements_by_id('com.nyc.ddup:id/tv_empty_tip')) == 1:
            print('该用户的动态列表为空')
        else:
            print('该用户动态列表不为空,点击进入动态详情页点赞点踩')
            if len(self.driver.find_elements_by_xpath("//*[@text = '没有更多了']")) == 1:
                self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').click()
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_unlike').click()
                work_comment(self, '不错不错')
                back(self)
            else:
                print('该用户动态列表超过一页,上滑查看更多数据')
                i = 0
                n = 1
                for i in range(10):
                    if len(self.driver.find_elements_by_xpath("//*[@text = '没有更多了']")) == 1:
                        print('动态列表下拉到底了')
                        self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').click()
                        sleep(2)
                        self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
                        self.driver.find_element_by_id('com.nyc.ddup:id/iv_unlike').click()
                        work_comment(self, '大写的赞')
                        back(self)
                        break
                    else:
                        swipe_up(self, 1000, n)
                        i += 1
                swipe_down(self, 500, i)

        # 个人主页--作品
        print('切换到作品页面')
        sleep(1)
        swipe_left(self, 1000, 1)
        # 作品列表  判断作品列表数量情况 1、空  2、不为空（分一页和多页情况）
        if len(self.driver.find_elements_by_xpath('//*[@text = "无内容"]')) == 1:
            print('该用户的作品为空')
        else:
            print('该用户作品列表不为空')
            if len(self.driver.find_elements_by_xpath("//*[@text = '没有更多了']")) == 1:
                self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').click()
                sleep(2)
                back(self)
            else:
                print('该用户作品超过一页，下滑查看更多数据')
                i = 0
                n = 1
                for i in range(10):
                    if len(self.driver.find_elements_by_xpath("//*[@text = '没有更多了']")) == 1:
                        print('作品列表下拉到底了')
                        self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').click()
                        sleep(2)
                        back(self)
                        break
                    else:
                        swipe_up(self, 1000, n)
                        i += 1
                swipe_down(self, 500, i)
        back(self)

        #  我赞过的
        print('*****开始测试我赞过的列表')
        self.driver.find_element_by_xpath("//*[@text ='我赞过的']").click()
        # 验证标题是否为 【我赞过的】
        assert len(self.driver.find_elements_by_xpath("//*[@text = '我赞过的']")) == 1
        # 我赞过列表 判断作品列表数量情况 1、空  2、不为空（分一页和多页情况）
        if len(self.driver.find_elements_by_xpath('//*[@text = "还没有赞过的内容，快去找好友互动吧～"]')) == 1:
            print('该用户的点赞列表为空，现在去【发现】点赞作品或者动态：')
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
            sleep(2)
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
            self.driver.find_element_by_xpath("//*[@text = '发现']").click()
            swipe_down(self, 1000, 3)
            T1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').text
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
            print('我点赞了作品：【' + T1 + '】')
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_user_home').click()
            self.driver.find_element_by_xpath("//*[@text ='我赞过的']").click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_dynamic_thumb').click()
            T2 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').text
            if T1 == T2:
                print("点赞ok,作品'" + T1 + "'成功加入到赞过的列表里")
            else:
                print(T1 + '点赞失败，未加入到赞过列表中')
            sleep(2)
            back(self)
            print('现在开始验证点赞数量显示是否正确')
            C1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_count').text
            print("我赞过的数量为%s" % C1)
            C1 = C1.replace('(', ' ')
            C1 = C1.replace(')', ' ')
            print(C1)
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_dynamic_thumb').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
            C2 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_count').text
            print("取消赞之后我赞过的数量为%s" % C2)
            C2 = C2.replace('(', ' ')
            C2 = C2.replace(')', ' ')
            assert int(C1) - int(1) == int(C2)
            print('赞过的列表数量正确')
        else:
            # 该用户点赞列表不为空，去发现模块点赞作品，然后验证点赞作品后是否显示在赞过的列表中
            print('该用户点赞列表不为空，去发现模块点赞作品：')
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
            sleep(2)
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
            self.driver.find_element_by_xpath("//*[@text = '发现']").click()
            swipe_down(self, 1000, 3)  # 下拉刷新
            t1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').text
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
            print('我点赞了作品：【' + t1 + '】')
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_user_home').click()
            self.driver.find_element_by_xpath("//*[@text ='我赞过的']").click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_dynamic_thumb').click()
            sleep(2)
            t2 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').text
            if t1 == t2:
                print("点赞ok,作品'" + t1 + "'成功加入到赞过的列表里")
            else:
                print(t1 + '点赞失败，未加入到赞过列表中')
            sleep(2)
            back(self)
            # 向上滑动查看更多赞过列表
            n = 1
            i = 0
            for i in range(10):
                if len(self.driver.find_elements_by_xpath("//*[@text = '没有更多了']")) == 1:
                    print('赞过列表已经到底了')
                    self.driver.find_element_by_id('com.nyc.ddup:id/iv_dynamic_thumb').click()
                    sleep(2)
                    back(self)
                    break
                else:
                    swipe_up(self, 1000, n)
                    i += 1
            swipe_down(self, 500, i)
            # 验证赞过的数量
            c1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_count').text
            print("我赞过的数量为%s" % c1)
            c1 = c1.replace('(', ' ')
            c1 = c1.replace(')', ' ')
            print(c1)
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_dynamic_thumb').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
            c2 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_count').text
            print("取消赞之后我赞过的数量为%s" % c2)
            c2 = c2.replace('(', ' ')
            c2 = c2.replace(')', ' ')
            assert int(c1) - int(1) == int(c2)
            print('赞过的列表数量正确')
        back(self)
        print('我赞过的列表测试通过。')

        # 我的动态
        sleep(5)
        print('*****开始测试我的动态模块：')
        self.driver.find_element_by_xpath("//*[@text = '我的动态']").click()
        # 判断我的动态列表数量情况 1、空  2、不为空（分一页和多页情况）
        if len(self.driver.find_elements_by_xpath("//*[@text = '空空如也，快去发布上传动态吧～']")) >= 1:
            print('该用户的动态为空，接下来发布文本动态')
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_create_dynamic').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/et_content').send_keys('站在痛苦之外规劝受苦的人，是件很容易的事。(《被缚的普罗米修斯》)')
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_issue').click()
            assert len(self.driver.find_elements_by_xpath("//*[@text = '站在痛苦之外规劝受苦的人，是件很容易的事。(《被缚的普罗米修斯》)']")) >= 1
            print('文本动态发布成功')
            # 动态详情操作
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').click()
            assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/tv_time')) == 1
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_unlike').click()
            print('点踩成功')
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
            print('点赞成功')
            # 发布评论
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_comment').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/et_content').send_keys("抢自己的沙发，第一次发布动态评论")
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_send').click()
            assert len(self.driver.find_elements_by_xpath("//*[@text = '抢自己的沙发，第一次发布动态评论']")) == 1
            print('评论成功')
            # 给评论点赞以及回复评论
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_comment').click()
            self.driver.find_element_by_xpath("//*[@text = '回复评论']").send_keys('第一次回复你的消息，加油')
            self.driver.find_element_by_xpath("//*[@text = '发送']").click()
            assert len(self.driver.find_elements_by_xpath("//*[contains(@text,'第一次回复你的消息，加油')]")) == 1
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_close').click()
            print('回复评论以及点赞评论成功')
            # QQ分享
            print('动态分享到QQ：')
            qq_share(self)
            # 删除动态
            d1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_content')
            TouchAction(self.driver).long_press(d1).perform()
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_delete').click()
            assert len(self.driver.find_elements_by_xpath("//*[@text = '空空如也，快去发布上传动态吧～']")) == 1
            print('刚刚发布的动态已删除了')
            sleep(2)
            back(self)
        else:
            print('该用户的动态不为空')
            i = 0
            n = 1
            for i in range(10):
                if len(self.driver.find_elements_by_xpath("//*[@text = '没有更多了']")) == 1:
                    print('动态列表下拉到底了')
                    self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').click()
                    if len(self.driver.find_elements_by_xpath("//*[@text = '审核中']")) == 1:
                        print('该动态处于审核中')
                    else:
                        print('该动态的状态为已通过审核')
                        self.driver.find_element_by_id('com.nyc.ddup:id/iv_unlike').click()
                        self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
                        w1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_comment_num').text
                        if int(w1) == 0:
                            self.driver.find_element_by_id('com.nyc.ddup:id/iv_comment').click()
                            self.driver.find_element_by_xpath("//*[@text = '快来发布你的评论…']").send_keys("我给自己的动态发布评论了")
                            self.driver.find_element_by_xpath("//*[@text = '发送']").click()
                            assert len(self.driver.find_elements_by_xpath("//*[@text = '我给自己的动态发布评论了']")) == 1
                            self.driver.find_element_by_id('com.nyc.ddup:id/iv_close').click()
                            print('第一个发布评论成功，点赞成功，点踩成功')
                        else:
                            self.driver.find_element_by_id('com.nyc.ddup:id/iv_comment').click()
                            self.driver.find_element_by_xpath("//*[@text = '快来发布你的评论…']").click()
                            self.driver.find_element_by_xpath("//*[@text = '快来发布你的评论…']").send_keys('拍的真好，我也来评论了')
                            self.driver.find_element_by_xpath("//*[@text = '发送']").click()
                            assert len(self.driver.find_elements_by_xpath("//*[@text = '拍的真好，我也来评论了']")) == 1
                            self.driver.find_element_by_id('com.nyc.ddup:id/iv_close').click()
                            print('再次发布评论成功，点赞成功，点踩成功')
                        # QQ分享
                        print('动态分享到QQ：')
                        qq_share(self)
                    sleep(2)
                    back(self)
                    break
                else:
                    swipe_up(self, 1000, n)
                    print('动态列表下拉了一次')
                    i += 1
            swipe_down(self, 500, i)

            # 发布动态
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_create_dynamic').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/et_content').send_keys('站在痛苦之外规劝受苦的人，是件很容易的事。(《被缚的普罗米修斯》)')
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_issue').click()
            assert len(self.driver.find_elements_by_xpath("//*[@text = '站在痛苦之外规劝受苦的人，是件很容易的事。(《被缚的普罗米修斯》)']")) >= 1
            print('文本动态发布成功')
            # 动态详情操作
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').click()
            assert len(self.driver.find_elements_by_id('com.nyc.ddup:id/tv_time')) == 1
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_unlike').click()
            print('点踩成功')
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
            print('点赞成功')
            # 发布评论
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_comment').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/et_content').send_keys("第一次评论，已收藏了")
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_send').click()
            assert len(self.driver.find_elements_by_xpath("//*[@text = '第一次评论，已收藏了']")) == 1
            print('评论成功')
            # 给评论点赞以及回复评论
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_comment').click()
            self.driver.find_element_by_xpath("//*[@text = '回复评论']").send_keys('第一次回复你的消息，加油')
            self.driver.find_element_by_xpath("//*[@text = '发送']").click()
            assert len(self.driver.find_elements_by_xpath("//*[contains(@text,'第一次回复你的消息，加油')]")) == 1
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_close').click()
            print('回复评论以及点赞评论成功')
            sleep(2)
        back(self)
        print("我的动态列表测试通过。")

    # 我的作品"""
    def test_works(self):
        print('\n*****开始测试我的作品')
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_user_home').click()
        self.driver.find_element_by_xpath("//*[@text = '我的作品']").click()
        # 作品列表测试 1、空  2、不为空，分一页（审核中 审核通过）和多页情况（审核中 审核通过）
        if len(self.driver.find_elements_by_xpath("//*[@text= '空空如也，快去发上传作品吧～']")) == 1:
            print('该用户作品列表为空，开始发布第一个作品 ')
            # 发布作品
            self.driver.find_element_by_xpath("//*[@text = '创作投稿']").click()
            # 默认选择手机最新的一个视频
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_image').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_complete').click()
            self.driver.find_element_by_xpath("//*[@text = 'UP学长说']").click()
            self.driver.find_element_by_xpath("//*[@text='给你的作品写个标题吧～']"). \
                send_keys('我的新作品，请欢迎查看。')
            self.driver.find_element_by_xpath("//*[@text = '发布']").click()
            sleep(10)
            print('作品发布成功')
            # 验证刚刚发布的作品是否为审核中
            self.driver.find_element_by_xpath("//*[@text = '我的新作品，请欢迎查看。']").click()
            assert len(self.driver.find_elements_by_xpath("//*[@text = '审核中']")) == 1
            w2 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_unlike_num').text
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_unlike').click()
            w3 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_unlike_num').text
            assert w2 == w3
            print('刚刚发布的作品处于审核中')
            # 删除作品
            w4 = self.driver.find_element_by_id('com.nyc.ddup:id/exo_subtitles')
            TouchAction(self.driver).long_press(w4).perform()
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_delete').click()
            print('作品删除成功')
            back(self)
        else:
            print('该用户的作品列表不为空')
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').click()
            if len(self.driver.find_elements_by_xpath("//*[@text = '审核中']")) == 1:
                print('该作品处于审核中')
            else:
                print('该作品的状态为已通过审核')
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_unlike').click()
                self.driver.find_element_by_id('com.nyc.ddup:id/iv_like').click()
                work_comment(self, '作品不错')
                # QQ分享
                print('分享功能测试')
                qq_share(self)
                sleep(2)
                back(self)
                i = 0
                n = 1
                for i in range(10):
                    if len(self.driver.find_elements_by_xpath("//*[@text = '没有更多了']")) == 1:
                        print('作品列表到底了')
                    else:
                        swipe_up(self, 1000, n)
                        print('作品列表下拉了一次')
                        i += 1
                swipe_down(self, 1000, i)

            # 发布作品
            back(self)
            print('测试发布作品')
            self.driver.find_element_by_xpath("//*[@text = '创作投稿']").click()
            # 默认选择手机最新的一个视频
            self.driver.find_element_by_id('com.nyc.ddup:id/iv_image').click()
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_complete').click()
            self.driver.find_element_by_xpath("//*[@text = 'UP学长说']").click()
            self.driver.find_element_by_xpath("//*[@text='给你的作品写个标题吧～']"). \
                send_keys('我的新作品，请欢迎查看。')
            self.driver.find_element_by_xpath("//*[@text = '发布']").click()
            sleep(10)
            print('作品发布成功')
            # 查看刚刚发布的作品是否为审核中
            self.driver.find_element_by_xpath("//*[@text = '我的新作品，请欢迎查看。']").click()
            sleep(2)
            assert len(self.driver.find_elements_by_xpath("//*[@text = '审核中']")) == 1
            print('刚刚发布的作品处于审核中')
            # 删除作品
            w4 = self.driver.find_element_by_id('com.nyc.ddup:id/exo_subtitles')
            TouchAction(self.driver).long_press(w4).perform()
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_delete').click()
            print('作品删除成功')
            sleep(2)
            back(self)
            sleep(2)
            back(self)
            print('我的作品模块完成测试')

        # 关注/粉丝
        print('\n*****开始测试关注/粉丝列表')
        self.driver.find_element_by_xpath("//*[@text = '关注/粉丝']").click()
        if len(self.driver.find_elements_by_xpath("//*[@text ='无内容']")) == 1:
            print('关注列表为空')
        else:
            print('关注列表不为空')
            self.driver.find_element_by_xpath("//*[@text = '已关注']").click()
            assert len(self.driver.find_elements_by_xpath("//*[@text ='+ 回关']")) == 1 or \
                   len(self.driver.find_elements_by_xpath("//*[@text ='+ 关注']")) == 1

        # 在发现模块关注用户，查看用户是否在关注列表里
        back(self)
        sleep(5)
        back(self)
        self.driver.find_element_by_xpath("//*[@text = '发现']").click()
        swipe_down(self, 500, 1)
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_cover').click()
        n = 1
        for n in range(50):
            if len(self.driver.find_elements_by_id("com.nyc.ddup:id/tv_focus_btn")) == 1:
                self.driver.find_element_by_id("com.nyc.ddup:id/tv_focus_btn").click()
                name1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_user_name').text
                break
                back(self)
            else:
                swipe_up(self, 500, n)
                sleep(2)
        sleep(2)
        back(self)
        sleep(2)
        back(self)
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_user_home').click()
        self.driver.find_element_by_xpath("//*[@text = '关注/粉丝']").click()
        name2 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_user_name').text
        assert name1 == name2
        print('关注用户[%s]成功' % name1)

        # 粉丝列表
        sleep(5)
        swipe_left(self, 1000, 1)
        if len(self.driver.find_elements_by_xpath("//*[@text ='无内容']")) == 1:
            print('粉丝列表为空')
        else:
            print('粉丝列表不为空')
        sleep(2)
        back(self)

        print('\n*****开始测试设置')
        # 家长监管
        self.driver.find_element_by_xpath("//*[@text = '家长监管']").click()
        assert len(self.driver.find_elements_by_xpath("//android.widget.Image[@content-desc='wxcode.78386401']")) == 1
        self.driver.keyevent(4)
        # 意见反馈
        self.driver.find_element_by_xpath("//*[@text = '意见反馈']").click()
        self.driver.find_element_by_id('com.nyc.ddup:id/et_feedback_message').send_keys('版本测试中，请忽略该条反馈')
        self.driver.find_element_by_id('com.nyc.ddup:id/et_phone').send_keys('166666667733')
        self.driver.find_element_by_id('com.nyc.ddup:id/et_qq_number').send_keys('2578613446')
        self.driver.find_element_by_id('com.nyc.ddup:id/et_email').send_keys('2578613446@qq.com')
        self.driver.find_element_by_xpath("//*[@text = '提交']").click()
        assert len(self.driver.find_elements_by_xpath("//*[@text='反馈成功']")) == 1
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_confirm').click()
        print('意见反馈成功')
        # 设置
        print('*****开始测试模块【设置】')
        self.driver.find_element_by_xpath("//*[@text = '设置']").click()
        # 修改昵称
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_username').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/et_name').send_keys('七七姗姗')
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_save').click()
        assert len(self.driver.find_elements_by_xpath("//*[@text = '七七姗姗']")) == 1
        # QQ账号绑定
        if len(self.driver.find_elements_by_xpath(
                "//*[@resource-id = 'com.nyc.ddup:id/tv_qq_bind'][@text = '去绑定']")) == 1:
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_qq_bind').click()
            self.driver.find_element_by_xpath("//*[@text = '授权登录']").click()
            print('QQ号绑定成功')

        else:
            print("该账号QQ已绑定")
        # 微信号绑定(取消绑定)
        if len(self.driver.find_elements_by_xpath(
                "//*[@resource-id = 'com.nyc.ddup:id/tv_wx_bind'][@text = '去绑定']")) == 1:
            self.driver.find_element_by_id('com.nyc.ddup:id/tv_wx_bind').click()
            self.driver.find_element_by_id('com.tencent.mm:id/ei').click()
            print('微信号未绑定 已取消微信号绑定了')
        else:
            print("该账号微信号已绑定")
        # 消息推送设置 个性化服务设置
        self.driver.find_element_by_id('com.nyc.ddup:id/message_push_switch').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/personal_service_switch').click()
        # 关于我们
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_about_us').click()
        assert len(self.driver.find_elements_by_xpath("//*[@content-desc= 'Version 1.1.7']")) == 1
        self.driver.find_element_by_xpath("//*[@content-desc= '检查更新']").click()
        e1 = self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']").text
        print(e1)
        self.driver.keyevent(4)
        print('关于我们测试完成')
        # 清理缓存
        if len(self.driver.find_elements_by_id('com.nyc.ddup:id/ll_clean_cache')) == 1:
            self.driver.find_element_by_id('com.nyc.ddup:id/ll_clean_cache').click()
            self.driver.keyevent(4)
        else:
            swipe_up(self, 500, 1)
            self.driver.find_element_by_id('com.nyc.ddup:id/ll_clean_cache').click()
            self.driver.keyevent(4)
        print('缓存清理完成')
        # 隐私与安全
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_privacy_security').click()
        # 用户协议网页
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_user_agreement').click()
        assert len(self.driver.find_elements_by_xpath("//*[@content-desc= 'DDup用户服务协议']")) == 1
        swipe_up(self, 500, 3)
        self.driver.keyevent(4)
        # 隐私政策网页
        self.driver.find_element_by_id('com.nyc.ddup:id/ll_privacy_policy').click()
        assert len(self.driver.find_elements_by_xpath("//*[@content-desc= 'DDup用户隐私政策']")) == 1
        swipe_up(self, 500, 4)
        self.driver.keyevent(4)
        print('隐私与安全测试完成')
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
        sleep(3)
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_back').click()
        print("设置模块测试完成")
        # 注销账号

    def test_daka(self):
        # # switch to webview
        # webview = self.driver.contexts.last
        # self.driver.switch_to.context(webview)
        # # do some webby stuff
        # self.driver.find_element(:css, '.green_button').click
        # #switch to back native view
        # self.driver.switch_to.context(self.driver.contexts.first)

        self.driver.find_element_by_xpath("//*[@text = '大咖说']").click()

        # 合辑页面滑动
        n = 1
        for n in range(10):
            swipe_up(self, 500, n)
            if len(self.driver.find_elements_by_xpath("//*[@text = '没有更多了']")) == 1:
                print('已经到底了')
                break
            else:
                n += 1
        print(self.driver.contexts)
