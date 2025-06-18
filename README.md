# 🖼️ Image Upscaler REST API (Flask)

이 프로젝트는 업로드된 이미지를 2배로 업스케일링하여 반환하는 간단한 Flask 기반 웹 애플리케이션입니다.

## 📦 기능

- 브라우저를 통해 이미지 업로드
- 서버에서 업스케일링 처리 (예: `model.predict(image)` 함수 사용)
- 결과 이미지를 브라우저에서 즉시 다운로드

---

## 🚀 실행 방법

### 1. 가상환경 생성 및 활성화 (선택사항)

```bash
python3 -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 2. 필수 라이브러리 설치

```bash
pip install -r requirements.txt
```

> `requirements.txt`가 없다면 직접 설치:
```bash
pip install flask pillow
```

또는 `model.py` 내부에서 사용하는 라이브러리에 따라 추가 설치가 필요할 수 있습니다.

---

### 3. 서버 실행

```bash
python app.py
```

### 4. 웹 브라우저 접속

```url
http://localhost:5001
```

---

## 📂 프로젝트 구조

```
.
├── app.py              # Flask 서버 코드
├── model.py            # predict(image) 함수를 포함한 업스케일링 모델 로직
├── requirements.txt    # 필요한 Python 패키지 목록
└── README.md           # 문서 파일
```

---

## 📸 예시 화면

- `/` : 이미지 업로드 폼
- `/upscale` : 업로드된 이미지 처리 및 업스케일링 후 다운로드 응답

---

## ⚠️ 주의사항

- `model.py`는 사용자 정의 코드입니다. `predict(image)` 함수가 반드시 `PIL.Image`를 입력받고 출력해야 합니다.
- 업스케일링 모델이 없을 경우, 해당 함수에 `image.resize(...)` 등의 임시 구현으로 대체 가능

---

## 📝 License

MIT License
