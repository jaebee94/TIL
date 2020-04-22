# Django

## 1. 프로젝트 및 APP 초기 설정

### 프로젝트 생성

```bash
$ django-admin startproject {프로젝트명}
```



### 앱 생성

```bash
$ python manage.py startapp {앱 이름}
```



### 설정(Settings.py)

```python
# HOST
ALLOWED_HOST =['*'] # 장고가 돌아갈 URL을 지정. ('*'는 모든 호스트에서 가능하게 한다는 뜻.)

# 앱 등록
INSTALLED_APPS = [
    '앱 이름',
]

# 언어, 시간
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```



## 2. Model 정의

```python
class Article(models.Model):
    title = models.CharField()
    content = ...
    # ForeignKey 가 있는 경우
    user = models.ForeignKey()
```



## 3. ModelForm 정의

> **왜 ModelForm 을 쓰는가?**
> Model에 정의한 Field대로 html 코드를 자동으로 만들어주기 위해. 편리함

```python
class ArticleForm(forms.ModelForm):
    # ModelForm은 필드에 대한 정보를 담고있는데, ArticleForm에 대한 정보를 담는 곳이 class Meta
    class Meta:
        model = 
        fields = []
```



## 코드 작성 흐름

> 하나의 요청을 처리하기 위해서 가져야 하는 흐름 (urls -> views -> templates)

### 1. urls.py

* (path) url -> view의 함수로 연결시키는 동작

```python
# app_name별 Namespace, 여러 개의 app이 있는 경우 path name의 충돌을 방지
app_name = 'articles'
urlpatterns = [
    # path에 name을 정의해주는 이유는 url을 변수화하여 활용하기 위함
    # url이 변경되더라도 view, template의 코드를 수정할 필요가 없음
    path('create/', views.create, name="create"),
]
```



### 2. views.py

* 함수 (인자 -> 반환(return))

```python
def ____(request, pk):	# (HTTP Request obj, variable)
    # Model에서의 정보들을 가져오는 Query Method,
    # Template에 필요한 context
    return _____	# HTTP Response obj(1. render 2. redirect)  => Template
```



### 3. Templates.py

- 넘겨받은 context 값으로 DTL을 이용하여 HTML을 만들어 줌

- request, user, ... -> context-processors

- 확장(상속) : base.html

  ```html
  {% extends 'base.html' %}
  ```

- APP_DIRS, DIR 설정

  - DIR 먼저 탐색하고, APP_DIRS 를 탐색하는데,
  - APP_DIRS 는 install한 APP 순서대로 탐색
  - app 별로 templates 의 경로가 충돌하지 않도록 `articles/templates/articles/~.html`와 같이 경로설정



### 4. 정적 파일(Static files)

- APP 폴더 내의 static 폴더 안에 정의해주면 된다.(JS, CSS, Images, ...)
- 추가적인 디렉토리 설정 가능

```html
{% load static %}
...
```



## django의 기본

- 클래스 / 상속
- Name (import, 변수)

### 클래스

- 동작 (메서드)

- 상태 (변수)

- OOP(Object Oriented Programming)

- S + V (주어 + 동사)로 생각해보자

  ```python
  article = Article.get()
  article.title	# article의 title이 뭐야?
  ```

### Import

- 폴더구조라고 생각하면 편하다.
- django
  - db
    - models.py
  - urls
    - path, include
  - views
    - decorators
  - shortcuts
  - contrib
    - admin
    - auth
      - 함수들, forms, decorators

```python
# urls.py
from django.urls import path
from django.urls import path, include

# form.py
from django import forms

# models.py
from django.db import models

# auth
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
```



Class -> 캐멀 케이스

변수명, 메서드 -> 스네이크

settings.py -> 대문자 스네이크

단/복수

app -> 복수

model -> 단수



## Auth

> Model(내부에 있는 User 모델), Form(ModelForm) 가져다 쓴다.
>
> 커스텀 하고 싶으면 가져다가 상속

### Example

- 회원가입 : User, UserCreatiionForm (ModelForm)

- 로그인 : 실제로 대응되는 모델 X, AuthenticationForm, Form -> 사용 시 유의. request객체에 담겨져 있는 정보로 처리가 되어야 한다. **request 매우 중요**

  ```python
  # request를 첫번째 인자로 넘겨준다.
  form = AuthenticationForm(request, request.POST)
  auth_login(request, form.get_user())	# 유저정보를 넘겨줘야 한다.
  ```

  