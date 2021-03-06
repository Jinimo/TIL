# Web Crawling
> - 웹 페이지 정보 가져오는 방법
>
> - 과도한 데이터 수집은 서버에 무리 및 보안 문제 발생



```python
 ! pip install 라이브러리명
```
 - `!` : 콘솔창에 해당 명령어 실행 (콘솔 창에서 실행시 제외)
 - `pip` : 파이썬 라이브러리 설치 명령어
 - `pip install 라이브러리명` : 지정 라이브러리 컴퓨터에 설치   



-------------------
 - `.get()`  
 - `.page_source`
 - ``
-------------------
 ## 1. selenium
> - Chrome,  Internet Explorer, Safari 등 다양한 브라우저에서 사용 가능 
> - `requests` 진행시 소스를 받아오지 못하는 경우에 사용
> - 줄 웹앱을 테스트하는데 사용하는 프레임워크
> - `webdriver`라는 API를 통해 운영체제에 설치된 크롬 등의 브라우저를 제어
> - `selenium` module 설치 후 사용 

![셀레니움 element 사용](/Users/hyunjinkim/Downloads/셀레니움 element 사용.PNG)



ChromeDriver - WebDriver for Chrome:
 https://chromedriver.chromium.org/downloads



크롬: https://chromedriver.chromium.org/downloads

Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/-

파이어폭스:https://github.com/mozilla/geckodriver/releases



**Chrome 브라우저**

- `selenium`으로 작동하는 `Chrome driver` -> 별도 파일 다운로드 필요

- Chrome 버전 확인 -> 운영체제, Chrome 버전과 일치하는 `Chrome driver` 파일 찾고 다운 



 0. 명령어
  - `driver.find_elements_by_css_selector('조건')` : 원하는 조건의 태그 찾기 (BeautifulSoup 별도 사용 필요 X)
    
    * 조건 : 태그명/ id 값/ 부모 태그 등의 구조 정보 (CSS Selector)   
    
    
 1. selenium  라이브러리 설치
 ``` python
 ! pip install selenium
 ```
 2.  selenium 라이브러리의 webdriver 불러오기
 ```python
 from selenium import webdriver
 from selenium.webdriver.common.keys import Keys
 ```
3. Chrome driver 실행
```python
from selenium import webdriver
driver = webdriver.Chrome('Chrome driver 파일 경로/파일명.exe')
```
4.  웹 페이지 접속 (Chrome 브라우저 이용)
```python
url = 'https://www.google.com/'
driver.get(url)
```
5. 웹 페이지 HTML 다운로드
```python
html = driver.page_source
```



```python
from selenium.webdriver import Chrome       # 크롬 웹 브라우저 
#from selenium import webdriver as wd        
from selenium.wsebdriver.common.by import By # 드라이버 로드 통해 사이트 접속 가능하도록 

# 사전에 필요한 정보 로드 (디비 or 쉘, 뱌치 파일에서 인자로 받아서 검색)
url = "검색 사이트 url 주소"     
keyword = "검색어" 

# 드라이브 로드 
# 차후 옵션 부여하여 (프록시, 에이전트 조작, 이미지를 배제) 속도 향상됨
# 크롤링을 오래 돌리면 => 임시파일들이 쌓인다!! -> 템포 파일 삭제
#driver = wd.Chrome(executable_path="./chromedriver")
driver = Chrome("")

# 사이트 접속 
driver.get(url)

```





-------------------


 ## 2. BeautifulSoup 



    0. 명령어

**데이터 (태그) 찾기**

- `.find("태그명")` : 첫번째 태그만 검색

- `.find_all("태그명")`=`.findAll("태그명")` : 전체 태그 검색 -> list형태로 반환

**데이터 (태그) 선택하기**

- `.select('조건)` : 조건 = 태그명/속성값(id값, class명)

  - `.select('태그명)`

  - `.select('속성값')` -> `.select('id 값')` / `.select('class명')`

    - `class 속성` :  서식 지정 하기위해 사용. HTML 내 동일한  class명 여러번 사용 가능 

    - `id 값` : 특정 대상 지정. HTML 내 한번만 사용 가능 -> id 값 활용하여 태그 검색 용이

- `.select('태그명.속성값)`



  1. bs4 패키지 설치

``` python
!ip install bs4
```
  2. HTML 해석

```python
from bs4 import BeautifulSoup as bs

# 변수에 들어있는 특정 문자열 정보 -> HTML 형식 맞게 해석
soup = bs(html, 'html.parswe') 
```
 3. 태그 선택 - `.slect('조건')` 사용 

   - 태그 하나만 선택 
```python
tags = soup('조건')
tag_1 = tags[0]   # tags의 첫번째 원소(인덱스 번호 0 )
print(tag_1)
```
  - 태그 하나씩 선택 - 반복문(for)
  ```python
  tags = soup('조건')
  for tag in tags:
    print(tag)
  ```
  4. 태그 정보 가져오기 - `.text`
```python
content = Tag.text       # 화면에 보이는 글 추출
attribute = Tag['속성명']  # 태그 내 속성 값
link =  Tag['href']      #  화면에 안보이는 URL 주소 수집 
```
```python
tags = soup.select('a')  # 태그명 'a'인 태그 선택 
tag = tags[0]            # tags의 인덱스 0번(첫번째) 원소 
content = tag.text       # tag에 저장된 화면에 보이는 텍스트 부분 추출
link =  tag['href']      # tag의 URL 주소 추출
```

  5. selenium + BeautifulSoup 웹 크롤링 정리(Chrome) 예시
```python
#  selenium - 크롬 브라우저 조작 -> 웹페이지 접속
driver = webdriver.Chrome('Chrome driver 파일 경로/파일명.exe')
url = '주소'
driver.get(url)

# BeautifulSoup - 원하는 정보 추출 
html = driver.page_source
soup = bs(html, 'html parser')

tags = soup.select('조건')
for tag in tags: 
  tag_1 = tag.selct('조건')[0].text
  tag_2 = tag.selct('조건')[0].text
  print(tag_1, tag_2)
```



