# 🐯Korea_Hackathon
2021 1.9 ~ 1.10    
🐯 고려대학교 해커톤 대회 - 순천향대학교 멋쟁이사자처럼  

## ⚡Link
- [홈페이지 링크](http://anaso.ml/)

## DEMO

### 메인

<img src="./DEMO/메인.gif" width="450px" />

### 회원가입

<img src="./DEMO/회원가입.gif" width="450px" />

### 포트폴리오

<img src="./DEMO/포트폴리오.gif" width="450px" />

### 프로젝트 템플릿

<img src="./DEMO/프로젝트생성.gif" width="450px" />

### 공모전 신청

<img src="./DEMO/공모전.gif" width="450px" />
![image](https://user-images.githubusercontent.com/60251579/119508186-8053d600-bdaa-11eb-98bb-69d5b9dd4c7b.png)



### 


## 🏆 수상 내역 (23개 팀 참가)

### 심사위원 상😍 수상 ( 심사위원 100% 평가 + 상금 100만원 ) 

![image](https://user-images.githubusercontent.com/60251579/104265631-612a6b00-54d1-11eb-92ef-2d69a2a1d3a7.png)  
![image](https://user-images.githubusercontent.com/60251579/104265278-8c608a80-54d0-11eb-8668-2a464728421b.png)  


## 👨‍👨‍👨‍👧‍👧Creater Member

### 🔙Back-end
- [최민석](https://github.com/minsgy) 🚩Team Leader, 🏷[고카톤후기](https://velog.io/@minsgy/고카톤-대회-출전-후기고카톤)
- [이남준](https://github.com/ningpop)  
- [김태완](https://github.com/wwan13)  

### 🔜Front-end
- [장하얀](https://github.com/white-jang)  
- [하유민](https://github.com/qhahd78)  

## 📑 프로젝트 명세서  

### 🏆 ANASO Service  
![image](https://user-images.githubusercontent.com/60251579/104265697-8323ed80-54d1-11eb-93e0-14686e87ab22.png)  

### 📁 Database Class UML
![image](https://user-images.githubusercontent.com/60251579/104265839-d138f100-54d1-11eb-992f-3802ad7fbacf.png)  

### 📃 File Directory  
📦users - App  
📦contest - App  
📦main - App  
📦projects - App  
📦config - Django 프로젝트 파일  
📦static - STATIC FILE 모음  





## ⏱Tech Stack
- Django : 2.2.1  
- Django-Templates  
- Python3  
- HTML5  
- CSS3  
- JS  
- JQuery  


## Commit Rule

- 커밋 메세지 작성시 '[nickname] : message' 의 형식으로 작성  

- 네이밍은 다음과 같이 작성함.  

  - Front-end  
    - Point
      - 시멘틱 Web 구성 신경 쓰기. (center, main, header, footer)  
      - Flex 남발 금지. (적재적소에만 사용하기. 반응형에 알맞는 곳)  
      - class name 작성 시, 띄어쓰기 '-'로 사용. `<div class='logo-item'></div>`  
    
    - templates
      - VS Code - settings - format on save 켜서 코드 정리 자동화
      - 페이지 최상단에 주석으로 페이지 간략 설명, 작성일 표기
      - 백엔드가 봤을 때 필요한 기능들을 단 번에 알 수 있도록 하기
      - 한 문서에서 동일한 ID 2번 이상 사용하지 않음.
      - CSS 작성시 base.html 의 스타일을 확인한 뒤 중복된 선택자 없이 작성
      
  - Back-end
    - Model Class
      - 모델 클래스의 첫 글자는 대문자로 한다.

    - App Folder
      - APP 폴더 이름은 첫 글자는 소문자로 한다.
      - APP 폴더 이름은 기능이 복수 일 경우, 's'를 붙힌다.
      - 예) comments, users

    - View Function
      - 함수(메소드)에 낙타 표기법 적용
        - 예) getName() ...
      - 변수(필드)에 팟홀 표기법 적용
        - 예) MyFirstVariable -> my_first_variable

    - Templates
      - templates 폴더는 APP 폴더 별로 나누어 관리한다.

    - Static
      - 각 App 폴더 static 폴더를 생성하여 저장한다.
      - `python manage.py collectstatic` 을 통해 모든 static 파일을 모은다.
      - css
        - css를 담는 폴더 명이며, css 명은 html과 동일 시 한다.
      - js
        - js를 담는 폴더 명이며, js 명은 html과 동일 시 한다.
        
