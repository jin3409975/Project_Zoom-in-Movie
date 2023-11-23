# 🔎 ZnMovie (2023.11.16 ~ 2023.11.24)
    Zoom in Movie
<br>

<br>

<br>

# 1. 팀원 정보 및 업무 분담 내역
<br>

## 1 - 1. 차현철 (팀장)
> Back
- accounts 및 movies 앱 관련 코드 작성
- 영화 추천 알고리즘 작성 및 수정
- Django-seed를 통한 더미데이터 생성
- TMDB API를 활용한 fixtures *.json 영화데이터 생성

<br>

> Front
- pinia-plugin-persistedstate 라이브러리를 통한 웹 local-storage 활용
- Django 서버의 Movie 및 Accounts 데이터베이스와 연결 및 데이터 교환
- 데이터베이스 내의 영화 데이터에서 인기도 등 원하는 데이터 출력
- 댓글 CRUD 코드 작성 및 실시간 데이터베이스 반영
- 전반적인 CSS 담당
    - lodash 라이브러리를 활용한 랜덤 배경 출력
    - Typed.js 라이브러리를 활용한 글자 출력
    - Youtube API를 활용한 관련 영상 출력
    - 반응형 웹을 활용한 화면 구성
    - 그 외 웹 페이지 디자인

<br>

## 1 - 2. 이지은 (팀원)
> Back
- Django-rest-auth를 활용한 accounts 관리 및 authorization 설정
- accounts 및 movies 앱 관련 코드 작성
- 영화 추천 알고리즘 작성 및 수정
- Front에서의 axios 요청에 대한 데이터 응답 코드 작성

<br>

> Front
- Django 데이터베이스와 회원가입 및 로그인을 연동
- Accounts 데이터베이스와 연결 및 데이터 교환
- Stores 관련 코드 작성

## 1 - 3. 공통업무
- ERD 작성 및 Component 구조도 작성
- 웹 페이지 구성요소 결정
- README 작성
  


<br>
<br>
<br>


# 2. 목표 서비스 구현 및 실제 구현 정도 
<br>

## 2 - 1. 목표 서비스

### 1. 영화 추천 서비스

    1) 사용자의 좋아요 기반 같은 장르 추천
    2) 인기도와 평점 순 영화 추천

### 2. 영화 상세 조회

    1) Youtube 관련 영상 재생
    2) 좋아요 및 댓글 기능

### 3. 영화 댓글
   
    1) 각 영화마다 댓글 생성, 조회, 수정, 삭제 가능

### 4. 로그인 상태에 따른 페이지 접근 권한 제한
    1) 로그아웃 상태 : 회원가입, 로그인, 메인 페이지 제외 접근 불가
    2) 로그인 상태 : 회원가입 페이지 제외 모든 페이지 접근 가능



<br>

## 2 - 2. 실제 구현 정도

### 1. 영화 추천 서비스

    1) 사용자가 좋아요를 누른 경우 : 사용자의 좋아요 기반 같은 장르 추천
    2) 사용자가 좋아요를 누르지 않은 경우 : 인기도 순, 평점 순 영화 추천

### 2. 영화 상세 조회

    1) Youtube 공식 예고편 재생
    2) 영화 정보 조회 가능
    3) 좋아요 버튼
    4) 댓글 작성, 조회, 수정, 삭제 가능
	
### 3. 영화 댓글

    1) 각 영화의 상세 페이지에서 댓글 작성, 조회, 수정, 삭제 가능
      >> 댓글 수정, 삭제는 작성자만 가능

### 4. 로그인 상태에 따른 페이지 접근 권한 제한
    
    1) 로그아웃 상태 : 회원가입, 로그인, 메인 페이지 제외 접근 불가
    2) 로그인 상태 : 회원가입 페이지 제외 모든 페이지 접근 가능

<br>
<br>
<br>


# 3. 데이터베이스 모델링 (ERD)
<br>
<br>

![Alt text](ERD.drawio.png)


<br>

# 4. 영화 추천 알고리즘

    1) 사용자가 좋아요를 누른 경우
      좋아요를 누른 영화의 장르를 기반으로 같은 장르의 영화 추천
      - 이미 선택한 장르라면 
        >> 가중치를 더해서 정렬한 후 상위 3개의 장르를 추출해서 영화를 추천
    
    2) 사용자가 좋아요를 누르지 않은 경우
      - 가장 높은 평점을 받은 상위 30개의 영화를 추천
      - 가장 인기있는 상위 30개의 영화를 추천



<br>
<br>
<br>


# 5. 기능 설명
<br>


| 기능               | 기능 설명                                                               |
| ---------------- | ------------------------------------------------------------------- |
| 회원가입, 로그인        | Dj-Rest-Auth 라이브러리의 authtoken을 사용한 인증, 해당 페이지에 인기도 상위 5개 영화의 배경 랜덤 노출                                          |
| 로그아웃             | Dj-Rest-Auth라이브러리 활용 및 authtoken 삭제                                                  |
| 사용자 접근 권한            | 로그인 상태에 따른 페이지 접근 제한                                           |
| nav bar             | 원하는 페이지로 이동 가능 및 스크롤에 따른 숨김 및 노출                                                   |
| 메인 화면             | 인기도 상위 5개 영화의 배경에 제목과 명대사 노출로 사용자의 흥미를 이끌어냄, 인기도 순 상위 30개의 영화 추천                   |
|나만의 영화 추천     | 사용자의 좋아요를 기반으로 사용자가 선호하는 장르의 영화 추천
| 카테고리      | nav bar의 드롭다운에서 원하는 장르를 선택하면 해당 장르의 영화를 모아서 제공
| 영화 상세 페이지     | Youtube 공식 예고편, 줄거리, 장르, 좋아요, 댓글 제공                            |
| 좋아요           | 해당 영화의  좋아요 추가 및 삭제 정보를 데이터베이스에 저장 >> 사용자 맞춤 영화 추천에 사용
| 영화 댓글       | 영화 상세 페이지에서 해당 영화에 대한 댓글 조회, 작성, 수정, 삭제 가능 >> 댓글 수정, 삭제는 작성자만 가능
|

<br>
<br>
<br>


# 6. 느낀 점
<br>


## 6 - 1. 차현철

    Typed.js 등 여러 라이브러리를 활용해서 사용자의 흥미를 불러일으키는 새로운 기술을 조사하고 활용할 수 있다는 것이 프로젝트의 장점 중 하나라고 생각한다. 또한 프로젝트의 종료 날짜가 다가오면서 팀원과의 소통과 기획의 중요함을 깨달았다. 사용자의 경험과 웹 사이트의 실제 운영을 예상하지 않으면 개발 기간이 더 소요되었고, 필요없는 개발에 기간을 낭비하기도 했다.

<br>
<br>

## 6 - 2. 이지은

    웹 사이트 하나를 온전하게 만들어 본 건 처음이었다. 
    한 학기 동안 배웠던 모든 것을 총동원해야 하는 작업들이 절대 쉽지 않았다. 
    하나하나 해 나아가야 할 때마다 수업자료를 찾아보고 실습자료를 들여다보면서 비로소 이해하게 된 것들이 많았다. 
    가장 어려웠던 건 django와 vue의 데이터를 연결하는 것이었는데, 도대체 어디서 어떻게 연결해서 
    정보를 불러오고 내보내야 하는지 알 수 없어서 상당히 힘들었다.
    하지만 원하는 기능을 마침내 구현해냈을 때 느낀 기쁨이 다음으로 넘어갈 수 있는 힘을 줬고, 프로젝트를 완성할 수 있게 했다. 
    이번 프로젝트는 어렵기도 했지만, 흥미롭기도 했다.
    많은 것들을 가능하게 만들어 준 팀장에게 고마움을 전한다.