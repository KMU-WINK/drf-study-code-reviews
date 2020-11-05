# django-rest-framework 코드리뷰 레파지토리

# drf-study-code-reviews

<img align="left" width="180" height="180" src="https://wink.kookmin.ac.kr/static/assets/logo/wink-color.png"></img>
**프로젝트 명 : WINK 공식 웹 사이트(kmu-wink-official)**
---
본 저장소는 django-rest-framework를 이용하여 REST-API를 만들어보는 스터디를 진행하며 코드리뷰를 받을 수 있는 저장소이다.
.

.

.

.

## 스터디 진행 방법


### master branch

master branch는 절때! 커밋, merge를 하면 안됩니다.
해당 브랜치를 이용하여 본인 브랜치를 만들때 사용을 합니다.


### username-master 브랜치

develop에서 과제 개발을 완료 후 pull request 를 보내는 브랜치입니다.

### username-develop 브랜치

과제를 할당 받고 개발하는 브랜치입니다. 해당 브랜치는 수시로 commit push를 통해 최신 상태를 유지합니다.

### pull request

과제 완료 후 병합 대상을 username-master 브랜치, 코드리뷰 받을 브랜치를 username-develop 브랜치로 하여 pull request를 작성합니다.

이후 스터디 팀원들과 코드리뷰를 진행하고 이상이 없다면 스터디장 이종휘가 merge 합니다.


### 새로운 과제 발생

새로운 과제는 Issues를 통해 할당합니다. 각 주마다 참여 인원들은 이슈를 통해 과제를 할당 받고 관련 질문을 Issues에 남깁니다.

### 질문 사항

질문 사항은 Issues에 Comment로 남겨 질문하도록합니다.

### 정보 공유

정보 공유는 Issues에 공유하도록합니다.


### PyCharm Django setting
 #### 가상환경 세팅
  1. sudo python3 -m virtualenv [가상환경을 설치할 경로]
  2. source [경로]/bin/activate 를 하여 가상환경에 접속합니다.
 
 #### 설치
  1. settings.py를 프로젝트 내 drf_study_code_reviews/settings.py로 저장합니다.
  2. 가상환경에서 sudo pip3 install -r requirement.txt를 실행합니다.
    - mysqlclient가 설치되지 않을 때.
      - brew install mysql을 한 후 다시 설치를 시도합니다. 
      - brew 설치 가이드 -> https://brew.sh/index_ko
      

 #### 프로젝트 실행 
 1. 우측 상단의 edit configuration 버튼을 클릭합니다.
 2. 창이 새로 떳다면 좌측 상단의 + 버튼을 누르고 Django server를 클릭합니다.
 3. Host를 0.0.0.0으로 설정합니다.

# 윙크 공식 홈페이지 개발팀
## 팀원 소개

<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/images/upload/ACF13837-13AE-4D45-878D-232B94553B24_1_105_c_lgyEbPJ.jpeg"></img>
```


17학번 이종휘

Role : 스터디장
GitHub : https://github.com/bell2lee


```

<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/images/upload/F7019A73-CA0C-47E2-8C90-B0F3646C4E5C.jpeg"></img>
```


17학번 박건후

Role : 스터디장
GitHub : https://github.com/parkgeonhu


```

<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/images/upload/123.PNG"></img>
```


17학번 정현구

GitHub : https://github.com/jhg3522


```


<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/images/upload/1.jpg"></img>
```


17학번 김현서

GitHub : https://github.com/gustj2005


```


<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/images/upload/25794831.jpeg"></img>
```


17학번 김태훈

GitHub : https://github.com/Kim-tang2


```


<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/images/upload/28584133.jpeg"></img>
```


17학번 김윤정

GitHub : https://github.com/wwjdtm


```


<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/images/upload/34D1B7FD-CB8E-428E-84E1-BC27E3F47B48.png"></img>
```


18학번 정소원

GitHub : https://github.com/sowish23


```


<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/images/upload/303D6E75-2EEB-4898-B8A5-C2A78D84225D.jpeg"></img>
```


18학번 허채림

GitHub : https://github.com/h0zzae


```


<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/assets/logo/wink-color.png"></img>
```


20학번 이지원

GitHub : https://github.com/easyandones


```


## 참조(Reference)

#### PAPER


## Contatc Us
``` Email : kmucs.wink@gmail.com ```