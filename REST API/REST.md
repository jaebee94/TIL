# REST API

> API : Application Programming Interface



## 데이터의 표기법

"약속"

### JSON

- JavaScript Object Notation (JavaScript 객체식 표기법)



#### Why not HTML?

- HTML의 제한된 태그로는 각 데이터를 분류하기 힘들다.
- 그래서 등장한게 XML
- 그렇지만 코드의 길이가 길어지기 때문에 (닫는 태그 때문에) **JSON**을 사용한다.
- 뿐만 아니라 문서의 구조를 정의하다보면 코드가 더 길어진다.



#### Why JSON?

- 코드가 짧은 것은 "돈"과 연관되어 있다.
- 짧은 코드 -> 적은 데이터 패킷, 사용 디스크 용량, 메모리 용량, 시간 등
- 웹이 빈번하게 데이터를 교환하기 때문에 적은 차이라도 격차는 엄청 벌어진다.



*" **Django** 에서 **JSON** 형식에 맞춰서 **Data** 만 제공한다."*



## API 서버

***"요청은 URL로 보낸다."***

-> JSON 형식으로 된 응답을 받는다.



URL : 자원의 위치 표시



### RESTful

1. http verb

   GET, POST, PUT/PATCH, DELETE, ...

2. 명사(복수형)로 구성

   `/articles/1/new`와 같은 url 은 RESTful하지 않다.