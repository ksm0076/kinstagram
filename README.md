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
> kinsta/templates/index.html 생성  
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

# 피드화면 만들기

<hr/>
https://youtu.be/M8UPyeF5DfM
