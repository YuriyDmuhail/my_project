from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth

# Завантаження HTML-сторінки
url = 'https://qauto2.forstudy.space/'

response = requests.get(url, auth=HTTPBasicAuth(
        "guest",
        "welcome2qauto"
    ))
html_content = response.content # html text
print(html_content)

# Аналіз HTML-документу з використанням BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
#
# Вилучення тексту з тегу <title> за допомогою CSS-локатора

title1 = soup.select_one('title')
meta_viewport = soup.select_one('meta[name="viewport"]')
favicon_icon = soup.select_one('link[rel="icon"][type="image/x-icon"]')
favicon_32 = soup.select_one('link[rel="icon"][sizes="32x32"]')
favicon_16 = soup.select_one('link[rel="icon"][sizes="16x16"]')
robots_meta = soup.select_one('meta[name="robots"]')
stylesheet = soup.select_one('link[rel="stylesheet"]')
base_tag = soup.select_one('base')
app_root = soup.select_one('app-root')
body_tag = soup.select_one('body')
head_tag = soup.select_one('head')
html_tag = soup.select_one('html')
charset_meta = soup.select_one('meta[charset="utf-8"]')
js_runtime = soup.select_one('script[src*="runtime"]')
js_polyfills = soup.select_one('script[src*="polyfills"]')
js_main = soup.select_one('script[src*="main"]')
icons = soup.select('link[rel="icon"]')
meta_tags = soup.select('meta')
scripts = soup.select('script')
links = soup.select('link')
defer_scripts = soup.select('script[defer]')
script_srcs = soup.select('script[src]')
title_fallback = soup.select_one('h1') or "H1 not found"
favicon_ico_href = soup.select_one('link[href$=".ico"]')





