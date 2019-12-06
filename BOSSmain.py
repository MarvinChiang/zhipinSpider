from BOSSnextpage import *
#CMD输入##chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenium\AutomationProfile" ##
#进入招聘列表，建议手动筛选要求，列表最多10页300条
global needSaveMongo
def main():
    if  needSaveMongo==True:
        print("启用MongoDB-->保存的数据库为："+MONGO_DB + "  数据表为:" + MONGO_TABLE+"  可在BOSSBase.py中修改")
    else:
        print("不保存数据库 可在BOSSBase.py中修改")

    if len(browser.window_handles) != 1:
        print("被chromedriver控制的独立Chrome的标签页应该有且仅有1页:  即简略的信息列表页")
        os._exit(0)
    browser.refresh()
    print("START... ")

    traversalANDnextPage()


if __name__=='__main__':
    main()

#README

###########################################
#简单的  BOSS直聘  爬虫演示。仅作自娱自乐学习交流，可以挂代理节点
#是否使用mongoDB数据库在BOSSBase.py 中设置,默认不使用
#1.启动bat文件，打开独立chrome，进入网站https://www.zhipin.com/，
#鼠标人工点击进入招聘列表。web页面 列表最多显示10页300条。
#2.建议手动筛选要求
#确保只有一个窗口一个标签页
#网址举例:https://www.zhipin.com/c101010100-p100101/b_%E6%9C%9D%E9%98%B3%E5%8C%BA/?ka=sel-business-0
#3.run  BOSSmain.py
#############################################

# 前期初始化[BOSSBase]
# main调用traversalANDnextPage()[BOSSmain]
# traversalANDnextPage()调用traversalList()&nextPage()    nextPage()调用getpagenow()[BOSSnextpage]
# traversalList()调用get_products() & save_to_mongo()[BOSSList]

#简单的使用.click  和  CSS选择器稳定性不好 我也不知道为啥 :(