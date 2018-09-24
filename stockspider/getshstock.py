#!/usr/bin/env python 
# _*_ coding:UTF-8 _*_
"""
__title__ = ''
__author__ = 'Goode'
__mtime__ = '2018/9/20'
"""
import requests
import time
import json

def getSHStockList():

    url = 'http://query.sse.com.cn/security/stock/getStockListData2.do'

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        #'Cookie': 'yfx_c_g_u_id_10000042=_ck18092022132519706772019885773; yfx_f_l_v_t_10000042=f_t_1537452805970__r_t_1537452805970__v_t_1537452805970__r_c_0; yfx_mr_10000042=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_mr_f_10000042=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_key_10000042=; VISITED_MENU=%5B%228464%22%5D',
        'Host': 'query.sse.com.cn',
        'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    for pageNo in range(1, 200):
        params = {
            'sonCallBack': 'jsonpCallback40821',
            'isPagination': 'true',
            'stockCode': '',
            'csrcCode': '',
            'areaName': '',
            'stockType': '1',
            'pageHelp.cacheSize': '1',
            'pageHelp.beginPage': pageNo,
            'pageHelp.pageSize': '25',
            'pageHelp.pageNo': pageNo,
            '_': int(time.time()*1000)
        }


        try:
            req = requests.get(url, params=params, headers=headers)
            # req = requests.get(url, params=params)
            if req.status_code != 200:
                print(req.text)
                return
            stockList = req.json().get('pageHelp').get('data')
            if stockList == []:
                return
            for item in stockList:
                print(item.get('SECURITY_ABBR_A'))
            # print(type(stockList))
        except Exception as e:
            print(e)
            return


if __name__ == '__main__':
    getSHStockList()

