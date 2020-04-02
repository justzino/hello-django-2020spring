class User(object):
    pass# hello-django-2020spring
 간단한 설문조사(Polls) 어플리 케이션 만들기
 
## 첫 번째 장고 앱 작성하기, part 1
## 사용 명령어

- virtualenv 디렉토리명(venv)  `가상환경 생성`
- .\Scripts\activate `가상환경 실행`
- pip install django `django 설치`
- django-admin startproject 디렉토리명 `Django project를 실행할 폴더 생성`
- django-admin startapp 이름(polls, user, order, project...) `app생성`
- python manage.py runserver `서버 실행`   
    - python manage.py runserver 8080   `포트8080으로 서버 시작`

---
#### 1. views.py
#### 2. urls.py
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
#### 3. path() 함수 인수에 대해
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

---
---

## 첫 번째 장고 앱 작성하기, part 2
## 사용 명령어

- python manage.py makemigrations polls `모델의 변경(생성)을 migration으로 저장`
- python manage.py migrate  `데이터베이스 테이블 만들기, 변경사항 적용`
- python manage.py sqlmigrate polls 0001 `migration이름을 인수로 받아, 실행하는 SQL 문장을 보여줌`
- python manage.py shell `Python 쉘에서 Django가 접근할 수 있는 Python 모듈 경로를 그대로 사용가능 - 시험용`
- python manage.py createsuperuser  `관리자 생성하기`
- python manage.py runserver    `개발 서버 시작`

### 1. 기본 어플리케이션
settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',         # 관리용 사이트. 곧 사용하게 될 겁니다.
    'django.contrib.auth',          # 인증 시스템.
    'django.contrib.contenttypes',  # 컨텐츠 타입을 위한 프레임워크.
    'django.contrib.sessions',      # 세션 프레임워크.
    'django.contrib.messages',      # 메세징 프레임워크.
    'django.contrib.staticfiles',   # 정적 파일을 관리하는 프레임워크.
]
```

### 2. Django 모델 API
#### 1. **INSERT**  
데이타를 삽입하기 위해서는 먼저 테이블에 해당하는 모델(Model Class)로부터 객체를 생성하고, 그 객체의 save() 메서드를 호출하면 된다.
save() 메서드가 호출되면, SQL의 INSERT이 생성되고 실행되어 테이블에 데이타가 추가된다.

#### 2. **SELECT**  
Django는 디폴트로 모델 틀래스에 대해 "objects"라는 Manager(django.db.models.Manager) 객체를 자동으로 추가한다.   
- 사용 :ModelClass.objects.QueryMethod
- Query란?
    - 데이터 베이스에 정보를 요청하는 것.  
    - 쿼리는 웹 서버에 특정한 정보를 보여달라는 웹 클라이언트 요청(주로 문자열을 기반으로 한 요청)에 의한 처리이다.
- 자주 사용되는 주요 메서드
    - all() : 테이블 데이터를 전부 가져오기   
    ex) User 테이블의 모든 데이터의 id와 name 컬럼을 출력
    ```python
    for u in User.objects.all():
        s += str(u.id) + ' : ' + u.name + '\n' 
    ```
    
    - get() : 하나의 Row만을 가져오기 위한 메서드  
    ex) Primary Key(일반적으로 id 컬럼)가 1인 row를 가져오기
    ```python
    row = User.objects.get(pk=1)    #pk = primary key
    print(row.name)
    ```
    
    - filter() : 특정 조건에 맞는 Row들을 가져오기 위한 메서드  
    ex) name 필드가 Lee인 데이터만 가져오기
    ```python
    rows = User.objects.filter(name='Lee')
    ``` 
    
    - exclude() : 특정 조건을 제외한 나머지 Row 가져오기 위한 메서드  
    ex)  name 필드가 Lee가 아닌 데이터만 가져오기
    ```python
    rows = User.objects.exclude(name='Lee')
    ```
    
    - count() : 데이터의 갯수(row 수)를 세기위한 메서드
    ```python
    n = User.objects.count()
    ```
    
    - order_by() : 데이터를 key에 따라 정렬. 인자로 정렬키를 나열할수 있고, 앞에 -가 붙으면 내림차순이다.  
    ex) id 올림차순, date 내림차순으로 정렬
    ```python
    rows = User.objects.order_by('id','-date')
    ```
  
    - distinct() : 중복된 값은 하나로만 표시하기 위한 메서드. SQL의 SELECT DISTINCT와 같은 효과  
    ex) name 필드가 중복되는 경우 한번만 표시
    ```python
    rows = User.objects.distinct('name')
    ```
  
    - first() : 데이터들 중 처음에 있는 row만 return  
    ex) name 필드 정렬 후 처음 row를 return 하기
    ```python
    rows = User.objects.order_by('name').first()
    ```
  
    - last() : 데이터들 중 마지막에 있는 row를 return  
    ex) name 필드 정렬 후 마지막 row return
    ```python
    rows = User.objects.order_by('name').last()
    ```
#### 3. **UPDATE**  
데이터를 수정하기 위해 먼저 수정할 Row 객체를 얻은 후 변경할 필드들을 수정한다.  
이어 마지막에 save() 메서드를 호출하면, SQL의 UPDATE가 실행되어 테이블에 데이터가 갱신된다.  
ex) id=1인 User 객체의 이름을 변경하기
```python
tmp = User.objects.get(pk=1)
tmp.name = 'Kim'
tmp.save()
```

#### 4. **DELETE**  
데이터를 삭제하기 위해서는 먼저 삭제할 Row 객체를 얻은 후 delete()메서드를 호출한다. 
ex) id=2인 User객체 삭제
```python
user1 = User.objects.get(pk=2)
user1.delete()
```   

Link: [참고](http://pythonstudy.xyz/python/article/310-Django-%EB%AA%A8%EB%8D%B8-API, "Django 모델 API")

#### 5. Model API에 대한 몇가지 정리 사항 
- choice_set 등장  
    - 구현한적 없는 q.choice_set.all() 라는 메서드가 등장.
    - 이는 기본적으로 객체에 접근할 수 있는 Manager 객체의 이름은 모델명(**소문자**)_set 으로 지어진다고 한다.  
    ex) class Choice 의 Manager 객체 = choice_set
    ```python
    q.choice_set.all()
    q.choice_set.create(choice_text='Not much', votes=0)
    q.choice_set.count()
    ```
  
-  Field lookups : SQL의 WHERE 절에 해당하는 부분이다.
    - QuerySet methods인 filter(), exclude(), get() 에 키워드 인자의 형태로 전달된다.
    - 형태 : `field__lookupType=조건값`  
    ```python
    Question.objects.get(pub_date__year=current_year)
    Choice.objects.filter(question__pub_date__year=current_year)
    ```  

### 3. Django 관리자 사이트
`python manage.py createsuperuser`  
관리자 사이트에서 편집 가능한 그룹과 사용자와 같은 몇 종류의 컨텐츠를 볼 수 있다.
이것들은 django.contrib.auth 모듈에서 제공되는데, Django 에서 제공되는 인증 프레임워크이다.
- 관리 사이트에서 poll app 을 변경가능하도록 만들기
 polls/admin.py
 ```python
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```