# 장고를 이용한 인스타그램 클론 코딩
### *MVT 개념
모델 : DB  
템플릿 : 유저가 보는 화면  
뷰 : 모델-템플릿 중계  

### *가상환경
```
python -m venv myenv
```
```
source myenv/scripts/activate # 활성화

deactivate # 비활성화
```

### *프로젝트 실행
```
python manage.py runserver
```
http://127.0.0.1:8000  
127.0.0.1 로컬 호스트 : 자신을 의미  
8000 : 포트번호, 외부에서 들어오는 요청을 받아들임
<hr/>

# MVT 구조 이해하기

### 1. 프로젝트 생성
```
django-admin startproject kinsta
```

```
cd kinsta
```

### 2. Django가 사용할 데이터베이스 생성
```
python manage.py migrate
```

<hr/>

### 3. html 파일 넣는 장소
> kinsta/templates/kinsta/index.html 생성  
> kinsta/kinsta/settings.py
```
TEMPLATES = [
    'DIRS': [BASE_DIR / 'templates'], # 추가
] 
```
<hr/>

### 4. Django Rest Framework 설치
```
pip install djangorestframework
```

### 5. url 연결 (rest_framework 이용)
#### 템플릿-뷰 과정
1. templates에 html 생성
2. views.py에 함수 등록
3. urls.py에서 url에 따라 함수를 불러옴
> kinsta/kinsta/views.py 생성
```
from django.shortcuts import render
from rest_framework.views import APIView

class sub(APIView): # 클래스형 뷰
    def get(self, request): # get 요청이 왔을 때
        return render(request, "index.html")
```

urls.py -> views.py -> templates의 html 실행
> kinsta/kinsta/urls.py
```
from .views import index, membership

urlpatterns = [
    path('', sub.as_view(), name='index'), # 추가, 127.0.0.1:8000/'' 호출하면 이 함수 실행    
]

```

<details>
<summary>현재까지의 파일 구조</summary>

* kinsta
  * (앱을 사용한다면 디렉토리가 위치할 곳)
  * db.sqlite3  
  * manage.py  
  * kinsta/  
      * settings.py  
      * urls.py  
      * views.py
  * templates/  
      * html 파일들
</details>

<hr/>

# 메인화면 만들기

### 6. content 앱 만들기
```
python manage.py startapp content
```

### 7. 부트스트랩 이용
> 웹 페이지의 아이콘, 버튼같은 것들이 디자인 되어있는 패키지

https://getbootstrap.kr/docs/5.3/getting-started/introduction/#%eb%b9%a0%eb%a5%b8-%ec%8b%9c%ec%9e%91

빠른 시작 코드 붙여넣기 -> 부트스트랩 코드 사용 가능

### 8. 상단 바 만들기
부트스트랩에서 내비게이션 바(Navbar)
https://getbootstrap.kr/docs/5.3/components/navbar/#%eb%82%b4%eb%b9%84%ea%b2%8c%ec%9d%b4%ec%85%98-%eb%b0%94

'Hello, world!' 대신 붙여넣기, 검색 기능도 넣기

### 9. 구글 머티리얼 아이콘 사용
https://fonts.google.com/icons

가이드 잘 읽고 따라하기  
홈, 탐색, 메시지, 알림, 만들기 아이콘 추가


<hr/>
https://youtu.be/M8UPyeF5DfM
