from BOSSBase import *
from BOSSMongo import *

def get_products():   #爬取所需信息
    global workItem
    global doc
    global html
    global couldNext
    def find_intrintroduction_text(Pseudo_classes, introduction):  # get_products()——轮流匹配介绍内容
        if introduction.find(Pseudo_classes + ' .text').siblings('h3').text() == '职位描述' or introduction.find(
                Pseudo_classes + ' .text').siblings('h3').text() == '岗位描述':
            Work_introduction = introduction.find(Pseudo_classes + ' .text').text()
            workItem.update({'work_introduction': Work_introduction})
        if introduction.find(Pseudo_classes + ' .text').siblings('h3').text() == '公司介绍':
            Company_introduction = introduction.find(Pseudo_classes + ' .text').text()
            workItem.update({'company__introduction': Company_introduction})
        Team_introduction = ''
        if introduction.find(Pseudo_classes + ' .text').siblings('h3').text() == '团队介绍':
            Team_introduction = introduction.find(Pseudo_classes + ' .text').text()
            workItem.update({'team__introduction': Team_introduction})
        if introduction.find(Pseudo_classes + ' .job-tags').siblings('h3').text() == '团队介绍':
            Team_introduction = Team_introduction + introduction.find(
                Pseudo_classes + ' .job-tags').text()  # 文字和标签可能都会有
            workItem.update({'team__introduction': Team_introduction})
        # if introduction.find(Pseudo_classes+' .text').siblings('h3').text()== '工作地址' :
    if couldNext==5:#失败5次放弃解析这页
        return
    try:
        url=browser.current_url
        html = browser.page_source#获取源代码
        doc = pq(html)#调用PyQuery库
    except:
        get_products()

    try:
        basic_info = doc('#main > div.job-banner > div > div')  # 基本工作信息
        # #顶部
        #basic_info可包含“ 工作名 工资 福利”  (实际也包含“基本要求” 但是后期使用不统一不方便)
        # 通过寻找basic_info    验证详情页是否打开成功
    except:
        print('本次详情页打不开了')
        print(datetime.datetime.now())
        couldNext = couldNext + 1
        get_products()#再来一次
    couldNext = 0  # 打得开重新置0
    try:
       compny_info = doc('#main > div.job-box > div > div.job-sider > div.sider-company')#基本公司信息
       # #右侧
       #compny_info可包含“公司名 资金 员工规模 行业 网站”
    except:
        compny_info=" "
    try:
       Work_name = basic_info.find('.name h1').text()  # 工作名
       workItem.update({'work_name': Work_name})
    except:
       pass
    try:
        Salary = basic_info.find('.salary').text()  # 工资
        workItem.update({'salary': Salary})
    except:
        pass
    try:
       requirements=str(doc('#main > div.job-banner > div > div > div.info-primary > p'))#基本要求
       #requirements 一定包含“城市 经验 文凭”
       Requirements = re.findall(r'>(.*?)<', requirements, re.S)  # 正则表达式 形成集合
       workItem.update({'city': Requirements[0]})  # 城市
       workItem.update({'experience': Requirements[1]})  # 经验
       workItem.update({'diploma': Requirements[2]})  # 文凭
    except:
       pass
    try:
       Company_name = compny_info.find('.company-info').text()  # 公司名
       workItem.update({'company_name': Company_name})
    except:
       pass
    try:
       Finances = compny_info.find('.icon-stage').parent().text()  # 资金
       workItem.update({'Finances': Finances})
    except:
       pass
    try:
       Scale = compny_info.find('.icon-scale').parent().text()  # 员工规模
       workItem.update({'scale': Scale})
    except:
       pass
    try:
       Industry = compny_info.find('.icon-industry').parent().text()  # 行业
       workItem.update({'industry': Industry})
    except:
       pass
    try:
       Web = compny_info.find('.icon-net').parent().text()  # 网站
       workItem.update({'web': Web})
    except:
       pass
    try:
       Welfare = basic_info.find('.job-tags').text()  # 福利
       workItem.update({'welfare': Welfare})
    except:
       pass

    ####段落梳理####
    try:
        Introduction = doc('#main > div.job-box > div > div.job-detail > div.detail-content')  # 介绍的所有段落
        # #中间
    except:
        Introduction=""
    try:
        WorkAddress = Introduction.find(' .location-address').text()
        workItem.update({'workAddress': WorkAddress})
    except:
        pass
    child1 = 'div:first-child '
    child2 = 'div:nth-child(2) '
    child3 = 'div:nth-child(3) '
    try:
       find_intrintroduction_text(child1,Introduction)
    except:
       pass
    try:
       find_intrintroduction_text(child2,Introduction)
    except:
       pass
    try:
       find_intrintroduction_text(child3,Introduction)
    except:
       pass
    try:
        URL = browser.current_url#网址，可数据库去重
        workItem.update({'workurl': URL})
    except:
       pass

def main():
    get_products()

if __name__=='__main__':
    main()