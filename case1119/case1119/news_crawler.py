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

def chinatimes(response):
    web = '中時電子報'
    soup = BeautifulSoup(response.text, 'html.parser')
    # title
    title = soup.find('h1').text
    print(title)
    # time
    time_info = soup.find('span', class_='date')
    time = (time_info.text).replace('/', '-')
    print(time)
    # content
    content_body = soup.find('div', class_='article-body')
    content_list = content_body.find_all('p')
    content = ''
    for c in content_list:
        content += c.text
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
    content_body.find('div', class_='modal-content-body').extract()
    content_body.find('div', id='myModal2').extract()
    content_body.find('div', id='myModal3').extract()
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
    content = objSoup.find('div', 'GN-lbox3B').text.strip().replace('\n', '')
    print(content)
    time = objSoup.find('p', 'GN-lbox3A').find('span').text.split(' ')[4]
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
      'www.chinatimes.com': chinatimes,
      'www.cna.com.tw': cna,
      'news.cnyes.com': cnyes,
      'csr.cw.com.tw': csr,
      'www.cw.com.tw': cw,
      'e-info.org.tw': einfo,
      'news.ebc.net.tw': ebc,
      'ec.ltn.com.tw': ecltn,
      'www.epochtimes.com': epochtimes,
      'www.ettoday.net': ettoday,
      'www.eventsinfocus.org': eventsinfocus,
      'finance.technews.tw': fitech,
      'technews.tw':fitech,
      'www.gvm.com.tw': gvm,
      'market.ltn.com.tw': market,
      'www.mirrormedia.mg': mirror,
      'newtalk.tw': newtalk,
      'www.setn.com': setn,
      'www.sportsv.net': sportsv,
      'www.storm.mg': storm,
      'news.tvbs.com.tw': tvbs,
      'udn.com': udn,
      'www.upmedia.mg': udnmedia,
      'www.walkerland.com.tw': walkerland,
      'tw.stock.yahoo.com': yahoostock,
      'tw.news.yahoo.com': yahoo,
      'www.techbang.com':techbang,
      'www.hkepc.com':hkepc,
      'www.cool3c.com':cool3c,
      'gnn.gamer.com.tw':gnn
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
