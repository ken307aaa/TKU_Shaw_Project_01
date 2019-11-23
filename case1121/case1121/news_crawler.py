'''將所有新聞爬蟲框架寫在底下，
並用dict以domain作為key來取對應方法使用'''
from bs4 import BeautifulSoup
import re

def EconomicDaily(response):
    web='經濟日報'
    title_xpath = response.xpath('//*[@id="story_art_title"]/text()')
    title = title_xpath.extract_first()
    print(title)
    # 內文
    content_xpath = response.xpath('//*[@id="article_body"]/p/text()')
    content = ''
    for i in content_xpath:
        if i.extract().find('延伸閱讀》') != -1:
            pass
        else:
            content += str(i.extract()).replace('\n', '').replace('\r', '')
    print(content)
    # 時間
    time_xpath = response.xpath('//*[@id="shareBar"]/div[2]/div/span/text()')
    time = str(time_xpath.extract_first()).split(' ')[0]

    print(time)
    return title,content,time,web

def DigiTimes(response):
    web = 'DIGITIMES'
    title = ''
    content = ''
    time = ''
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('p', 'txt-blue2 txt-bold m-b-10').text.strip()
    print(title)
    content_list = objSoup.find_all('p', 'main_p')
    for i in range(len(content_list) - 1):
        content += content_list[i].text.strip()
    print(content)
    time = objSoup.find('ul', 'list-inline m-b-5 txt-16').find('time').text.strip()
    print(time)
    print(web)
    return title, content, time, web

def VideoUdn(response):
    web = '聯合影音'
    title = ''
    content = ''
    time = ''
    objSoup = BeautifulSoup(response.body, 'lxml')
    objTag = objSoup.find('div', 'article')
    title = objTag.find('h1', 'title').text.strip()
    print(title)
    content_list = objTag.find('div', 'description').find_all('p')
    for i in content_list:
        content += i.text.strip()
    print(content)
    time_list = objTag.find('div', 'datetime')
    y = time_list.find('span', 'year').text.strip()
    m = time_list.find('span', 'month').text.strip()
    d = time_list.find('span', 'day').text.strip()
    time = y + '-' + m + '-' + d
    print(time)
    return title, content, time, web

def Ustv(response):
    web = '非凡電視台'
    # 標題
    title_xpath = response.xpath('//*[@id="news_detail"]/div/h1/text()')
    title = str(title_xpath.extract_first()).strip()
    print(title)
    # 內文
    content_xpath = response.xpath('//*[@id="primarytext"]/text()')
    content = ''
    for i in content_xpath:
        content += str(i.extract()).strip()
    print(content)
    # 時間
    time_xpath = response.xpath('//*[@id="news_detail"]/div/h1/div/text()')
    time = str(time_xpath.extract_first()).strip().split(' ')
    print(time[0].replace('/', '-'))
    return title, content, time, web

def GlobalNewsTv(response):
    web = '寰宇新聞網'
    # 標題
    title_xpath = response.xpath('/html/body/div[2]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/h1/text()')
    title = ''
    for i in title_xpath:
        title += str(i.extract()).strip()
    print(title)
    contect_xpath = response.xpath(
        '/html/body/div[2]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/div[5]/div[2]/p/text()')
    content = ''
    for i in contect_xpath:
        content += str(i.extract()).strip()
    print(content)
    time = str(response.xpath('/html/head/meta[12]').extract()).split('content="')[1].split('T')[0]
    print(time)
    return title, content, time, web

def BusinessToday(response):
    web = '今周刊'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'article__maintitle').text.strip()
    print(title)
    content = objSoup.find('div', 'cke_editable font__select-content').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('p', 'context__info-item context__info-item--date').text.strip().split(' ')[0]
    print(time)
    return title, content, time, web

def CTS(response):
    web = '華視新聞'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'artical-title').text.strip()
    print(title)
    content = ''
    content_list = objSoup.find('div', 'artical-content').find_all('p')
    for i in content_list:
        content += i.text.strip()
    print(content)
    time = objSoup.find('p', 'artical-time').text.strip().split(' ')[0].replace('/', '-')
    print(time)
    return title, content, time, web

def XFastest(response):
    web = 'XFastest'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'entry-title').text.strip()
    print(title)
    content_list = objSoup.find('div', 'vw-post-content clearfix').find_all('p')
    content = ''
    for i in content_list:
        content += i.text.strip()
    print(content)
    time = objSoup.find('time').text.strip()
    print(time)
    return title, content, time, web

def EPrice(response):
    web = 'ePrice'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'topic').text.strip()
    print(title)
    content = objSoup.find('div', 'col-lg-12 col-xs-12 content parallax-ads-layer').text.strip().replace('\n', '')
    print(content)
    time = str(objSoup.find('div', 'small started_at').text.strip().split('：')[1]).split(' ')[0]
    print(time)
    return title, content, time, web

def Engadget(response):
    web = 'Engadget'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 't-h4@m- t-h1-b@tp t-h1@tl+ mt-20 mt-15@tp mt-0@m-').text.strip()
    print(title)
    content = objSoup.find('div', 'article-text c-gray-1').text.strip().replace('\n', '')
    print(content)
    time = str(objSoup.find('div', 'th-meta').text.strip()).replace(' ', '').replace('年', '-').replace('月','-').replace('日','')
    print(time)
    return title, content, time, web

def Kocpc(response):
    web = '電腦王阿達'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', id='tc2sc-title').text.strip()
    print(title)
    content_list = objSoup.find_all('div', 'dable-content-wrapper')
    content = ''
    for i in content_list:
        content += i.text.strip().replace('\n', '')
    print(content)
    time = objSoup.find_all('div', 'info-item')[1].text.strip().replace('/', '-')
    print(time)
    return title, content, time, web

def Cardu(response):
    web = '卡優新聞網'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('div', 'pt-3 mx-3 detail_title').find('h2').text.strip()
    print(title)
    content_list = objSoup.find('div', 'pb-3 mx-3 detail_content').find_all('p')
    content = ''
    for i in content_list:
        content += i.text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('div', 'col-md-8 col-12').find('p').text.strip().split('\n')[1].strip().split(' ')[1]
    print(time)
    return title, content, time, web

def bbc(self, response):
    web = 'BBC 中文网'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('div', class_='date date--v2').text
    time = re.sub(r'(\d+)年 (\d+)月 (\d+)日', r'\1-\2-\3', time_info)
    print(time)
    # content
    content_body = soup.find('div', class_='story-body')
    content = ''
    for c in content_body.find_all('p'):
        content += c.text
    print(content)
    return title, content, time, web

def business(response):
    web = '商周財富網'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time = soup.find('div', class_='article-date').text.replace('.', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='article-txt')
    content = ''
    for c in content_body.find_all('p'):
        content += c.text
    print(content)

    return title, content, time, web

def businessw(response):
    web = '商業周刊'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('div', class_='Padding-left Margin-top')
    time = (time_info.find_all('span')[1].text).replace('.', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='Single-article WebContent')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text.replace('\n', '')
    print(content)

    return title, content, time, web

def buzzorange(response):
    web = 'TechOrange 科技報橘'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1', class_='entry-title').text
    print(title)
    # time
    time = soup.find('time', class_='entry-date published').text.replace('/', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='entry-content')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def chinatimes(response):
    web = '中時電子報'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('span', 'date')
    time = (time_info.text).replace('/', '-')
    print(time)
    # content
    content = ''
    if soup.find('div', 'article-body') is not None:
        content_body = soup.find('div', 'article-body')
        content_list = content_body.find_all('p')
        for c in content_list:
            content += c.text
    if soup.find('p', 'collection-intro') is not None:
        content += soup.find('p', 'collection-intro').text
    print(content)
    return title, content, time, web

def cna(response):
    web = '中央社即時新聞'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('div', class_='updatetime')
    time = (time_info.find('span').text).split(' ')[0].replace('/', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='paragraph')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        if c.find('figure'):
            de = c.find('figure')
            c = c.text
            c = c.replace(de.text, '')
            content += c
            continue
        content += c.text
    print(content)

    return title, content, time, web

def cnyes(response):
    web = '鉅亨網'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('time')
    time = (time_info.text).split(' ')[0].replace('/', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='_1UuP')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        if c.find('figure'):
            continue
        content += c.text
    print(content)

    return title, content, time, web

def csr(response):
    web = 'CSR@天下'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('div', class_='articleInfoBox')
    time = (time_info.find('li', class_='time').text).split(' ')[0]
    print(time)
    # content
    soup.find('p', class_='introduction').extract()
    content_body = soup.find('section', class_='content')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def ctwant(response):
    web = 'CTWANT'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text.strip()
    print(title)
    # time
    time_info = soup.find('p', class_='p-article__info').text
    time = re.sub(r'(\d+)月(\d+)日, (\d+)', r'\3-\1-\2', time_info).strip()
    print(time)
    # content
    content_body = soup.find('div', class_='p-article__content')
    content_body.find('div', class_='e-popover__qr-wrapper').extract()
    content_body.find('div', class_='p-article__img-box').extract()
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text.strip()
    print(content)

    return title, content, time, web

def cw(response):
    web = '天下雜誌'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('address', class_='authorInfor')
    time = (time_info.find('time').text)
    print(time)
    # content
    content_body = soup.find('section', class_='nevin')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text.strip()
    print(content)

    return title, content, time, web

def einfo(response):
    web = '環境資訊電子報'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1', class_='title').text
    print(title)
    # time
    time_info = soup.find('div', class_='article-create-date').text
    time = re.sub(r'(\d+)年(\d+)月(\d+)日', r'\1-\2-\3', time_info)
    print(time)
    # content
    content_body = soup.find_all('div', class_='field-item even')[2]
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def ebc(response):
    web = '東森新聞'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time = soup.find('span', class_='small-gray-text').text.split(' ')[0].replace('/', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='raw-style')
    content_body.find('a').extract()
    content_body.find('strong').extract()
    # content_body.find('div',id='myModal3').extract()
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text.strip()
    print(content)

    return title, content, time, web

def ecltn(response):
    web = '自由時報電子報'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text.strip()
    print(title)
    # time
    time_info = soup.find('span', class_='time')
    time = (time_info.text).split(' ')[0]
    print(time)
    # content
    soup.find('p', class_='appE1121').extract()
    soup.find('div', class_='ltnapp boxTitle').extract()
    content_list = soup.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def epochtimes(response):
    web = '大紀元'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('div', class_='mbottom10 large-12 medium-12 small-12 columns')
    time = (time_info.find('time').text).split(' ')[1]
    print(time)
    # content
    content_body = soup.find('div', id='artbody')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def ettoday(response):
    web = 'ETtoday'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1', class_='title').text
    print(title)
    # time
    time_info = soup.find('time', class_='date').text.strip().split(' ')[0]
    time = re.sub(r'(\d+)年(\d+)月(\d+)日', r'\1-\2-\3', time_info)
    print(time)
    # content
    for s in soup.find_all('strong'):
        s.extract()
    content_body = soup.find('div', class_='story')

    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def eventsinfocus(response):
    web = '焦點事件'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1', class_='page-title').text
    print(title)
    # time
    # time_info = soup.find('',class_ = 'story_bady_info_author')
    time = (soup.find('span', class_='date-display-single').text).replace('/', '-')
    print(time)
    # content
    content_body = soup.find_all('div', class_='field-items')[2]
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def fitech(response):
    web = '科技新報 TechNews'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1', class_='entry-title').text
    print(title)
    # title = title.find('a').text
    # time
    time_info = soup.find_all('span', class_='body')[1].text
    time = re.sub(r'(\d+) 年 (\d+) 月 (\d+) 日.*', r'\1-\2-\3', time_info)
    print(time)
    # content
    content_body = soup.find('div', class_='indent')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def fncebc(response):
    web = '東森財經新聞'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time = soup.find('span', class_='small-gray-text').text.split(' ')[0].replace('/', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='origin-style web-content')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text.strip()
    print(content)

    return title, content, time, web

def gvm(response):
    web = '遠見雜誌'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('div', class_='pc-bigArticle')
    t = time_info.text.split('\xa0')
    time = t[len(t) - 1]
    print(time)
    # content
    content_body = soup.find('section', class_='article-content')
    content_body.find('p', class_='keyWord').extract()
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def hinet(response):
    web = 'HiNet 新聞社群'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h2').text
    print(title)
    # time
    time_info = soup.find('span', class_='cp').text.split(' ')[0]
    time = time_info.split('\xa0')[1].replace('/', '-')
    print(time)
    # content
    soup.find('cite').extract()
    content = soup.find('div', class_='newsContent').text
    print(content)

    return title, content, time, web

def hkon(response):
    web = 'on.cc東網台灣'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('span', class_='datetime').text
    # print(time_d)
    time = re.sub(r'(\d+)年(\d+)月(\d+)日.*', r'\1-\2-\3', time_info)
    print(time)
    # content
    content_body = soup.find('div', class_='breakingNewsContent')
    content_list = content_body.find_all('div', class_='paragraph')
    content = ''
    for c in content_list:
        if c.text.find('-') != -1:
            break
        content += c.text.strip().replace('\n', '-')
    print(content)

    return title, content, time, web

def inside(response):
    web = 'INSIDE 硬塞的網路趨勢觀察'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time = soup.find('li', class_='post_date').text.replace('/', '-').replace('\n', '')
    print(time)
    # content
    for s in soup.find_all('strong'):
        s.extract()
    content_body = soup.find('div', id='article_content')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def manager(response):
    web = '經理人月刊'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text.strip()
    print(title)
    # time
    time = soup.find('time', itemprop='datePublished').text.strip()
    print(time)
    # content
    content = soup.find('div', itemprop='articleBody').text.strip()
    print(content)

    return title, content, time, web

def market(response):
    web = '自由電子報市場動態'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text.strip()
    print(title)
    # time
    time = soup.find('span', class_='date1').text.split(' ')[0]
    print(time)
    # content
    content_body = soup.find('div', class_='text')
    content_body.find('p', class_='appE1121').extract()
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def mirror(response):
    web = '鏡週刊'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('div', class_='date')
    time = (time_info.text).split(' ')[0].replace('.', '-')
    print(time)
    # content
    soup.find('div', class_='info middle__info').extract()
    soup.find('div', class_='newsletterCategories').extract()
    soup.find('div', class_='article_main_tags').extract()
    content_body = soup.find('div', class_='article_body')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def mobiyahoo(response):
    web = 'Yahoo奇摩'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('header', class_='caas-title-wrapper').text
    print(title)
    # time
    time_info = soup.find('time', class_='caas-attr-meta-time caas-relative-time caas-attr-item')
    time = re.sub(r'.*datetime="(\d+)-(\d+)-(\d+).*', r'\1-\2-\3', str(time_info))
    print(time)
    # content
    content_body = soup.find('div', class_='caas-body')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        if c.find('figure') or c.find('strong'):
            continue
        content += c.text
    print(content)

    return title, content, time, web

def moneydj(response):
    web = 'MoneyDJ理財網'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text.strip()
    print(title)
    # time
    time = soup.find('span', id='MainContent_Contents_lbDate').text.split(' ')[0].replace('/', '-')
    print(time)
    # content
    content = soup.find('div', id='highlight').text.strip()
    print(content)

    return title, content, time, web

def MoneyUdn(response):
    web = '經濟日報'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find(id='story_art_title').text
    print(title)
    # time
    time_info = soup.find('div', class_='shareBar__info--author')
    time = (time_info.find('span').text).split(' ')[0]
    print(time)
    # content
    content_body = soup.find('div', id='article_body')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        if c.find('figure'):
            de = c.find('figure')
            c = c.text
            c = c.replace(de.text, '')
            content += c
            continue
        content += c.text
    print(content)

    return title, content, time, web

def mygonews(response):
    web = '買購不動產新聞台'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time = soup.find('div', class_='detaildate').text.split('：')[2]
    print(time)
    # content
    content = soup.find('div', class_='editbox').text.replace('\n', '').strip()
    print(content)

    return title, content, time, web

def newtalk(response):
    web = '新頭殼'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1', class_='content_title').text
    print(title)
    # time
    time_info = soup.find('div', class_='content_date').text
    time = time_info.strip().split(' ')[1].replace('.', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='fontsize news-content')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def nownews(response):
    web = 'NOWnews'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time = soup.find('time', class_='entry-date updated td-module-date').text.split(' ')[0]
    print(time)
    # content
    content_body = soup.find('span', itemprop='articleBody')
    content = ''
    for c in content_body.find_all('p'):
        content += c.text
    print(content)

    return title, content, time, web

def ntdtv(response):
    web = '新唐人亞太電視台'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1', class_='article_title').text
    print(title)
    # time
    time = soup.find('div', class_='article_info').text.split('：')[1].split(' ')[0]
    print(time)
    # content
    content_body = soup.find('div', id='article_content')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def ntdtvs(response):
    web = 'NTDTV'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('div', class_='time')
    time = (time_info.find('span').text).split(' ')[0]
    print(time)
    # content
    content_body = soup.find('div', class_='post_content')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def people(response):
    web = '民報'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time = soup.find('span', class_='date').text.split(' ')[0]
    print(time)
    # content
    content_body = soup.find('div', id='newscontent')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def peopo(response):
    web = '公民新聞'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1', class_='page-title').text
    print(title)
    # time
    time_info = soup.find('div', class_='submitted')
    time = (time_info.find('span').text).split(' ')[0].replace('.', '-')
    print(time)
    # content
    content_body = soup.find_all('div', class_='field-item even')[1]
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def reporter(response):
    web = '報導者The Reporter'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('div', class_='metadata__DateSection-sc-1c3910m-3 gimsRe').text
    time = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', time_info)
    print(time)
    # content
    content_body = soup.find('div', class_='article-page__ContentBlock-sc-1wuywdb-8 irqyDp')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def rti(response):
    web = '中央廣播電台'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time = soup.find('li', class_='date').text.split('：')[1].split(' ')[0]
    print(time)
    # content
    content_body = soup.find('section', class_='news-detail-box')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def setn(response):
    web = '三立新聞網'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1', class_='news-title-3').text
    print(title)
    # time
    time = soup.find('time', class_='page-date').text.split(' ')[0].replace('/', '-')
    print(time)
    # content
    content_body = soup.find('div', id='Content1')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def sina(response):
    web = '臺灣新浪網'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time = soup.find('cite').text.split(' ')[1].replace('(', '')
    print(time)
    # content
    content = soup.find('div', class_='pcont').text.replace('　', '').strip()
    print(content)

    return title, content, time, web

def sevencar(response):
    web = '7car 小七車觀點'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h2').text
    print(title)
    # time
    time = soup.find('div', class_='meta_time').text.split(' ')[0].replace('/', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='article_container h_arr')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def sportsv(response):
    # print(response)
    web = '運動視界 Sports Vision'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time = soup.find('div', class_='date').text.replace('/', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='article-content')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def storm(response):
    web = '風傳媒'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1', id='article_title').text
    print(title)
    # time
    time = (soup.find('span', id='info_time').text).split(' ')[0]
    print(time)
    # content
    content_body = soup.find('div', id='CMS_wrapper')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def talkltn(response):
    web = '自由時報'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time = soup.find('div', class_='writer_date').text.split(' ')[0]
    print(time)
    # content
    content_body = soup.find('div', class_='cont')
    content_body.find('p', class_='appE1121').extract()
    content = ''
    for c in content_body.find_all('p'):
        content += c.text
    print(content)

    return title, content, time, web

def taronews(response):
    web = '芋傳媒 TaroNews'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('span', class_='post-title').text
    print(title)
    # time
    time_info = soup.find('time', class_='post-published updated')
    time = (time_info.find('b').text).split(' ')[0]
    print(time)
    # content
    content_body = soup.find('div', class_='entry-content clearfix single-post-content')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def thenewslens(response):
    web = 'The News Lens 關鍵評論網'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1', class_='article-title').text.strip()
    print(title)
    # time
    time = soup.find('div', class_='article-info').text.strip().split(',')[0].replace('/', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='article-main-box')
    content_list = content_body.find_all('p')
    content = content_body.find('h5').text
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def travelnews(response):
    web = '宜蘭新聞網'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('div', class_='post-date').text.split(' ')[0]
    time = re.sub(r'(\d+)年(\d+)月(\d+)日', r'\1-\2-\3', time_info)
    print(time)
    # content
    content_body = soup.find('div', class_='article-content clearfix')
    for cb in content_body.find_all('div', class_='text-center'):
        cb.extract()
    for cb in content_body.find_all('div', class_='wp-caption aligncenter'):
        cb.extract()
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def tvbs(response):
    web = 'TVBS旅食樂'  # TVBS新聞
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('div', class_='icon_time time leftBox2')
    time = (time_info.text).split(' ')[0].replace('/', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='h7 margin_b20')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def ubrand(response):
    web = '倡議家'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1', id='story_art_title').text
    print(title)
    # time
    time = soup.find('div', class_='story_bady_info_author').text.strip().replace('/', '-').split(' ')[0]
    print(time)
    # content
    content_body = soup.find('div', class_='story_body_content')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text.strip()
    print(content)

    return title, content, time, web

def udn(response):
    web = '聯合新聞網'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find(id='story_art_title').text
    print(title)
    # time
    time_info = soup.find('div', class_='story_bady_info_author')
    time = (time_info.find('span').text).split(' ')[0]
    print(time)
    # content
    content_body = soup.find('div', id='story_body_content')
    content_body.find('div', 'modal-content-body')
    content_body.find('div', id='myModal2')
    content_body.find('div', id='myModal3')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        if c.find('figure'):
            de = c.find('figure')
            c = c.text
            c = c.replace(de.text, '')
            content += c
            continue
        content += c.text.strip()
    print(content)
    return title, content, time, web

def udnmedia(response):
    web = '上報'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h2', id='ArticleTitle').text
    print(title)
    # time
    time_info = soup.find('div', class_='author')
    time = (time_info.text).strip().split(' ')[0]
    time = re.sub(r'(\d+)年(\d+)月(\d+)日', r'\1-\2-\3', time)
    print(time)
    # content
    content_body = soup.find('div', class_='editor')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def walkerland(response):
    web = 'WalkerLand窩客島'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time = soup.find('span', class_='text').text.split('｜')[0]
    print(time)
    # content
    content_body = soup.find('div', class_='user')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text.replace('\n', '')
    print(content)

    return title, content, time, web

def wealth(response):
    web = '財訊'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('div', class_='entry-header')
    time = re.sub(r'(\d+)-(\d+)-(\d+).*', r'\1-\2-\3', (time_info.find('p').text))
    print(time)
    # content
    content_body = soup.find('div', id='cms-article')
    content_body.find('p', class_='main-img-intro').extract()
    content = ''
    for c in content_body.find_all('p'):
        content += c.text
    print(content)

    return title, content, time, web

def worldj(response):
    web = '世界日報'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('time', class_='date').text.split(' ')[0].split('\n')[2]
    time = re.sub(r'(\d+)年(\d+)月(\d+)日', r'\1-\2-\3', time_info)
    print(time)
    # content
    content_body = soup.find('div', class_='post-content')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        if re.match('●', c.text):
            continue
        content += c.text
    print(content)

    return title, content, time, web

def yahoostock(response):
    web = 'yahoo奇摩股市'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('span', class_='t1')
    time = (time_info.text).split(' ')[0].replace('/', '-')
    print(time)
    # content
    content_body = soup.find('td', class_='yui-text-left')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def yahoo(response):
    web = 'yahoo!新聞'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('time')
    time = (time_info.text).split(' ')[0]
    time = re.sub(r'(\d+)年(\d+)月(\d+)日', r'\1-\2-\3', time)
    print(time)
    # content
    content_body = soup.find('div', class_='canvas-body Wow(bw) Cl(start) Mb(20px) Lh(1.7) Fz(18px) D(i)')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
    print(content)

    return title, content, time, web

def techbang(response):
    web = 'T客邦'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'post-title').text.strip()
    print(title)
    content_list = objSoup.find('div', 'article-content').find_all('p')
    content = ''
    for i in content_list:
        content += i.text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('p', 'post-meta-info').find_all('span')[2].text.split(' ')[1].replace('年', '-').replace('月','-').replace('日', '')
    print(time)
    return title, content, time, web

def hkepc(response):
    web = '電腦領域'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('title').text
    print(title)
    content = ''
    if objSoup.find('div', 'headerBanner reviewEditorsChoice').find('p') != None:
        content += objSoup.find('div', 'headerBanner reviewEditorsChoice').find('p').text
    content_list = objSoup.find('div', 'content').find_all('p')
    for i in content_list:
        content += i.text.strip()
    print(content)
    time = objSoup.find('div', 'publishDate').text.strip()
    print(time)
    return title, content, time, web

def cool3c(response):
    web = 'Cool3c 癮科技'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'col-12').text
    print(title)
    content_list = objSoup.find('div', 'row content').find_all('p')
    content = ''
    for i in content_list:
        content += i.text.strip()
    print(content)
    time = objSoup.find('div', 'created slacken').text.strip().split(' ')[0].replace('.', '-')
    print(time)
    return title, content, time, web

def gnn(response):
    web = '巴哈姆特電玩資訊站'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('div', 'BH-lbox GN-lbox3 gnn-detail-cont').find('h1').text.strip()
    print(title)
    content = objSoup.find('div', 'GN-lbox3B').find('div').find('div').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('p', 'GN-lbox3A').find('span').text.split(' ')[4]
    print(time)
    return title, content, time, web

def bnext(response):
    web = '數位時代'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'article_title bitem_title').text.strip()
    print(title)
    content = objSoup.find('article', 'main_content').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('div', 'col ctnBox').find('span', 'item').text.strip().replace('.', '-')
    print(time)
    return title, content, time, web

def sogi(response):
    web = 'SOGI 手機王'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'd-inline-block m-0').text.strip()
    print(title)
    content = objSoup.find('div', 'editable my-2').text.strip().replace('\r', '').replace('\n', '')
    print(content)
    time = objSoup.find('div', 'media-body').find_all('div', 'd-inline-block mr-2')[1].text.strip().split('：')[1].replace('/', '-')
    print(time)
    return title, content, time, web

def ithome(response):
    web = 'iThome Online'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'page-header').text.strip()
    print(title)
    content = objSoup.find('div', 'contents-wrap').find('div', 'field-item even').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('div', 'submitted').find('span', 'created').text.strip()
    print(time)
    return title, content, time, web

def epochtimes(response):
    web = '大紀元'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'blue18 title').text.strip()
    print(title)
    content_list = objSoup.find('div', id='artbody').find_all('p')
    content = ''
    for i in range(len(content_list) - 1):
        content += content_list[i].text.strip()
    print(content)
    time = objSoup.find('div', 'mbottom10 large-12 medium-12 small-12 columns').find('time').text.strip().split(' ')[1]
    print(time)
    return title, content, time, web

def turnnews(response):
    web = '翻爆'
    objSoup = BeautifulSoup(response.body, 'html.parser')
    title = objSoup.find('span', 'post-title').text.strip()
    if objSoup.find('h2', 'post-subtitle') is None:
        None
    else:
        title += objSoup.find('h2', 'post-subtitle').text.strip()
    print(title)
    content = objSoup.find('div', 'entry-content clearfix single-post-content').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('div', id='ft-single-meta-max').text.strip().split('・')[0]
    print(time)
    return title, content, time, web

def ctee(response):
    web = '工商時報'
    objSoup = BeautifulSoup(response.body, 'html.parser')
    title = objSoup.find('span', 'post-title').text.strip()
    print(title)
    content_list = objSoup.find('div', 'entry-content clearfix single-post-content').find_all('p')
    content = ''
    for i in content_list:
        content += i.text.strip()
    print(content)
    time = objSoup.find('time', 'post-published updated').text.strip().split('T')[0].replace('.', '-')
    print(time)
    return title, content, time, web

def mem(response):
    web = '新電子'
    objSoup = BeautifulSoup(response.body, 'html.parser')
    title = objSoup.find('div', 'title').text.strip()
    print(title)
    content_list = objSoup.find('div', 'alltxt').find_all('p')
    content = ''
    for i in content_list:
        content += i.text.strip()
    print(content)
    time = objSoup.find('div', 'data').find('span').text.strip().split('：')[1].replace('/', '-')
    print(time)
    return title, content, time, web

def yahoomoney(response):
    web = 'Yahoo奇摩理財'
    objSoup = BeautifulSoup(response.body, 'html.parser')
    title = objSoup.find('h1', 'Fw-b Fz-27 C-n').text.strip()
    print(title)
    content_list = objSoup.find('div', 'Ln-15 Fz-l C-darkgray content-body').find_all('p')
    content = ''
    for i in content_list:
        content += i.text.strip()
    print(content)
    time = objSoup.find('cite', 'Mstart-6 Fz-s Fs-n C-grayishblue').text.strip().split(' ')[0].replace('年','-').replace('月','-').replace('日', '')
    print(time)
    return title, content, time, web

def foxsports(response):
    web = 'Fox體育台'
    objSoup = BeautifulSoup(response.body, 'html.parser')
    title = objSoup.find('h1', 'entry-title').text.strip()
    print(title)
    content = objSoup.find('div', 'entry-content').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('time', 'meta-date').text.strip().replace('/', '-')
    print(time)
    return title, content, time, web

def gamers4(response):
    web='4Gamers'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('title').text.strip()
    print(title)
    content = objSoup.find('article', 'render-content').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('main', 'p-3').find('time').text.strip().split(' ')[0].replace('年', '-').replace('月','-').replace('日', '')
    print(time)
    return title, content, time, web

def meet(response):
    web = 'Meet'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'article_title').text.strip()
    print(title)
    content = objSoup.find('div', 'content htmlview').text.strip().replace('\n', '')
    print(content)
    time_list = objSoup.find('div', 'article_info').find_all('span', 'item')[1].text.strip().split('：')[1].replace(' ','').split('/')
    time = time_list[2] + '-' + time_list[0] + '-' + time_list[1]
    print(time)
    return title, content, time, web

def zeek(response):
    web = 'ZEEK玩家誌'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'entry-title').text.strip()
    print(title)
    content = objSoup.find('div', 'td-post-content').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('time', 'entry-date updated td-module-date').text.strip()
    print(time)
    return title, content, time, web

def buzzorange(response):
    web = 'TechOrange'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'entry-title').text.strip()
    print(title)
    content = objSoup.find('div', 'fb-quotable').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('time', 'entry-date published updated').text.strip().replace('/', '-')
    print(time)
    return title, content, time, web

def yamnews(response):
    web = 'yamNews蕃新聞'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h2', 'newsTitle').text.strip()
    print(title)
    content = objSoup.find('article', 'newsArticle').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('span', 'time').text.strip().split(' ')[0].replace('.', '-')
    print(time)
    return title, content, time, web

def petsettoday(response):
    web = 'ETtoday寵物雲'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'title').text.strip()
    print(title)
    content_list = objSoup.find('div', 'story').find_all('p')
    content = ''
    for i in content_list:
        if i.text.find('▲') != -1 or i.text.find('►') != -1 or i.text.find('▼') != -1:
            None
        else:
            content += i.text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('time', 'news-time').text.strip().split(' ')[0].replace('年', '-').replace('月', '-').replace('日','')
    print(time)
    return title, content, time, web

def autosyahoo(response):
    web = 'Yahoo奇摩汽車'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'title').text.strip()
    print(title)
    content_list = objSoup.find('div', 'content news-content-16 jq-add-blank').find_all('p')
    content = ''
    for i in range(1, len(content_list)):
        if content_list[i].text.find('更多詳細資訊') != -1:
            break
        else:
            content += content_list[i].text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('div', 'info-list').find('div', 'detail').find_all('span')[1].text.strip().split(' ')[0]
    print(time)
    return title, content, time, web

def hk01(response):
    web = '香港01'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'n743at-3 bhhWoS sc-gqjmRU iEiEQ').text.strip()
    print(title)
    content_list = objSoup.find_all('p', 'u02q31-0 gvqXdj sc-gqjmRU gBjLGB')
    content = ''
    for i in range(1, len(content_list)):
        content += content_list[i].text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('time').text.strip().split(' ')[0]
    print(time)
    return title, content, time, web

def hkfinanceyahoo(respnse):
    web = '雅虎香港新聞'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1',
                         'Lh(36px) Fz(25px)--sm Fz(32px) Mb(17px)--sm Mb(20px) Mb(30px)--lg Ff($ff-primary) Lts($lspacing-md) Fw($fweight) Fsm($fsmoothing) Fsmw($fsmoothing) Fsmm($fsmoothing) Wow(bw)').text.strip()
    print(title)
    content_list = objSoup.find_all('p', 'canvas-atom canvas-text Mb(1.0em) Mb(0)--sm Mt(0.8em)--sm')
    content = ''
    for i in range(0, len(content_list)):
        if content_list[i].text.strip().find('延伸閱讀') != -1:
            break
        else:
            content += content_list[i].text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('div', 'auth-prov-soc Mend(4px) Va(m) D(tbc) Mah(45px) Mah(40px)--sm Maw(320px) Fz(14px)').find('time','date Fz(11px) Mb(4px) D(ib)').text.strip().split('T')[0].replace('年', '-').replace('月', '-').replace('日', '')
    print(time)
    return title, content, time, web

def mingpao(response):
    web = '明報新聞網'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('hgroup').find('h1').text.strip()
    print(title)
    content = objSoup.find('article', 'txt4').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('div', id='articleTop').find('div', 'date').text.strip().split('日')[0].replace('年','-').replace('月','-')
    print(time)
    return title, content, time, web

def rmim(response):
    web = '《現代保險》雜誌'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('div', id='news_detail').find('div', 'news_detail_block1x2_col1_row3 cap1').text.strip()
    print(title)
    content = objSoup.find('div', id='news_detail').find('div','news_detail_block1x2_col1_row6 txt3').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('div', id='news_detail').find('div', 'news_detail_block1x2_col1_row4 txt2').text.strip().split('|')[1].strip().replace('.', '-').split(' ')[0]
    print(time)
    return title, content, time, web

def cmmedia(response):
    web = '信傳媒'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h4', 'article_title cc02').text.strip()
    print(title)
    content = objSoup.find('div', 'article_content').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('div', 'article_author-bar').find_all('span')[1].text.strip().split(' ')[0]
    print(time)
    return title, content, time, web

def ydn(response):
    web = '青年日報'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h3', 'article__news-title').text.strip()
    print(title)
    content_list = objSoup.find('article', 'article').find_all('p')
    content = ''
    for i in range(2, len(content_list)):
        content += content_list[i].text.strip()
    print(content)
    time = objSoup.find('div', 'section-heading__news-toolbar').find('li', 'news-toolbar__cell').text.strip()
    print(time)
    return title, content, time, web

def smart(response):
    web = 'smart智富月刊'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('section', 'article').find('h1').text.strip()
    print(title)
    content_list = objSoup.find('section', 'article').find_all('p')
    content = ''
    for i in range(2, len(content_list)):
        if content_list[i].text.find('延伸閱讀') != -1:
            None
        else:
            content += content_list[i].text.strip()
    print(content)
    time = objSoup.find('section', 'article').find('h5').find('span', 'writter').text.strip().split('：')[2]
    print(time)
    return title, content, time, web

def sportsyahoo(response):
    web = 'Yahoo奇摩運動'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1','Lh(36px) Fz(25px)--sm Fz(32px) Mb(17px)--sm Mb(20px) Mb(30px)--lg YahooSans-Bold Ff($ff-primary) Lts($lspacing-md) Fw($fweight) Fsm($fsmoothing) Fsmw($fsmoothing) Fsmm($fsmoothing) Wow(bw)').text.strip()
    print(title)
    content_list = objSoup.find('div','canvas-body Wow(bw) Cl(start) Mb(20px) Fz(17px) Lh(1.6) YahooSans-Regular D(i)').find_all('p')
    content = ''
    for i in range(len(content_list)):
        content += content_list[i].text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('div', 'auth-prov-soc Mend(4px) Va(m) D(tbc) Mah(45px) Mah(40px)--sm Maw(320px) Fz(14px)').find('time', 'date Fz(11px) Mb(4px) D(ib)').text.strip().replace('年', '-').replace('月', '-').replace('日', '')
    print(time)
    return title, content, time, web

def one(response):
    web = '1111產經新聞網'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('div', id='titlecon').find('h1').text.strip()
    print(title)
    content = objSoup.find('div', style='width:677px;').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('div', id='content_news').find_all('p')[1].text.strip().split(' ')[0].replace('/', '-')
    print(time)
    return title, content, time, web

def womany(response):
    web = '女人迷 womany'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', itemprop='name headline').text.strip()
    print(title)
    content = objSoup.find('section', 'article-body').text.strip().replace('\r', '').replace('\n', '')
    print(content)
    time = objSoup.find('aside', 'article-actions top').find('time').text.strip().replace('/', '-')
    print(time)
    return title, content, time, web

def crossing(response):
    web = '換日線 Crossing'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'article-page-title serif').text.strip()
    print(title)
    content_list = objSoup.find('div', 'text-input').find_all('p')
    content = ''
    for i in content_list:
        content += i.text.strip().replace('\r', '').replace('\n', '')
    print(content)
    time = objSoup.find('div', 'article-info').find('span', 'date').text.strip().replace('/', '-')
    print(time)
    return title, content, time, web

def topick(response):
    web = '香港經濟日報 - TOPick'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('div', 'article-detail_title').find('h1').text.strip()
    print(title)
    content_list = objSoup.find('div', 'article-detail-content-container').find_all('p')
    content = ''
    for i in range(len(content_list) - 1):
        content += content_list[i].text.strip().replace('\r', '').replace('\n', '')
    print(content)
    time = objSoup.find('span', 'article-details-info-container_date').find_all('span', 'font-en')[
        1].text.strip().replace('/', '-')
    print(time)
    return title, content, time, web

def cosmopolitan(response):
    web = '柯夢波丹 (台灣)'
    objSoup = BeautifulSoup(response.body, 'lxml')
    title = objSoup.find('h1', 'content-hed listicle-hed').text.strip()
    print(title)
    content = ''
    if objSoup.find('div', 'listicle-intro') is None:
        None
    else:
        content += objSoup.find('div', 'listicle-intro').text.strip()
    content += objSoup.find('div', 'listicle-body-content').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('time', 'content-info-date').text.strip().replace('\n', '').replace('/', '-')
    print(time)
    return title, content, time, web


dict={'money.udn.com':EconomicDaily,
      'video.udn.com':VideoUdn,
      'www.digitimes.com.tw':DigiTimes,
      'www.ustv.com.tw':Ustv,
      'globalnewstv.com.tw':GlobalNewsTv,
      'www.businesstoday.com.tw':BusinessToday,
      'news.cts.com.tw':CTS,
      'news.xfastest.com':XFastest,
      'm.eprice.com.tw':EPrice,
      'chinese.engadget.com':Engadget,
      'www.kocpc.com.tw':Kocpc,
      'www.cardu.com.tw':Cardu,
      'www.chinatimes.com':chinatimes,
      'www.cna.com.tw':cna,
      'news.cnyes.com':cnyes,
      'csr.cw.com.tw':csr,
      'www.cw.com.tw':cw,
      'e-info.org.tw':einfo,
      'news.ebc.net.tw':ebc,
      'ec.ltn.com.tw':ecltn,
      'www.ettoday.net':ettoday,
      'www.eventsinfocus.org':eventsinfocus,
      'finance.technews.tw':fitech,
      'technews.tw':fitech,
      'www.gvm.com.tw':gvm,
      'market.ltn.com.tw':market,
      'www.mirrormedia.mg':mirror,
      'newtalk.tw':newtalk,
      'www.setn.com':setn,
      'www.sportsv.net':sportsv,
      'www.storm.mg':storm,
      'news.tvbs.com.tw':tvbs,
      'udn.com':udn,
      'www.upmedia.mg':udnmedia,
      'www.walkerland.com.tw':walkerland,
      'tw.stock.yahoo.com':yahoostock,
      'tw.news.yahoo.com':yahoo,
      'taronews.tw':taronews,
      'www.ntdtv.com.tw':ntdtv,
      'www.twreporter.org':reporter,
      'fnc.ebc.net.tw':fncebc,
      'times.hinet.net':hinet,
      'www.inside.com.tw':inside,
      'www.7car.tw':sevencar,
      'www.peopo.org':peopo,
      'www.mygonews.com':mygonews,
      'ubrand.udn.com':ubrand,
      'www.worldjournal.com':worldj,
      'www.ntdtv.com':ntdtvs,
      'www.rti.org.tw':rti,
      'hk.on.cc':hkon,
      'www.thenewslens.com':thenewslens,
      'www.travelnews.tw':travelnews,
      'wealth.businessweekly.com.tw':business,
      'www.wealth.com.tw':wealth,
      'www.bbc.com/zhongwen':bbc,
      'www.nownews.com':nownews,
      'www.ctwant.com':ctwant,
      'tw.mobi.yahoo.com':mobiyahoo,
      'news.sina.com.tw':sina,
      'www.managertoday.com.tw':manager,
      'www.moneydj.com':moneydj,
      'talk.ltn.com.tw':talkltn,
      'www.businessweekly.com.tw':businessw,
      'www.peoplenews.tw':people,
      'www.techbang.com':techbang,
      'www.hkepc.com':hkepc,
      'www.cool3c.com':cool3c,
      'gnn.gamer.com.tw':gnn,
      'www.bnext.com.tw':bnext,
      'www.sogi.com.tw':sogi,
      'www.ithome.com.tw':ithome,
      'www.epochtimes.com':epochtimes,
      'turnnewsapp.com':turnnews,
      'ctee.com.tw':ctee,
      'www.mem.com.tw':mem,
      'tw.money.yahoo.com':yahoomoney,
      'www.foxsports.com.tw':foxsports,
      'www.4gamers.com.tw':gamers4,
      'meet.bnext.com.tw':meet,
      'zeekmagazine.com':zeek,
      'buzzorange.com':buzzorange,
      'n.yam.com':yamnews,
      'pets.ettoday.net':petsettoday,
      'autos.yahoo.com.tw':autosyahoo,
      'www.hk01.com':hk01,
      'hk.finance.yahoo.com':hkfinanceyahoo,
      'news.mingpao.com':mingpao,
      'www.rmim.com.tw':rmim,
      'www.ydn.com.tw':ydn,
      'smart.businessweekly.com.tw':smart,
      'tw.sports.yahoo.com':sportsyahoo,
      'www.1111.com.tw':one,
      'womany.net':womany,
      'crossing.cw.com.tw':crossing,
      'topick.hket.com':topick,
      'www.cosmopolitan.com':cosmopolitan,
      }


def getCrawler(key,response):
    title=None
    content=None
    time=None
    web=None
    try:
        title,content,time,web=dict[key](response)
        return title,content,time,web
    except:#當未寫到該爬蟲框架時需做錯誤處理
        return title,content,time,web