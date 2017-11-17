import requests
from bs4 import BeautifulSoup
import re


def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html


def get_diet(code, ymd, weekday):
    schMmealScCode = code #int
    schYmd = ymd #str
    num = weekday + 1 #int 0월1화2수3목4금5토6일
    URL = (
            "http://stu.sen.go.kr/sts_sci_md01_001.do?"
            "schulCode=B100000519&schulCrseScCode=4&schulKndScCode=04"
            "&schMmealScCode=%d&schYmd=%s" % (schMmealScCode, schYmd)
        )
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find_all("tr")
    element = element[2].find_all('td')
    element = element[num] #num
    element = str(element)

    element = element.replace('[', '')
    element = element.replace(']', '')
    element = element.replace('<br/>', '\n')
    element = element.replace('<td class="textC last">', '')
    element = element.replace('<td class="textC">', '')
    element = element.replace('</td>', '')
    element = element.replace('(h)', '')
    element = element.replace('.', '')
    element = re.sub(r"\d", "", element)
    return element
