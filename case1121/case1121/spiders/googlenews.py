import scrapy
import requests
from urllib.parse import urlparse
import news_crawler#如果找不到，至檔案夾將Mark Directory as改成root
from items import ScrapyCaseItem


class GoogleNewsSpider(scrapy.Spider):
    name = "googlenews"
    USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

    def __init__(self,words=None,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.words=words
        self.start_urls=[f'https://news.google.com/search?q={self.words}&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers={"User-Agent": self.USER_AGENT})#header

    def parse(self, response):
        news_xpath = response.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div')
        count_true=0
        count_false=0
        for i in range(len(news_xpath)-1):
            try:
                title=news_xpath[i].xpath('div/article/h3/a/text()').extract_first()# 標題
                web=news_xpath[i].xpath('div/article/div[2]/div/a/text()').extract_first()# 來源
                url='https://news.google.com' + news_xpath[i].xpath('div/article/h3/a/@href').extract_first()# url
                origin_url = self.getOriginUrl(url)  # 原文網址
                key_domain = urlparse(origin_url).netloc  # 網域
                yield scrapy.Request(origin_url,meta={'resource':key_domain,'origin_url':origin_url},headers={"User-Agent": self.USER_AGENT},callback=self.switch)#傳送至對應框架
                count_true+=1
            except:
                print('錯誤:',news_xpath[i])
                count_false+=1
        print('總成功筆數：', count_true)
        print('總失敗筆數：', count_false)

    def getOriginUrl(self,googleUrl):#取得原文網址
        return requests.get(googleUrl).url

    def switch(self,response):#判斷該新聞適用爬蟲框架
        source=response.meta['resource']
        origin_url=response.meta['origin_url']
        title,content,time,web=news_crawler.getCrawler(source, response)
        if title==None or content==None or time==None or web==None:#如果回傳是空的就不儲存
            print('此網頁無爬蟲框架:'+origin_url)
            with open('無爬蟲框架集.csv', 'a', encoding='utf_8_sig') as f:
                f.write(origin_url)
                f.write('\n')
        else:
            print('存取成功:'+origin_url)
            item = ScrapyCaseItem()
            item['title'] = title
            item['content'] = content
            item['time'] = time
            item['web']=web
            yield item