from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re
from pyquery import PyQuery as pq
import os
import time
import  pymongo
import datetime

####前期浏览器操作####
chrome_options = Options()#chromeOptions 是一个配置 chrome 启动属性的类
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
try:
    chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
except:
    print('chromedriver.exe在该路径下无法找到，请修改此处代码或移动文件')
    #建议符合chrome版本的chromedriver.exe和chrome.exe在同一文件夹下
browser = webdriver.Chrome(chrome_driver, options=chrome_options)

####参数设置####
couldNext = 1#判断标记
itemFinished =1#计数器
itemFound=0#计数器
workItem={}#空字典
wait = WebDriverWait(browser, 10)#网速慢所以最多让网页加载10秒
#######################################################################################
global MONGO_DB
global MONGO_TABLE
global needSaveMongo#是否保存数据库
needSaveMongo=False
MONGO_DB='JAVA'
MONGO_TABLE = 'HaiDian'
#######################################################################################