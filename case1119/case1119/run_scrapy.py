import os

words=['台積電']

for i in words:
    os.system("scrapy crawl googlenews -a words=" + str(i))
