### *프로젝트 실행
```
python manage.py runserver
```
http://127.0.0.1:8000
127.0.0.1 로컬 호스트 : 자신을 의미
8000 : 포트번호, 외부에서 들어오는 요청을 받아들임

### 0. 가상환경
```
python -m venv myenv
source myenv/scripts/activate # 활성화

deactivate # 비활성화
```

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




https://youtu.be/M8UPyeF5DfM