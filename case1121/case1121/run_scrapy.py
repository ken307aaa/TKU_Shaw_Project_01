import os

t=input('請輸入欲搜尋關鍵字之新聞：')
os.system("scrapy crawl googlenews -a words=" + str(t))#單執行