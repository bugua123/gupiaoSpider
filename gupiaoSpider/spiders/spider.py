#-*-coding:utf-8-*-
import  scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
import re
from lxml import etree
import threading
from gupiaoSpider.items     import GupiaospiderItem
import random
class Myspider(scrapy.Spider):
    name = 'gupiao'
    allowed_domains=['sinajs.cn']
    start_urls=[
        'http://hq.sinajs.cn/list=sh600587',
    ]
    dom = 'hq.sinajs.cn'
    bashurl='.html'

    def __init__(self, *args, **kwargs):
        self.ua_list = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        ]
        self.ua = random.choice(self.ua_list)
        super(Myspider, self).__init__(*args, **kwargs)
        self.xsrf = ''
    def start_requests(self):
        headers = {
            "Host":"hq.sinajs.cn",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding":"gzip, deflate",
            "Referer":"http://onlinelibrary.wiley.com/journal/10.1002/(ISSN)1521-3773",
            "Cookie":"EuCookie='this site uses cookies'; __utma=235730399.1295424692.1421928359.1447763419.1447815829.20; s_fid=2945BB418F8B3FEE-1902CCBEDBBA7EA2; __atuvc=0%7C37%2C0%7C38%2C0%7C39%2C0%7C40%2C3%7C41; __gads=ID=44b4ae1ff8e30f86:T=1423626648:S=ALNI_MalhqbGv303qnu14HBk1HfhJIDrfQ; __utmz=235730399.1447763419.19.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; TrackJS=c428ef97-432b-443e-bdfe-0880dcf38417; OLProdServerID=1026; JSESSIONID=441E57608CA4A81DFA82F4C7432B400F.f03t02; WOLSIGNATURE=7f89d4e4-d588-49a2-9f19-26490ac3cdd3; REPORTINGWOLSIGNATURE=7306160150857908530; __utmc=235730399; s_vnum=1450355421193%26vn%3D2; s_cc=true; __utmb=235730399.3.10.1447815829; __utmt=1; s_invisit=true; s_visit=1; s_prevChannel=JOURNALS; s_prevProp1=TITLE_HOME; s_prevProp2=TITLE_HOME",
            "Connection":"keep-alive"
        }
        headers = {'User - Agent': self.ua}
        for url in self.start_urls:
            # request.headers.setdefault('Use-Agent',self.ua)
            yield Request(url,headers=headers,callback=self.parse)


    def parse(self, response):
        #print response.url  # 打印当前爬取的链接
        #print response.body # 打印当前爬取网页的源代码
        item =GupiaospiderItem()

        # 保存数据到数据库
        str =  response.body;
        #替换双引号
        str=str.replace(chr(34), "")
        str=str.split('=')[1].split(',')

        item['gpcode']=str[0]
        item['kaipanjia']=str[1]
        item['zuorishoupanjia']=str[2]
        item['dangqianjia']=str[3]
        item['jinrizuigaojia']=str[4]
        item['jinrizuidijia']=str[5]
        item['jingbuy1']=str[6]
        item['jingsale1']=str[7]
        item['chengjiaogupiaoshu']=str[8]
        item['chengjiaojine']=str[9]
        item['buygushu1']=str[10]
        item['buybaojia1']=str[11]
        item['buygushu2']=str[12]
        item['buybaojia2']=str[13]
        item['buygushu3']=str[14]
        item['buybaojia3']=str[15]
        item['buygushu4']=str[16]
        item['buybaojia4']=str[17]
        item['buygushu5']=str[18]
        item['buybaojia5']=str[19]
        item['salegushu1']=str[20]
        item['salebaojia1']=str[21]
        item['salegushu2']=str[22]
        item['salebaojia2']=str[23]
        item['salegushu3']=str[24]
        item['salebaojia3']=str[25]
        item['salegushu4']=str[26]
        item['salebaojia4']=str[27]
        item['salegushu5']=str[28]
        item['salebaojia5']=str[29]
        item['riqi']=str[30]
        item['shijian']=str[31]

        yield item
        #print str.split('=')[1].split(',');
        #print a[0]
        # max_num=BeautifulSoup(response.text,'lxml').find('div',class_='pagelink').fild_all('a')[-1].get_text()
        # bashurl=str(response.url)[-7]
        # for num in range(1,int(max_num)+1):
        #     url=bashurl+'_'+str(num)+self.bashurl
            #yield Request(url,callback=self.get_name)

    # def get_name(self,response):
    #     tds=BeautifulSoup(response.text,'lxml').find_all('tr',bgcolor='#FFFFFF')
    #     for td in tds:
    #         novelname=td.find('a').get_text()
    #         novelurl=td.find('a')['href']
    #         print 'name'+novelurl
    #         yield Request(novelurl,callback=self.get_chapterurl,meta={'name':novelname,'url':novelurl})
    # def get_chapterurl(self,response):
    #     item=DingdianItem()
    #     item['name']=str(response.meta['name']).replace('\xa0','')
    #     item['novelurl']=response.meta['url']
    #     category=BeautifulSoup(response.text,'lxml').find('table').find('a').get_text()
    #     author=BeautifulSoup(response.text,'lxml').find('table').find_all('td')[1].get_text()
    #     bash_url=BeautifulSoup(response.text,'lxml').find('p',class_='btnlinks').find('a',class_='read')['hred']
    #     name_id=str(bash_url)[-6:-1].replace('/','')
    #     item['category']=str(category).replace('/','')
    #     item['name_id']=name_id
    #     return item

