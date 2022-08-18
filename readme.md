## 프로젝트 실행 방법(순서대로 진행하기)

### 1. 레퍼지토리 클론
    git clone https://github.com/LikeLion-at-DGU/Fillme_Back.git

### 2. 가상환경 실행
    source myvenv/Scripts/activate

### 3-a. 라이브러리 설치
    pip install -r requirements.txt

### 3-b. reqirements.txt로 필요한 라이브러리 설치가 안된다면
    pip install django
    pip install djangorestframework
    pip install django-cors-headers
    pip install djangorestframework-simplejwt
    pip install dj-rest-auth
    pip install django-allauth
    pip install pillow

### 4. 프로젝트 폴더 위치로 이동 (manage.py 파일이 있는 위치)
    cd fillme

### 5. DB 마이그레이션
    python manage.py makemigrations
    python manage.py migrate

### 6. 서버 실행
    python manage.py runserver

## API

### 유저 회원가입 및 로그인/로그아웃

### 127.0.0.1:8000/accounts - POST 메소드 사용
    username, email, password1(비밀번호), password2(비밀번호 확인) 입력
    ex)
    {
        "username" : "유저네임 입력",
        "email" : "이메일형식 입력",
        "password1" : "비밀번호",
        "password2" : "비밀번호 확인"
    }

### 로그인
### 127.0.0.1:8000/accounts/login - POST 메소드 사용
    username, password 입력
    ex)
    {
        "username" : "유저네임",
        "password" : "비밀번호"
    }

### 로그아웃
### 127.0.0.1:8000/accounts/logout - POST 메소드 사용
    입력값 없이 POST방식으로 보내기


### 유저 메인 프로필 조회 및 수정(회원가입시 자동으로 생성되기 때문에 빈값의 프로필을 수정한다는 개념)
### 내 프로필
### 127.0.0.1:8000/mypage - GET 메소드 사용
#### 결과
    {
        "id" : "해당 프로필의 id 값(정수)",
        "user" : "유저의 id 값(정수)",
        "username" : "로그인할때 사용되는 사용자 아이디",
        "fullname" : "성명",
        "memo" : "한줄소개",
        "color" : "색상",
        "color_hex" : "색상 hex값",
        "image" : "프로필 사진"
        "followings" : []
    }

#### 프로필 사진은 파일 형식
#### color는 선택지가 있음
#### 프론트에서 가져올때 : profile.color 는 키값(ex. 'pink'), profile.get_color_display() 는 내용(ex. '#FEBCC0')

    COLOR_LIST = (
            ('pink', '#FEBCC0'),
            ('red', '#83333E'),
            ('lorange', '#FFB37C'),
            ('orrange', '#FF9A50'),
            ('yellow', '#FFE886'),
            ('green', '#153D2E'),
            ('lblue', '#8692CC'),
            ('blue', '#486FBB'),
            ('navy', '#1C0F67'),
            ('lpurple', '#8878E1'),
            ('purple', '#4D2E66'),
            ('etoffe', '#827165'),
            ('brown', '#231819'),
            ('gray', '#464648'),
            ('black', '#010101'),
        )

### 내 프로필 수정
### 127.0.0.1:8000/mypage/profile_update - PATCH 메소드 사용
    {
        "fullname" : "성명",
        "memo" : "한줄소개",
        "color" : "색상",
        "image" : "프로필 사진"
    }

### 다른 유저 프로필 조회
### 127.0.0.1:8000/mypage/<int:user_id> - GET 메소드 사용
#### 결과
    {
        "id" : "해당 프로필의 id 값(정수)"
        "user" : "유저의 id 값(정수)",
        "username" : "로그인할때 사용되는 사용자 아이디",
        "fullname" : "성명",
        "memo" : "한줄소개",
        "color" : "색상",
        "color_hex" : "색상 hex값",
        "image" : "프로필 사진",
        "followings" : []
    }

### 본인 페르소나 조회
### 127.0.0.1:8000/mypage/persona - GET 메소드 사용
#### 결과
    [
        {
            "id": "persona id 값",
            "user": "user id 값",
            "username" : "로그인할때 사용되는 사용자 아이디",
            "profile": "profile id 값",
            "name": "persona 1 이름",
            "category": "persona 1 카테고리",
            "image": "persona 1 이미지"
            "openpublic": true
        },
        {
            "id": "persona id 값",
            "user": "user id 값",
            "username" : "로그인할때 사용되는 사용자 아이디",
            "profile": "profile id 값",
            "name": "persona 2 이름",
            "category": "persona 2 카테고리",
            "image": "persona 2 이미지"
            "openpublic": true
        }
    ]

### 본인 페르소나 생성하기
### 127.0.0.1:8000/mypage/persona - POST 메소드 사용
    {
        "name" : "페르소나 이름",
        "category" : "카테고리",
        "image" : "페르소나 사진"
    }

### 본인 페르소나 조회하기(페르소나 detail)
### 127.0.0.1:8000/mypage/persona/<int:persona_id> - GET 메소드 사용
#### 결과
    {
        "id": "persona id 값",
        "user": "user id 값",
        "username" : "로그인할때 사용되는 사용자 아이디",
        "profile": "profile id 값",
        "name": "persona 2 이름",
        "category": "persona 2 카테고리",
        "image": "persona 2 이미지",
        "openpublic": true
    }

### 본인 페르소나 수정하기
### 127.0.0.1:8000/mypage/persona/<int:persona_id> - PATCH 메소드 사용
    {
        "name" : "페르소나 이름",
        "category" : "카테고리",
        "image" : "페르소나 사진"
    }

### 본인 페르소나 삭제하기
### 127.0.0.1:8000/mypage/persona/<int:persona_id> - DELETE 메소드 사용
### 결과
    {
        "persona_id": "삭제된 페르소나 id"
    }

### 다른 유저 페르소나 목록 조회하기
### 127.0.0.1:8000/mypage/<int:user_id>/persona - GET 메소드 사용
#### 결과
    [
        {
            "id": "persona id 값",
            "user": "user id 값",
            "username" : "로그인할때 사용되는 사용자 아이디",
            "profile": "profile id 값",
            "name": "persona 1 이름",
            "category": "persona 1 카테고리",
            "image": "persona 1 이미지",
            "openpublic": true
        },
        {
            "id": "persona id 값",
            "user": "user id 값",
            "username" : "로그인할때 사용되는 사용자 아이디",
            "profile": "profile id 값",
            "name": "persona 2 이름",
            "category": "persona 2 카테고리",
            "image": "persona 2 이미지",
            "openpublic": true
        }
    ]

### 다른 유저 페르소나 조회하기(persona detail)
### 127.0.0.1:8000/mypage/<int:user_id>/persona/<int:persona_id> - GET 메소드 사용
#### 결과
    {
        "id": "persona id 값",
        "user": "user id 값",
        "username" : "로그인할때 사용되는 사용자 아이디",
        "profile": "profile id 값",
        "name": "persona 1 이름",
        "category": "persona 1 카테고리",
        "image": "persona 1 이미지",
        "openpublic": true
    }

### 나의 페르소나 공개 여부 설정(persona detail)
### 127.0.0.1:8000/mypage/persona/<int:persona_id>/openpublic/ - PATCH 메소드 사용
    입력값 아무것도 없이 patch 메소드로 request 보내면 됨.
#### 결과(공개->비공개 전환 시 openpublic이 true에서 false로 변경됨)
    {
        "id": "persona id 값",
        "user": "user id 값",
        "username" : "로그인할때 사용되는 사용자 아이디",
        "profile": "profile id 값",
        "name": "persona 1 이름",
        "category": "persona 1 카테고리",
        "image": "persona 1 이미지",
        "openpublic": false
    }
#### 결과(비공개->공개 전환 시 openpublic이 false에서 true로 변경됨)
    {
        "id": "persona id 값",
        "user": "user id 값",
        "username" : "로그인할때 사용되는 사용자 아이디",
        "profile": "profile id 값",
        "name": "persona 1 이름",
        "category": "persona 1 카테고리",
        "image": "persona 1 이미지",
        "openpublic": true
    }

### 나의 프로필과 페르소나 한번에 조회하기
### 127.0.0.1:8000/mypage/profile_persona - GET 메소드 사용
#### 결과
    {
        "id": "해당 프로필 id 값(정수)",
        "user": "해당 유저의 id 값(정수)",
        "username" : "로그인할때 사용되는 사용자 아이디",
        "fullname": "프로필 성명",
        "memo": "프로필 한줄 소개",
        "color": "색상",
        "color_hex" : "색상 hex값",
        "image": "이미지",
        "followings": [],
        "personas": [
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            },
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            }
        ],
        "persona_count": "해당 유저가 가지고 있는 페르소나 개수(정수)"
    }

### 다른 유저의 프로필과 페르소나 한번에 조회하기
### 127.0.0.1:8000/mypage/profile_persona/<int:user_id> - GET 메소드 사용
#### 결과
    {
        "id": "해당 프로필 id 값(정수)",
        "user": "해당 유저의 id 값(정수)",
        "username" : "로그인할때 사용되는 사용자 아이디",
        "fullname": "프로필 성명",
        "memo": "프로필 한줄 소개",
        "color": "색상",
        "color_hex" : "색상 hex값",
        "image": "이미지",
        "followings": [],
        "personas": [
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            },
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            }
        ],
        "persona_count": "해당 유저가 가지고 있는 페르소나 개수(정수)"
    }

### 추천 프로필 조회(최대 5개까지 랜덤, 그 이하의 유저만 존재하면 랜덤 순서로 조회)
### 127.0.0.1:8000/mypage/random_profile/ - GET 메소드 사용
#### 결과
    [
    {
        "id": "해당 프로필 id 값(정수)",
        "user": "해당 유저의 id 값(정수)",
        "username" : "로그인할때 사용되는 사용자 아이디",
        "fullname": "프로필 성명",
        "memo": "프로필 한줄 소개",
        "color": "색상",
        "color_hex" : "색상 hex값",
        "image": "이미지",
        "followings": [],
        "personas": [
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            },
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            }
        ],
        "persona_count": "해당 유저가 가지고 있는 페르소나 개수(정수)"
    },
    {
        "id": "해당 프로필 id 값(정수)",
        "user": "해당 유저의 id 값(정수)",
        "fullname": "프로필 성명",
        "memo": "프로필 한줄 소개",
        "color": "색상",
        "color_hex" : "색상 hex값",
        "image": "이미지",
        "followings": [],
        "personas": [
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            },
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            }
        ],
        "persona_count": "해당 유저가 가지고 있는 페르소나 개수(정수)"
    },
    {
        "id": "해당 프로필 id 값(정수)",
        "user": "해당 유저의 id 값(정수)",
        "username" : "로그인할때 사용되는 사용자 아이디",
        "fullname": "프로필 성명",
        "memo": "프로필 한줄 소개",
        "color": "색상",
        "color_hex" : "색상 hex값",
        "image": "이미지",
        "followings": [],
        "personas": [
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            },
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            }
        ],
        "persona_count": "해당 유저가 가지고 있는 페르소나 개수(정수)"
    },
    {
        "id": "해당 프로필 id 값(정수)",
        "user": "해당 유저의 id 값(정수)",
        "username" : "로그인할때 사용되는 사용자 아이디",
        "fullname": "프로필 성명",
        "memo": "프로필 한줄 소개",
        "color": "색상",
        "color_hex" : "색상 hex값",
        "image": "이미지",
        "followings": [],
        "personas": [
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            },
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            }
        ],
        "persona_count": "해당 유저가 가지고 있는 페르소나 개수(정수)"
    },
    {
        "id": "해당 프로필 id 값(정수)",
        "user": "해당 유저의 id 값(정수)",
        "username" : "로그인할때 사용되는 사용자 아이디",
        "fullname": "프로필 성명",
        "memo": "프로필 한줄 소개",
        "color": "색상",
        "color_hex" : "색상 hex값",
        "image": "이미지",
        "followings": [],
        "personas": [
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            },
            {
                "id": "해당 페르소나의 id값(정수)",
                "name": "해당 페르소나 이름",
                "category": "해당 페르소나 카테고리",
                "image": "이미지",
                "openpublic": "공개여부(true/false)",
                "user": "해당 페르소나의 유저의 id값(정수)",
                "username" : "로그인할때 사용되는 사용자 아이디",
                "profile": "해당 페르소나의 유저의 프로필 id 값(정수)"
            }
        ],
        "persona_count": "해당 유저가 가지고 있는 페르소나 개수(정수)"
    }
]


### 게시물

### 1. 모든 게시물 가져 오기 및 사진 게시물 작성
### 1-1. 모든 게시물 가져 오기
### 127.0.0.1:8000/post/ - GET 메소드 사용
#### 결과
#### 사진을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": "이미지1(필수값)",
            "image2": "이미지2",
            "image3": "이미지3",
            "image4": "이미지4",
            "image5": "이미지5",
            "image6": "이미지6",
            "image7": "이미지7",
            "image8": "이미지8",
            "image9": "이미지9",
            "image10": "이미지10",
            "video": null,
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 영상을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": null,
            "image2": null,
            "image3": null,
            "image4": null,
            "image5": null,
            "image6": null,
            "image7": null,
            "image8": null,
            "image9": null,
            "image10": null,
            "video": "영상",
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
    
### 1-2. 사진 게시물 작성
### 127.0.0.1:8000/post/ - POST 메소드 사용
    {
        "title": "제목",
        "content": "내용",
        "persona": "사용할 페르소나의 id 값(정수)"
        "image1": "이미지1(필수값)"
    }
   
### 2. 사진을 첨부한 게시물 중 특정 게시물 가져 오기 / 수정 / 삭제
### 2-1. 사진을 첨부한 게시물 중 특정 게시물 가져 오기
### 127.0.0.1:8000/post/<int:post_pk>/ - GET 메소드 사용
#### 결과
    {
        "id": "해당 게시물 id 값(정수)",
        "writer": "해당 게시물 작성자 id 값(정수)",
        "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
        "title": "게시물 제목",
        "content": "게시물 내용",
        "image1": "이미지1(필수값)",
        "image2": "이미지2",
        "image3": "이미지3",
        "image4": "이미지4",
        "image5": "이미지5",
        "image6": "이미지6",
        "image7": "이미지7",
        "image8": "이미지8",
        "image9": "이미지9",
        "image10": "이미지10",
        "like_num": "해당 게시물 좋아요 수(정수)",
        "comment_set": [],
        "comment_count": "해당 게시물 댓글 수(정수)",
        "created_at": "작성 일자",
        "updated_at": "수정 일자"
        "username" : "로그인할 때 사용되는 사용자 아이디",
        "fullname": "프로필 성명",
    }
    
### 2-2. 사진을 첨부한 게시물 중 특정 게시물 수정하기
### 127.0.0.1:8000/post/<int:post_pk>/ - PATCH 메소드 사용
    {
        "title": "제목",
        "content": "내용",
        "persona": "사용할 페르소나의 id 값(정수)"
        "image1": "이미지1"
    }
    
### 2-3. 사진을 첨부한 게시물 중 특정 게시물 삭제하기
### 127.0.0.1:8000/post/<int:post_pk>/ - DELETE 메소드 사용
#### 결과
    {
        "post": "삭제된 게시물 id 값(정수)"
    }

### 3. 영상을 첨부한 게시물 중 특정 게시물 작성하기
### 127.0.0.1:8000/post/video_post_create/ - POST 메소드 사용
    {
        "title": "제목",
        "content": "내용",
        "persona": "사용할 페르소나의 id 값(정수)"
        "video": "영상"
    }

### 4. 영상을 첨부한 게시물 중 특정 게시물 가져 오기 / 수정 / 삭제
### 4-1. 영상을 첨부한 게시물 중 특정 게시물 가져 오기
### 127.0.0.1:8000/post/<int:post_pk>/video_post_update_delete/ - GET 메소드 사용
#### 결과
    {
        "id": "해당 게시물 id 값(정수)",
        "writer": "해당 게시물 작성자 id 값(정수)",
        "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
        "title": "게시물 제목",
        "content": "게시물 내용",
        "video": "영상",
        "like_num": "해당 게시물 좋아요 수(정수)",
        "comment_set": [],
        "comment_count": "해당 게시물 댓글 수(정수)",
        "created_at": "작성 일자",
        "updated_at": "수정 일자"
        "username" : "로그인할 때 사용되는 사용자 아이디",
        "fullname": "프로필 성명",
    },
    
### 4-2. 영상을 첨부한 게시물 중 특정 게시물 수정하기
### 127.0.0.1:8000/post/<int:post_pk>/video_post_update_delete/ - PATCH 메소드 사용
    {
        "title": "제목",
        "content": "내용",
        "persona": "사용할 페르소나의 id 값(정수)"
        "video": "영상"
    }

### 4-3. 영상을 첨부한 게시물 중 특정 게시물 삭제하기
### 127.0.0.1:8000/post/<int:post_pk>/video_post_update_delete/ - DELETE 메소드 사용
#### 결과
    {
        "post": "삭제된 게시물 id 값(정수)"
    }

### 0817 추가
### 1. 내가 팔로우한 유저의 게시글만 조회가능한 api
### 127.0.0.1:8000/post/myfollow/ - GET 메소드 사용
#### 결과
#### 사진을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": "이미지1(필수값)",
            "image2": "이미지2",
            "image3": "이미지3",
            "image4": "이미지4",
            "image5": "이미지5",
            "image6": "이미지6",
            "image7": "이미지7",
            "image8": "이미지8",
            "image9": "이미지9",
            "image10": "이미지10",
            "video": null,
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 영상을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": null,
            "image2": null,
            "image3": null,
            "image4": null,
            "image5": null,
            "image6": null,
            "image7": null,
            "image8": null,
            "image9": null,
            "image10": null,
            "video": "영상",
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 게시물이 없다면
    []
    
### 2. 내가 작성한 게시글 목록을 조회하는 api
### 127.0.0.1:8000/post/mypost/ - GET 메소드 사용
#### 결과
#### 사진을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": "이미지1(필수값)",
            "image2": "이미지2",
            "image3": "이미지3",
            "image4": "이미지4",
            "image5": "이미지5",
            "image6": "이미지6",
            "image7": "이미지7",
            "image8": "이미지8",
            "image9": "이미지9",
            "image10": "이미지10",
            "video": null,
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 영상을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": null,
            "image2": null,
            "image3": null,
            "image4": null,
            "image5": null,
            "image6": null,
            "image7": null,
            "image8": null,
            "image9": null,
            "image10": null,
            "video": "영상",
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 게시물이 없다면
    []
    
### 3. 나의 특정 페르소나가 작성한 게시글 목록을 조회하는 api
### 127.0.0.1:8000/post/mypost/<int:persona_id>/ - GET 메소드 사용
#### 결과
#### 사진을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": "이미지1(필수값)",
            "image2": "이미지2",
            "image3": "이미지3",
            "image4": "이미지4",
            "image5": "이미지5",
            "image6": "이미지6",
            "image7": "이미지7",
            "image8": "이미지8",
            "image9": "이미지9",
            "image10": "이미지10",
            "video": null,
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 영상을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": null,
            "image2": null,
            "image3": null,
            "image4": null,
            "image5": null,
            "image6": null,
            "image7": null,
            "image8": null,
            "image9": null,
            "image10": null,
            "video": "영상",
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 게시물이 없다면
    []

### 4. 내가 아닌 특정 유저가 작성한 게시글만 조회하는 api
### 127.0.0.1:8000/post/user_post/<int:user_id>/ - GET 메소드 사용
#### 결과
#### 사진을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": "이미지1(필수값)",
            "image2": "이미지2",
            "image3": "이미지3",
            "image4": "이미지4",
            "image5": "이미지5",
            "image6": "이미지6",
            "image7": "이미지7",
            "image8": "이미지8",
            "image9": "이미지9",
            "image10": "이미지10",
            "video": null,
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 영상을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": null,
            "image2": null,
            "image3": null,
            "image4": null,
            "image5": null,
            "image6": null,
            "image7": null,
            "image8": null,
            "image9": null,
            "image10": null,
            "video": "영상",
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 게시물이 없다면
    []
    
### 5. 내가 아닌 특정 유저의 특정 페르소나가 작성한 게시글만 조회하는 api
### 127.0.0.1:8000/post/user_post/<int:user_id>/<int:persona_id>/ - GET 메소드 사용
#### 결과
#### 사진을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": "이미지1(필수값)",
            "image2": "이미지2",
            "image3": "이미지3",
            "image4": "이미지4",
            "image5": "이미지5",
            "image6": "이미지6",
            "image7": "이미지7",
            "image8": "이미지8",
            "image9": "이미지9",
            "image10": "이미지10",
            "video": null,
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 영상을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": null,
            "image2": null,
            "image3": null,
            "image4": null,
            "image5": null,
            "image6": null,
            "image7": null,
            "image8": null,
            "image9": null,
            "image10": null,
            "video": "영상",
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 게시물이 없다면
    []
   
### 6. 내가 소식받기한 페르소나의 게시글만 조회하는 api
### 127.0.0.1:8000/post/follow_persona/ - GET 메소드 사용
#### 결과
#### 사진을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": "이미지1(필수값)",
            "image2": "이미지2",
            "image3": "이미지3",
            "image4": "이미지4",
            "image5": "이미지5",
            "image6": "이미지6",
            "image7": "이미지7",
            "image8": "이미지8",
            "image9": "이미지9",
            "image10": "이미지10",
            "video": null,
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 영상을 업로드한 경우
    [
        {
            "id": "해당 게시물 id 값(정수)",
            "writer": "해당 게시물 작성자 id 값(정수)",
            "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
            "title": "게시물 제목",
            "content": "게시물 내용",
            "image1": null,
            "image2": null,
            "image3": null,
            "image4": null,
            "image5": null,
            "image6": null,
            "image7": null,
            "image8": null,
            "image9": null,
            "image10": null,
            "video": "영상",
            "like_num": "해당 게시물 좋아요 수(정수)",
            "comment_set": [],
            "comment_count": "해당 게시물 댓글 수(정수)",
            "created_at": "작성 일자",
            "updated_at": "수정 일자"
            "username" : "로그인할 때 사용되는 사용자 아이디",
            "fullname": "프로필 성명",
        },
    ]
#### 게시물이 없다면
    []

### 댓글

### 1. 특정 게시물의 댓글 보기 / 작성하기
### 1-1. 특정 게시물의 댓글 보기
### 127.0.0.1:8000/post/<int:post_id>/comments - GET 메소드 사용
#### 결과
    [
        {
            "id": "해당 댓글 id 값(정수)",
            "post": "해당 게시물 id 값(정수)",
            "writer": "해당 유저의 id 값(정수)",
            "content": "댓글 내용",
            "created_at": "생성 일자",
            "updated_at": "수정 일자"
        }
    ]
    
### 1-2. 특정 게시물의 댓글 작성하기
### 127.0.0.1:8000/post/<int:post_id>/comments - POST 메소드 사용
    {
        "content": "댓글 내용"
    }
    
### 2. 특정 게시물의 특정 댓글 보기 / 수정 / 삭제
### 2-1. 특정 게시물의 특정 댓글 보기
### 127.0.0.1:8000/post/<int:post_pk>/comments/<int:comment_pk> - GET 메소드 사용
#### 결과
    {
        "id": "해당 댓글 id 값(정수)",
        "post": "해당 댓글의 게시물 id 값(정수)",
        "writer": "해당 유저의 id 값(정수)",
        "content": "댓글 내용",
        "created_at": "생성 일자",
        "updated_at": "수정 일자"
    }
    
### 2-2. 특정 게시물의 특정 댓글 수정하기
### 127.0.0.1:8000/post/<int:post_pk>/comments/<int:comment_pk> - PATCH 메소드 사용
    {
        "content" : "댓글 내용"
    }
    
### 2-3. 특정 게시물의 특정 댓글 삭제하기
### 127.0.0.1:8000/post/<int:post_pk>/comments/<int:comment_pk> - DELETE 메소드 사용
#### 결과
    {
        "comment": "삭제된 댓글 id 값(정수)"
    }


### 유저 검색
### 127.0.0.1:8000/search/ - POST 메소드 사용
#### 입력
    {
        "word":"검색 입력값"
    }

#### 결과
    [
        {
            "id": "결과1 유저의 프로필 id값(정수)",
            "userid": "결과1 유저의 id값(정수)",
            "username": "결과1 유저의 계정 아이디(username)",
            "fullname": "결과1 유저의 프로필 이름",
            "image": "결과1 유저의 프로필 이미지"
        },
        {
            "id": "결과2 유저의 프로필 id값(정수)",
            "userid": "결과2 유저의 id값(정수)",
            "username": "결과2 유저의 계정 아이디(username)",
            "fullname": "결과2 유저의 프로필 이름",
            "image": "결과2 유저의 프로필 이미지"
        },
        {
            "id": "결과2 유저의 프로필 id값(정수)",
            "userid": "결과2 유저의 id값(정수)",
            "username": "결과2 유저의 계정 아이디(username)",
            "fullname": "결과2 유저의 프로필 이름",
            "image": "결과2 유저의 프로필 이미지"
        }
    ]

## 나의 검색 기록
### 나의 검색 기록 조회
### 127.0.0.1:8000/search/history - GET 메소드 사용
#### 결과
    [
        {
            "id": "해당 히스토리 id 값(정수)",
            "user": "나의 유저 id 값(정수)",
            "userid": "검색 결과로 나왔던 유저1 id(정수)",
            "username": "검색 결과로 나왔던 유저1의 계정 아이디",
            "resultprofile": "검색 결과로 나왔던 유저1 프로필 id(정수)",
            "fullname": "검색 결과로 나왔던 유저1의 프로필명",
            "image": "검색 결과로 나왔던 유저1의 프로필 사진",
        },
        {
            "id": "해당 히스토리 id 값(정수)",
            "user": "나의 유저 id 값(정수)",
            "userid": "검색 결과로 나왔던 유저2 id(정수)",
            "username": "검색 결과로 나왔던 유저2의 계정 아이디",
            "resultprofile": "검색 결과로 나왔던 유저2 프로필 id(정수)",
            "fullname": "검색 결과로 나왔던 유저2의 프로필명",
            "image": "검색 결과로 나왔던 유저2의 프로필 사진",
        },
        {
            "id": "해당 히스토리 id 값(정수)",
            "user": "나의 유저 id 값(정수)",
            "userid": "검색 결과로 나왔던 유저3 id(정수)",
            "username": "검색 결과로 나왔던 유저3의 계정 아이디",
            "resultprofile": "검색 결과로 나왔던 유저3 프로필 id(정수)",
            "fullname": "검색 결과로 나왔던 유저3의 프로필명",
            "image": "검색 결과로 나왔던 유저3의 프로필 사진",
        }
    ]

### 나의 검색 기록 생성
### 127.0.0.1:8000/search/history - POST 메소드 사용
#### 입력
    {
        "resultprofile": "검색 결과로 나왔던 유저1 프로필 id(정수)",
        "image": "검색 결과로 나왔던 유저1의 프로필 사진(문자열)",
    }

### 나의 검색 기록 삭제
### 127.0.0.1:8000/search/history/<int:history_id> - DELETE 메소드 사용
#### 결과
    {
        "history_id":"삭제된 history id 값(정수)"
    }
    
### 좋아요

### 1. 해당 게시물 좋아요 수 보기
### 127.0.0.1:8000/post/<int:post_pk>/post_likes - GET 메소드 사용
#### 결과
    {
        "id": "해당 게시물 id 값(정수)",
        "like_num": "해당 게시물 좋아요 수(정수)"
    }
    
### 2. 해당 게시물 속 좋아요 누르기 / 취소하기
### 127.0.0.1:8000/post/<int:post_pk>/send_like - PATCH 메소드 사용
### PATCH 버튼을 눌렀을 때(입력값 없이 PATCH 메소드 보내기)
#### 결과
#### 좋아요 버튼을 누르는 유저가 해당 게시물에 좋아요를 누른 적이 없는 경우(좋아요 수 추가 = 좋아요 하기)
    {
        "id": "해당 게시물 id 값(정수),
        "writer": "해당 게시물 작성자의 id 값(정수)",
        "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
        "title": "제목",
        "content": "내용",
        "like_num": "기존의 좋아요 수 + 1(정수)",
        "comment_set": [],
        "comment_count": "댓글 개수(정수)",
        "created_at": "작성 일자",
        "updated_at": "수정 일자"
    }
#### 좋아요 버튼을 누르는 유저가 해당 게시물에 좋아요를 누른 적이 있는 경우(좋아요 수 감소 = 좋아요 취소하기)
    {
        "id": "해당 게시물 id 값(정수),
        "writer": "해당 게시물 작성자의 id 값(정수)",
        "persona": "해당 게시물 작성자의 페르소나 id 값(정수)",
        "title": "제목",
        "content": "내용",
        "like_num": "기존의 좋아요 수 - 1(정수)",
        "comment_set": [],
        "comment_count": "댓글 개수(정수)",
        "created_at": "작성 일자",
        "updated_at": "수정 일자"
    }


## 팔로우/팔로잉
### 내가 팔로우한 사용자 목록
### 127.0.0.1:8000/mypage/following_list/ - GET 메소드 사용
#### 결과
    {
        "followings": [
            "내가 팔로우한 유저1의 id값(정수)",
            "내가 팔로우한 유저2의 id값(정수)"
        ],
        "followingnum": "내가 팔로우한 유저 수(정수)",
        "followernum": "나를 팔로잉하고 있는 팔로워수(정수)",
        "subfollowings": [
            "내가 팔로우한 유저1의 페르소나1 id값(정수)",
            "내가 팔로우한 유저1의 페르소나2 id값(정수)",
            "내가 팔로우한 유저2의 페르소나1 id값(정수)",
            "내가 팔로우한 유저2의 페르소나2 id값(정수)",
            "내가 팔로우한 유저2의 페르소나3 id값(정수)"
        ]
    }

### 다른 사용자가 팔로우한 사용자 목록
### 127.0.0.1:8000/mypage/<int:user_id>/following_list/ - GET 메소드 사용
#### 결과
    {
        "followings": [
            "유저가 팔로우한 사용자1 user.profile.id값(정수)",
            "유저가 팔로우한 사용자2 user.profile.id값(정수)"
        ],
        "followingnum":"유저가 팔료우한 유저 수(정수)",
        "followernum":"유저를 팔로잉하고 있는 팔로워수(정수)",
         "subfollowings": [
            "유저가 팔로우한 유저1의 페르소나1 id값(정수)",
            "유저가 팔로우한 유저1의 페르소나2 id값(정수)",
            "유저가 팔로우한 유저2의 페르소나1 id값(정수)",
            "유저가 팔로우한 유저2의 페르소나2 id값(정수)",
            "유저가 팔로우한 유저2의 페르소나3 id값(정수)"
        ]
    }

### 다른 사용자 팔로우/언팔로우 하기
### 127.0.0.1:8000/mypage/follow/<int:user_id>/ - POST 메소드 사용
#### 입력 및 결과
    입력은 아무것도 넣지 않고 보내고, 보낸 후 결과
    {
        "followings": [
            "내가 팔로우한 유저1의 id값(정수)",
            "내가 팔로우한 유저2의 id값(정수)"
        ],
        "followingnum": "내가 팔로우한 유저 수(정수)",
        "followernum": "나를 팔로잉하고 있는 팔로워수(정수)",
        "subfollowings": [
            "내가 팔로우한 유저1의 페르소나1 id값(정수)",
            "내가 팔로우한 유저1의 페르소나2 id값(정수)",
            "내가 팔로우한 유저2의 페르소나1 id값(정수)",
            "내가 팔로우한 유저2의 페르소나2 id값(정수)",
            "내가 팔로우한 유저2의 페르소나3 id값(정수)"
        ]
    }
    기존에 팔로우 했던 사용자 id를 넣고 POST 보내면 언팔로우,
    팔로우 하지 않고 있던 사용자 id를 넣고 POST 보내면 팔로우

### 내가 다른 특정 사용자를 팔로우/언팔로우 하고 있는지 확인
### 127.0.0.1:8000/mypage/follow/<int:user_id>/ - GET 메소드 사용
#### 팔로우 중 결과
    {
        "followState": "팔로잉",
        "text": "유저를 팔로우 중입니다."
    }
#### 언팔로우 중 결과
    {
        "followState": "팔로우",
        "text": "유저를 언팔로우 중입니다."
    }

### 다른 사용자 페르소나 소식받기 설정 기능
### 127.0.0.1:8000/mypage/persona_follow/<int:persona_id>/ - POST 메소드 사용
#### 입력 및 결과
    예시 : 유저2의 페르소나2의 id값이 4라면 127.0.0.1:8000/mypage/persona_follow/4/
    입력은 아무것도 넣지 않고 보내고, 보낸 후 결과
    {
        "followings": [
            "내가 팔로우한 유저1의 id값(정수)",
            "내가 팔로우한 유저2의 id값(정수)"
        ],
        "followingnum": "내가 팔로우한 유저 수(정수)",
        "followernum": "나를 팔로잉하고 있는 팔로워수(정수)",
        "subfollowings": [
            "내가 팔로우한 유저1의 페르소나1 id값(정수)",
            "내가 팔로우한 유저1의 페르소나2 id값(정수)",
            "내가 팔로우한 유저2의 페르소나1 id값(정수)",
            "내가 팔로우한 유저2의 페르소나3 id값(정수)"
        ]
    }
    기존에 소식을 받던 페르소나 id를 넣고 POST 보내면 소식 끊기,
    소식받기를 안하던 페르소나 id를 넣고 POST 보내면 소식 받기
#### 만약 소식 받기를 누른 페르소나의 사용자를 팔로우 하고 있지 않는 경우는 소식받기가 안되며 결과로 밑에 json으로 나옴
    {"warning":"페르소나의 사용자를 팔로우해야합니다."}

## 알림 목록
### 127.0.0.1:8000/mypage/notice/ - GET 메소드 사용
#### 좋아요 알림
    {
        "id": "해당 알림의 id값(정수)",
        "created_at": "알림이 생성된 날짜/ 시간",
        "user":"알림을 받는 유저(나, 본인) id값(정수)",
        "userfrom":"내 게시물을 좋아요 누른사람 계정 아이디",
        "userto":"내 게시물의 페르소나 이름"
        "text":"님의 게시물을 좋아합니다.",
        "content":null
    }
#### 팔로우 알림
    {
        "id": "해당 알림의 id값(정수)",
        "created_at": "알림이 생성된 날짜/ 시간",
        "user":"알림을 받는 유저(나, 본인) id값(정수)",
        "userfrom":"나를 팔로우 시작한 사람 계정 아이디",
        "userto":"'회원'이라는 텍스트로 출력"
        "text":"님을 팔로우하기 시작했습니다.",
        "content":null
    }
#### 댓글 알림
    {
        "id": "해당 알림의 id값(정수)",
        "created_at": "알림이 생성된 날짜/ 시간",
        "user":"알림을 받는 유저(나, 본인) id값(정수)",
        "userfrom":"내 게시글에 댓글을 단 사람 계정 아이디",
        "userto":"댓글달린 게시글의 페르소나명"
        "text":"님의 게시글에 댓글을 남겼습니다.",
        "content":"댓글 내용"
    }
