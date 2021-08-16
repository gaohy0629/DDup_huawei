# coding=utf-8
from telnetlib import EC
from time import sleep, time
from venv import logger

from appium.webdriver.common.touch_action import TouchAction
from pip._internal.utils import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.android import webdriver
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from testcase.BasePage import is_toast2, swipe_up


class TestDDup:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['version'] = '6.0'
        caps['deviceName'] = 'XSENW19B29002179'
        caps['appPackage'] = 'com.nyc.ddup'
        caps['appActivity'] = '.activity.SplashActivity'
        caps['noReset'] = 'True'
        # caps['automationName'] = 'uiautomator1'
        caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def test_comment(self):
        self.driver.find_element_by_xpath("//*[@text = '发现']").click()
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_dynamic_text').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_comment').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/et_content').send_keys('学到了')
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_send').click()
        # loc1 = self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']").text
        # print('\n第一个评论发布成功，Toast提示 ' + loc1)
        is_toast2(self, '成')
        e1 = self.driver.find_element_by_id('com.nyc.ddup:id/tv_comment_content')
        TouchAction(self.driver).long_press(e1).perform()
        self.driver.find_element_by_id('com.nyc.ddup:id/tv_item').click()
        is_toast2(self, '除')

        # 第一种方式 √
        # loc3 = self.driver.find_element_by_xpath("//*[@class = 'android.widget.Toast']").text
        # print('第一个评论发布成功，Toast提示 ' + loc3)

        # 第二种
        # el = self.driver.find_element_by_xpath("//*[contains(@text, '删除')]").text
        # print(el)

    def test_picture(self):
        self.driver.find_element_by_xpath("//*[@text = '高校通览']").click()
        self.driver.find_element_by_xpath("//*[@text = '清华大学']").click()
        sleep(3)
        swipe_up(self, 1000, 2)
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_photo_3').click()
        self.driver.find_element_by_id('com.nyc.ddup:id/iv_download').click()
        is_toast2(self, '保存')
