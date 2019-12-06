from BOSSBase import *
from selenium.webdriver.common.action_chains import ActionChains
from BOSSList import *

global couldNextpage
def getpagenow():#获取当前页面数
    try:
        pageNow = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR,'#main > div > div.job-list > div.page >  .cur')))#找到页码行(.page)中的当前页(.cur)
        return int(pageNow.text)#返回为int类型
    except:
        return 1#找不到默认只有1页
def nextPage():
    global couldNextpage
    couldNextpage=True
    js="var q=document.documentElement.scrollTop=10000"
    browser.execute_script(js)#滑到底部
    time.sleep(1)
    try:
        pagelist= wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR,'#main > div > div.job-list > div.page' )))#找到页码行(.page)
        ActionChains(browser).move_to_element(pagelist).perform()#按下按钮
    except:
        print("只有一页，完毕")#只有一页就没有列表
        couldNextpage = False
    url = browser.current_url
    print(url)#输出当前网址，url等会还要用到
    if couldNextpage==True:#可翻页标记
        pagenext=str(getpagenow()+1)#下一页参照
        try:
            NextPageNumButton=browser.find_element_by_link_text(pagenext)
            ActionChains(browser).move_to_element(NextPageNumButton).click(NextPageNumButton).perform()#按下翻页按钮
            print('翻页成功',getpagenow())
        except:
            if url==browser.current_url:#没有跳转新的网页，和原来的url一样
                couldNextpage = False
                print('本次所有翻页完毕。现在页码是',getpagenow())
def  traversalANDnextPage():
    global couldNextpage
    couldNextpage=True
    while couldNextpage==True:
        print('开始遍历')
        traversalList()
        print('开始翻页')
        nextPage()
        print('可翻页：',couldNextpage)
def main():
    traversalANDnextPage()
if __name__=='__main__':
    main()
