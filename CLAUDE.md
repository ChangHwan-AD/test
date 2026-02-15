# CLAUDE.md

This file provides guidance for AI assistants (including Claude) working in this repository.

## Repository Overview

- **Repository**: ChangHwan-AD/test
- **Description**: Flask 기반 웹 애플리케이션 — EvenTime(시간 표시)과 EvenStock(주식 대시보드) 두 페이지 앱.
- **Language**: Python
- **Framework**: Flask
- **Deployment**: Render (free tier)

## Project Structure

```
/
├── app.py                 # Flask 애플리케이션 엔트리포인트
├── templates/
│   ├── index.html         # EvenTime 페이지 템플릿 (Jinja2)
│   └── stock.html         # EvenStock 페이지 템플릿 (Jinja2)
├── requirements.txt       # Python 의존성 (flask, gunicorn)
├── render.yaml            # Render 배포 설정 (Blueprint)
├── CLAUDE.md              # AI 어시스턴트 가이드 (이 파일)
└── .git/
```

## Development Setup

```sh
pip install -r requirements.txt
```

## Build and Run

로컬 실행:
```sh
python app.py
```
서버가 `http://0.0.0.0:10000` 에서 실행됩니다.

프로덕션 (Render):
```sh
gunicorn app:app
```

## Deployment

Render (https://render.com) 무료 플랜으로 배포합니다.
- `render.yaml` Blueprint 파일로 서비스가 자동 구성됩니다.
- GitHub 저장소 연동 시 push마다 자동 배포됩니다.

## Testing

테스트 프레임워크가 아직 구성되어 있지 않습니다. 추가 시 이 섹션을 업데이트하세요.

## Linting and Formatting

린터/포매터가 아직 구성되어 있지 않습니다. 추가 시 이 섹션을 업데이트하세요.

## Key Conventions

- 커밋 메시지는 명확하고 서술적으로 작성합니다.
- 프로젝트 구조나 워크플로에 변경이 있으면 이 `CLAUDE.md` 파일을 함께 업데이트합니다.
- 템플릿은 `templates/` 디렉토리에 Jinja2 형식으로 작성합니다.

## Architecture

- **app.py**: Flask 앱 인스턴스 생성, 라우트 정의 (`/` → EvenTime, `/stock` → EvenStock).
- **templates/index.html**: EvenTime 페이지. `datetime.now()`를 `strftime`으로 포매팅하여 날짜와 시간 표시.
- **templates/stock.html**: EvenStock 페이지. 주요 주가지수 및 종목 정보를 대시보드 형태로 표시.
- **render.yaml**: Render Blueprint. Python 런타임, 빌드/시작 커맨드, 무료 플랜 설정 정의.
