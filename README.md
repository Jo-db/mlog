# Personal Blog

Flask 기반 개인 블로그 프로젝트

---

## 📌 프로젝트 소개

개발 기록, 공부 내용, 문제 해결 과정을 저장하는 개인 블로그입니다.

---

## 🛠️ 기술 스택

* Python
* Flask
* SQLite
* HTML / CSS / JavaScript

---

## ⚙️ 실행 방법 (Git Bash 기준)

### 1. 저장소 클론

```
git clone https://github.com/아이디/레포이름.git
cd 레포이름
```

---

### 2. 가상환경 생성

```
python -m venv .venv
```

---

### 3. 가상환경 활성화

```
source .venv/Scripts/activate
```

---

### 4. 패키지 설치

```
pip install -r requirements.txt
```

---

### 5. 서버 실행

```
python app.py
```

---

### 6. 접속

```
http://127.0.0.1:5000
```

---

## 📁 폴더 구조

```
personal-blog/
│
├─ app.py
├─ blog.db
├─ requirements.txt
│
├─ templates/
│   └─ index.html
│
└─ static/
    ├─ style.css
    └─ script.js
```

---

## 📌 TODO

* [ ] 글 작성 기능
* [ ] 글 목록 조회
* [ ] 글 수정 / 삭제
* [ ] 태그 기능
* [ ] 검색 기능
