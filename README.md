School_Meal_Parser_Python
============
- - -
>전국 초,중,고 식단표 파서

나이스 학생서비스 페이지를 파싱하여 급식정보를 출력해 줍니다.


변수 설명
---------
소스코드의 주석 참고


사용 예시
---------
<pre><code>
  from parser import*
  
  #parser.py를 먼저 수정해 주세요.
  
  
  meal = get_diet(2, "2017.11.17", 4) #중식, 2017년 11월 17일, 금요일
  print(meal)

</code></pre>

활용 예제: [디스코드_봇](https://github.com/M4ndU/inhun_discord_bot2), [카카오톡_봇](https://github.com/M4ndU/inhun_kakao_api2)


설치해야되는 파이썬 라이브러리
---------
- parser.py
  - __requests__ library
  - __BeautifulSoup4__ library
  - __regex__ library

- - -
