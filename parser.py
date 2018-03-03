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
    schMmealScCode = code #int 1조식2중식3석식
    schYmd = ymd #str 요청할 날짜 ex:"2017.11.17"
    if weekday == 5 or weekday == 6: #토요일,일요일 버림
        element = " "
    else:
        num = weekday + 1 #int 요청할 날짜의 요일 0월1화2수3목4금5토6일 파싱한 데이터의 배열이 일요일부터 시작되므로 1을 더해줍니다.
        URL = (
                "http://stu.use.go.kr/sts_sci_md01_001.do?"
                "schulCode=A000000000&schulCrseScCode=4&schulKndScCode=04"
                "&schMmealScCode=%d&schYmd=%s" % (schMmealScCode, schYmd)
            )
        #http://stu.AAA.go.kr/ 관할 교육청 주소 확인해주세요.
        #schulCode= 학교고유코드
        #schulCrseScCode= 1유치원2초등학교3중학교4고등학교
        #schulKndScCode= 01유치원02초등학교03중학교04고등학교
        #으로 변경해 주시면 됩니다.
        html = get_html(URL)
        soup = BeautifulSoup(html, 'html.parser')
        element = soup.find_all("tr")
        element = element[2].find_all('td')
        try:
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
        except:
            element = " "
    return element
