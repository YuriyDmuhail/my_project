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




# xPath locators

# $x("//nav/a")
# $x("//button[@class='btn header-link'][1]")
# $x("//button[@class='btn header-link'][2]")
# $x("//button[@class='header-link -guest']")
# $x("//button[@class='btn btn-outline-white header_signin']")
# $x("//svg[@xmlns='http://www.w3.org/2000/svg']")
#
# $x("//h1[@class='hero-descriptor_title display-2']")
# $x("//div[@class='col-md-6 d-flex flex-column align-items-center align-items-md-start']/h2")
# $x("//div[@class='col-md-6 d-flex flex-column align-items-center align-items-md-end justify-content-md-end mb-2 mt-3 mt-md-0']/a[@class='contacts_link display-4']")
# $x("//div[@class='col-md-6 d-flex flex-column align-items-center align-items-md-end justify-content-md-end mb-2 mt-3 mt-md-0']/a[@class='contacts_link h4']")
# $x("//div[@class='col-7 d-flex flex-column justify-content-center footer_item -left']/p[1]")
# $x("//span[@class='socials_icon icon icon-linkedin']")
# $x("//span[@class='socials_icon icon icon-instagram']")
# $x("//span[@class='socials_icon icon icon-facebook']")
# $x("//div[@class='about-block']/p[@class='about-block_title h2'][1]")
# $x("//div[@class='about-block_picture about-picture']/img[@class='about-picture_img'][1]")
# $x("//div[@class='hero-descriptor']/button[@class='hero-descriptor_btn btn btn-primary']")
# $x("//div[@class='ytp-title-channel ytp-title-show-collapsed']/a[@class='ytp-title-channel-logo']")
# $x("//div[@class='ytp-cued-thumbnail-overlay']/button/svg")
# $x("//div[@class='ytp-watch-later-title']")
# $x("//div[@class='ytp-share-title']")
# $x("//div[@class='ytp-title-text']/a[@class='ytp-title-link yt-uix-sessionlink']")
# $x("//div[@class='ytp-share-icon']/svg")
# $x("//div[@class='ytp-watch-later-icon']/svg")
# $x("//div[@class='col footer_item -right']/a/svg")





