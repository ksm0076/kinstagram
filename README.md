# 장고를 이용한 인스타그램 클론 코딩 (CSS, DB 연결)

### *MVT 구조
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

### 3. html 파일 넣는 장소
> kinsta/templates/kinsta/index.html 생성  
> kinsta/kinsta/settings.py
```
TEMPLATES = [
    'DIRS': [BASE_DIR / 'templates'], # 추가
] 
```

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

```
# rest_framework 사용 안한 기본 형태
def index(request):
    return render(request, 'index.html')
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
<summary> **5.1 앱 만들고 url 연결** </summary>

**1. 앱 생성**  
**2. templates 생성**  
**3. view 함수 등록**  
**4. 앱의 url 설정**  
**5. 프로젝트 url에서 앱 연결**  


1. 앱 생성
```
python manage.py startapp content
```

2. 앱에 대한 html 담을 폴더 생성 (kinsta/templates/kinsta 폴더가 있는 곳)
> kinsta/templates/content 생성

3. views.py에 함수 등록
> kinsta/content/views.py
```
class test(APIView):
    def get(self, request):
        return render(request, 'content/test.html') # templates/content/test.html 불러옴
```

4. urls.py에서 함수를 불러옴
> kinsta/content/urls.py 생성
```
urlpatterns = [
    path('test', test.as_view(), name='test'), # http://localhost:8000/content/test 경로로 접근
]
```

5. kinsta의 urls에서 앱의 url 연결
> kinsta/kinsta/urls.py
```
urlpatterns = [
    path('content/', include('content.urls')) # 추가
]
```
</details>

<details>
<summary>현재까지의 파일 구조</summary>

* kinsta
  * db.sqlite3  
  * manage.py  
  * kinsta/  
    * settings.py  
    * urls.py  
    * views.py
  * content/ (앱)
    * urls.py
    * views.py
  * templates/  
    * kinsta
      * main.html
    * content
      * test.html
</details>

<hr/>


<details>
<summary>메인화면 만들기</summary>

### 부트스트랩 이용
> 웹 페이지의 아이콘, 버튼같은 것들이 디자인 되어있는 패키지

https://getbootstrap.kr/docs/5.3/getting-started/introduction/#%eb%b9%a0%eb%a5%b8-%ec%8b%9c%ec%9e%91

빠른 시작 코드 붙여넣기 -> 부트스트랩 코드 사용 가능

### 구글 머티리얼 아이콘 사용
https://fonts.google.com/icons

### [css-flex 익히기](https://studiomeal.com/archives/197)

### 6. 상단 바 만들기

### 7. 하단 정렬
display: flex = 가로 방향으로 배치  
justify-content: center = 가운데 정렬  
padding-top:55px = 상단 바와의 간격

<details>
<summary>margin과 padding의 차이</summary>

* margin : 외부에서 밀어주는 느낌
* padding : 내부에서 미는 느낌
</details>


### 8. 상단 바 고정, 오른쪽 고정, 상단 바 페이지의 가로 꽉 채우기

### 9. 좌측 피드 만들기

1. 사용자 정보
2. 사진 부분
3. 아이콘
4. 댓글 부분

### 10. 우측 추천 목록 만들기
</details>
<hr/>

# 모델 구조 (DB연결, ORM)
ORM : Object Relational Mapping

객체-DB 매핑, SQL을 사용하지 않고도 DB 작업 수행 가능

<hr/>
https://youtu.be/M8UPyeF5DfM
