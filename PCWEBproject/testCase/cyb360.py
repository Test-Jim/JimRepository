#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest,time
from selenium import webdriver
from commonFunction.commonClass import commonClass
from selenium.webdriver.support.ui import WebDriverWait
from commonFunction.log_print import logPrint
from commonFunction.configini import configini
import logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class seleniumTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        logPrint("seleniumTest.log")
        self.url=configini('brower','url')
        self.user=configini('brower','user')
        self.password=configini('brower','password')
        # self.driver=webdriver.Remote(command_executor='http://192.168.0.4:5555/wd/hub',
        #                              desired_capabilities={'platform': 'ANY',
        #                                 'browserName':'chrome',
        #                                 'version': '',
        #                                 'javascriptEnabled': True
        #                                 })

        self.driver=webdriver.Chrome()

        self.driver.get(self.url)

    def test_Ageturl(self):
        self.driver.execute_script("$('.lb').click();")
        WebDriverWait(self.driver,10).until(lambda dr: dr.find_element_by_id('TANGRAM__PSP_2__titleText').is_displayed())
        self.driver.execute_script("$('#TANGRAM__PSP_8__userName').val('%s');$('#TANGRAM__PSP_8__password').val('%s');"
                                   %(self.user,self.password))
        self.driver.find_element_by_id('TANGRAM__PSP_8__submit').click()
        time.sleep(5)


    def test_Blogin(self):
        pass
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

# if __name__ == '__main__':
#     unittest.main()
