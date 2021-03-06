# _*_coding:utf-8*_
import urllib.request
from time import sleep
# 安装selenium
# pip3 install selenium
# 安装浏览器驱动（chrome win版不支持 headless，此处选用firefox）
# chromedriver 下载地址：https://code.google.com/p/chromedriver/downloads/list
# geckodriver  下载地址：https://github.com/mozilla/geckodriver/releases
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# def getPage(url):
#     request = urllib.request.Request(url)
#     response = urllib.request.urlopen(request)
#     print(type(response))
#     print(response.geturl())
#     print(response.info())
#     print(response.getcode())
#     #print(response.read().decode('utf-8'))
#     return response.read()
#
# url='http://www.sse.com.cn/js/common/ssesuggestdata.js'
# result=getPage(url).decode('utf-8')
# #print(result)
# txt='E:\github\pythonstudy'
# f = open(txt, "w+", encoding='utf-8')
# f.write(result)
# print(result)
# f.close()

def getSHStockList(url):
    stocklist = []
    firefox_options = webdriver.FirefoxOptions()
    #firefox_options.add_argument('--headless')
    #firefox_options.set_headless()
    firefox_options.add_argument('--disable-gpu')
    browser = webdriver.Firefox(executable_path='geckodriver', firefox_options=firefox_options)
    browser.set_page_load_timeout(60)
    browser.get(url)  # 取得浏览器中的element的内容了
    browser.implicitly_wait(30)
    #total_page_no = browser.find('pagebutton').text #获取股票总页数
    max_page_no = browser.find_element_by_css_selector('.pagination > li:nth-child(7) > a:nth-child(1)').text # 获取股票页数列表
    print(max_page_no)
    for page_no in range(1,int(max_page_no) + 1):
        if page_no != 1: #第一页不用输入
            td_id_before = browser.find_element_by_tag_name('td')
            #print(td_id_before.text)
            browser.find_element_by_id('ht_codeinput').clear()  # 清空页码
            browser.find_element_by_id('ht_codeinput').send_keys(page_no)  # 输入页码
            browser.find_element_by_id('pagebutton').click()  # 点击
            td_id_after = browser.find_element_by_tag_name('td')
            while(td_id_after == td_id_before):
                # 判断td加载后的id是否与加载前相等，如果相等，说明加载没有完成，继续等待判断
                # sleep(1)  # 给1s时间完成加载
                td_id_after = WebDriverWait(browser, 60, 0.5).until(
                lambda x: x.find_element_by_tag_name('td'))
            #print(td_id_after.text)

        print(page_no)
        result = browser.find_elements_by_tag_name('td') #获取element中td元素id
        stockinfo = []
        cnt = 0
        for i in result:
            cnt = cnt + 1
            #print(i.text)
            stockinfo.append(i.text)  # 得到内容
            if cnt%8 == 0:   #每8个换一列表
                stocklist.append(stockinfo)
                stockinfo = [] #不能用stockinfo.clear()，否则全置空了
        #print(stocklist)
    return stocklist

def main():
    sh_stock_list_url = 'http://www.sse.com.cn/assortment/stock/list/share/'
    shstocklist = getSHStockList(sh_stock_list_url)
    print(shstocklist)

main()