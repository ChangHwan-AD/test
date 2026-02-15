# CLAUDE.md

This file provides guidance for AI assistants (including Claude) working in this repository.

## Repository Overview

- **Repository**: ChangHwan-AD/test
- **Description**: Flask 기반 웹 애플리케이션 — 오늘 날짜와 시간을 표시하는 단일 페이지 앱.
- **Language**: Python
- **Framework**: Flask

## Project Structure

```
/
├── app.py                 # Flask 애플리케이션 엔트리포인트
├── templates/
│   └── index.html         # 메인 페이지 템플릿 (Jinja2)
├── requirements.txt       # Python 의존성
├── CLAUDE.md              # AI 어시스턴트 가이드 (이 파일)
└── .git/
```

## Development Setup

```sh
pip install -r requirements.txt
```

## Build and Run

```sh
python app.py
```

서버가 `http://127.0.0.1:5000` 에서 실행됩니다 (debug 모드 활성화).

## Testing

테스트 프레임워크가 아직 구성되어 있지 않습니다. 추가 시 이 섹션을 업데이트하세요.

## Linting and Formatting

린터/포매터가 아직 구성되어 있지 않습니다. 추가 시 이 섹션을 업데이트하세요.

## Key Conventions

- 커밋 메시지는 명확하고 서술적으로 작성합니다.
- 프로젝트 구조나 워크플로에 변경이 있으면 이 `CLAUDE.md` 파일을 함께 업데이트합니다.
- 템플릿은 `templates/` 디렉토리에 Jinja2 형식으로 작성합니다.

## Architecture

- **app.py**: Flask 앱 인스턴스 생성, 라우트 정의, `datetime.now()`로 현재 시각을 가져와 템플릿에 전달.
- **templates/index.html**: Jinja2 템플릿. 서버에서 전달받은 `now` 객체를 `strftime`으로 포매팅하여 날짜와 시간 표시.
