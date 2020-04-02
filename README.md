# hello-django-2020spring

## 첫 번째 장고 앱 작성하기, part 1
 간단한 설문조사(Polls) 어플리 케이션 만들기

## 사용 명령어

- virtualenv 디렉토리명(venv)  `가상환경 생성`
- .\Scripts\activate `가상환경 실행`
- pip install django `django 설치`
- django-admin startproject 디렉토리명 `Django project를 실행할 폴더 생성`
- django-admin startapp 이름(polls, user, order, project...) `app생성`
- python manage.py runserver `서버 실행`   
    - python manage.py runserver 8080   `포트8080으로 서버 시작`

---
### 1. views.py
### 2. urls.py
    - view 호출을 위해 URLconf를 생성
- polls/urls.py
```python
urlpatterns = [
    path('', views.index, name='index'),
]
```
- mysite/urls.py
```python
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
- path() 함수 인수에 대해
    - 필수 인수 : route, view
    - 선택 인수 : kwargs, name
    ```python
    from django.urls import path
    
    path(route, view, kwargs=None, name=None)
    ```
    - route: URL pattern을 가진 문자열
        - 도메인 이름 이후 요청된 URL을 각 패턴과 리스트의 순서대로 비교
        - 각 pattern들은 GET/POST의 매개변수 검색x
    - view
        - 일치하는 패턴을 찾으면, HttpRequest 객체를 첫번째 인수로,
        - view함수 호출
    - kwargs
    - name
        - URL에 이름을 부여 -> Django 어디서나 명확히 참조
        
