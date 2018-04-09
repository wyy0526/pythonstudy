import whois
#import urllib3
import requests
import re
import urljoin
import urllib
from urllib import robotparser
from urllib import request
from urllib import error
from urllib import parse



# w = whois.whois("baidu.com")
# print(w)

url = 'http://webscraping.com'
rp = robotparser.RobotFileParser()
rp.set_url(urljoin.url_path_join(url, 'robots.txt'))
rp.read()

def download(url, user_agent='wyy', proxy =None, retries=2):
    print('Downloading:', url)
    headers = {'User-agent':user_agent}

    if not rp.can_fetch(user_agent, url):
        print('Blocked by robots.txt:', url)
        return None

    req = request.Request(url, headers=headers)
    opener = request.build_opener()
    if proxy:
        proxy_params = {parse.urlparse(url).schema: proxy}
        opener.addheaders(request.ProxyHandler(proxy_params))
    try:
        html = opener.open(req).read()
    except error.URLError as e:
        print('Download error:', e.reason)
        html = None
        if retries > 0:
            if hasattr(e, 'errno') and 500 <= e.errno <600:
                return download(url, user_agent='Baiduspider', proxy =None, retries=retries-1)
    #print('aaa：',html.decode('utf-8'))
    return html.decode('utf-8')

def link_crawler(seed_url, link_regex):
    """
    :param seed_url:主页面地址
    :param link_regex:正则表达式
    :return:Node
    """
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url, user_agent='Baiduspider', proxy=None, retries=2)
        for link in get_links(html):
            #print('seen:', seen)
            if re.match(link_regex, link, re.I):
                link = urljoin.url_path_join(seed_url, link)
                #print('link1:', link)
                if link not in seen:
                    crawl_queue.append(link)
                    seen.add(link)
                    #print('link2:', link)

def get_links(html):
    """
    :param html: 主页面
    :return: 主页面包含的链接地址list
    """
    webpage_regex = re.compile('<a href=\"(/.+?)\">', re.IGNORECASE)
    #print(html)
    #print('aaaaaaaaaaaaaaaa')
    #print('bbbbbbbbbbbbbbbb')
    return webpage_regex.findall(html)


def main():
    soup = link_crawler(url, '.*(about)')
    print(soup)

if __name__ == '__main__':
    main()



