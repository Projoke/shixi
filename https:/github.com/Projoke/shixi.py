#!/usr/bin/env python
#coding=utf-8
import time
import requests
from lxml import etree
import json
 
# 查数据总数量
def listnum(iname=''):
    url='https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA%E5%90%8D%E5%8D%95&cardNum=&iname=%E7%89%9B&areaName='
    headers={
        'Referer': 'Referer: https://www.baidu.com/s?wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA&rsv_spt=1&rsv_iqid=0xd609bc53000007a2&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=%25E4%25BA%25BA%25E4%25BA%25BA%25E7%25BD%2591&inputT=4103&rsv_t=284b4GKK9AtCD7tiOTYP1zvlPucgiWINKuuwdhMhPwufPfGhspZJaAnNGqS4bjC9fL2e&rsv_sug3=29&rsv_sug1=27&rsv_sug7=100&rsv_pq=dadd35d50000105a&rsv_sug2=0&rsv_sug4=4817',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    params={
        'pn': '0',
        # 't': '1539162179792',
        # '_': '1539162104029',
        'resource_id':'6899',
        'query':'失信被执行人名单',
        'iname': iname,
        'rn':'10',
        'ie':'utf-8',
        'oe':'utf-8',
        'format':'json',
        'cb':'jQuery11020530582244968731_1539162104026'
    }
    req=requests.get(url=url,headers=headers,params=params).text
    data1=req.split('(')
    data2=''
    data=''
    for i in data1[1:]:
        data2+=i
 
    data3=data2.split(')')
    for i in data3[:-1]:
        data+=i
    data=json.loads(data)
    # 包含失信人信息的字典
    results=data['data'][0].get('result')
    for person in results:
        print person['iname'] + "\t" + person['disruptTypeName'] + "\t" + person['duty']
    # 总共多少条数据
    listNum=data['data'][0].get('listNum')
    print('共'+str(listNum)+'条数据')
    return int(listNum)
 
def shixin(iname='',pn=0):
    url='https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA%E5%90%8D%E5%8D%95&cardNum=&iname=%E7%89%9B&areaName='
    headers={
        'Referer': 'Referer: https://www.baidu.com/s?wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA&rsv_spt=1&rsv_iqid=0xd609bc53000007a2&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=%25E4%25BA%25BA%25E4%25BA%25BA%25E7%25BD%2591&inputT=4103&rsv_t=284b4GKK9AtCD7tiOTYP1zvlPucgiWINKuuwdhMhPwufPfGhspZJaAnNGqS4bjC9fL2e&rsv_sug3=29&rsv_sug1=27&rsv_sug7=100&rsv_pq=dadd35d50000105a&rsv_sug2=0&rsv_sug4=4817',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    params={
        'pn': str(pn*50),
        # 't': '1539162179792',
        # '_': '1539162104029',
        'resource_id':'6899',
        'query':'失信被执行人名单',
        'iname': iname,
        'rn':'10',
        'ie':'utf-8',
        'oe':'utf-8',
        'format':'json',
        'cb':'jQuery11020530582244968731_1539162104026'
    }
    req=requests.get(url=url,headers=headers,params=params).text
    data1=req.split('(')
    data2=''
    data=''
    for i in data1[1:]:
        data2+=i
 
    data3=data2.split(')')
    for i in data3[:-1]:
        data+=i
    data=json.loads(data)
    if data['data']:
        # 包含失信人信息的字典
        results=data['data'][0].get('result')
        # 总共多少条数据
        listNum=data['data'][0].get('listNum')
        print('共'+str(listNum)+'条数据')
        for i in results:
            print(i.get('iname'),i.get('cardNum'))
    else:
        return None
 
iname=raw_input("名称: ")
listnum(iname)

'''for i in inames:
    num = listnum()
    pn=int(num/50)+1
    for j in range(pn):
        shixin(i, j)
'''
