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
* 앱을 사용하지 않는 경우 (manage.py 파일이 있는 곳에 templates 폴더 생성)<br/>
kinsta/templates/index.html

* 앱 사용하는 경우
```
python manage.py startapp main
```
kinsta/main/templates/main/index.html

> settings.py
>> INSTALLED_APPS = [ 'main', ] 추가

### 4. Django Rest Framework 설치
```
pip install djangorestframework
```

### 5. url 연결

https://youtu.be/M8UPyeF5DfM