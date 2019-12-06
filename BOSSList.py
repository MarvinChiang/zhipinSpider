from BOSSBase import *
from BOSSAnalysis import *
from selenium.webdriver.common.action_chains import ActionChains
from BOSSMongo import *
global workItem

def traversalList():#遍历招聘信息列表
    global itemFinished
    global workItem
    global itemFound
    thisListItem = 0
    browser.switch_to.window(browser.window_handles[-1])  # 保证控制最新标签页
    browser.execute_script('window.scrollBy(0,300)')#JS模拟滚轮300像素
    try:#CSS选择器不稳定
        work_links_ul = browser.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/ul')#full Xpath
        work_links_li = work_links_ul.find_elements_by_css_selector('li .info-primary .name')#没有.info-primary会按下公司超链接
    except:
        print('招聘信息列表找不到')
        return#直接停止跳出函数
    errorTimes =0
    ####已经成功找到了li,招聘列表页打开成功####
    worklinksli_num=len(work_links_li)#本页li计数器
    itemFound=itemFound+worklinksli_num#累计li计数器
    print('到该页已经找到',worklinksli_num,'/',itemFound)
    for worklink in work_links_li:#循环所有
        browser.switch_to.window(browser.window_handles[-1])#保证控制最新标签页
        if errorTimes == 10:
            print('遍历点击招聘信息列表  一直  出错')
            os._exit(0)#出错第10次直接停止跳出函数
        try:
            time.sleep(0.5)
            ActionChains(browser).move_to_element(worklink).click(worklink).perform()#click失败率非常高
        except:
            print('本次   遍历点击招聘信息列表出错',datetime.datetime.now(),browser.current_url)#返回当前时间,url)
            errorTimes = errorTimes+1
            time.sleep(2)
            continue
        browser.switch_to.window(browser.window_handles[-1])#保证控制最新标签页
        time.sleep(1.212)
        ########################
        get_products()#爬取整个页面，仅测试翻页可以注释掉
        ########################
        if needSaveMongo == True:
            save_to_mongo(workItem)  ####写入数据库####可注释
        ########################
        if len(browser.window_handles)==2:
            browser.switch_to.window(browser.window_handles[-1])#保证控制最新标签页
            browser.close()
        if len(browser.window_handles)>2:
            os._exit(0)#标签页受干扰停止
        browser.switch_to.window(browser.window_handles[-1])#保证控制最新标签页
        thisListItem=thisListItem+1
        print(thisListItem,'/本页共',worklinksli_num,'/累计',itemFinished,workItem)#已完成爬虫的网页数目
        itemFinished = itemFinished + 1
        workItem.clear()#清空字典
def main():
    traversalList()

if __name__=='__main__':
    main()