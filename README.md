
# 🖼️ Image Upscaler API (Flask & FastAPI)

이 프로젝트는 업로드된 이미지를 2배로 업스케일링하여 반환하는 웹 애플리케이션입니다.  
두 가지 버전으로 제공됩니다: **Flask** 및 **FastAPI**.

---

## 📦 공통 기능

- 웹 브라우저를 통해 이미지 업로드
- `model.predict(image)` 함수 기반 업스케일링 처리
- 업스케일된 이미지를 JPEG로 자동 다운로드
- REST API 설계 방식 사용

---

# 🧰 버전 1: Flask 기반

## 🚀 실행 방법 (Flask)

### 1. 가상환경 생성 및 활성화 (선택사항)

```bash
python3 -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 2. 라이브러리 설치

```bash
pip install -r requirements.txt
```

> requirements.txt가 없다면 직접 설치:
```bash
pip install flask pillow
```

### 3. 서버 실행

```bash
python app.py
```

### 4. 브라우저 접속

```
http://localhost:5001
```

## 📂 구조 (Flask)

```
.
├── app.py              # Flask 서버 코드
├── model.py            # predict(image) 함수 포함
└── requirements.txt    # 필요한 패키지 목록
```

---

# ⚡ 버전 2: FastAPI 기반

## 🚀 실행 방법 (FastAPI)

### 1. 가상환경 생성 및 활성화 (선택사항)

```bash
python3 -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 2. 라이브러리 설치

```bash
pip install fastapi uvicorn pillow jinja2
```

또는

```bash
pip install -r requirements.txt
```

### 3. 서버 실행

```bash
uvicorn main:app --host 0.0.0.0 --port 5001
```

### 4. 접속

- 로컬 접속: `http://localhost:5001`
- 다른 기기에서 접속: `http://<서버의 IP 주소>:5001`


## 📂 구조 (FastAPI)

```
.
├── main.py             # FastAPI 서버 코드
├── model.py            # predict(image) 함수 포함
└── requirements.txt    # 필요한 패키지 목록
```

## 📌 참고

- `model.py` 파일에서 `PIL.Image`를 입력받고 결과를 반환하는 `predict()` 함수가 정의되어 있어야 합니다.
- 예:
```python
def predict(image: Image.Image) -> Image.Image:
    # 예시 업스케일 처리
    return image.resize((image.width * 2, image.height * 2))
```

---
