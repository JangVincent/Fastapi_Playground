# ===== Python / Environment =====

# 활성화된 가상환경에 맞는 Python 실행
PYTHON=.venv/bin/python
UV=.venv/bin/uv
UVX=uvx   # uvx는 글로벌 PATH에서 실행 가능

# ===== Commands =====

# 가상환경 생성
venv:
	uv venv

# 패키지 설치
install:
	uv sync

# FastAPI development server
dev:
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# FastAPI production (예: gunicorn + uvicorn worker)
prod:
	gunicorn src.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# 코드 포맷팅
format:
	uvx ruff check --fix .

# 코드 검사
lint:
	uvx ruff check .

# 테스트 (pytest 사용 시)
test:
	uvx pytest -q

# 환경 변수 출력
env:
	.venv/bin/python -c "from src.config import settings; print(settings.model_dump())"

create-module:
	uv run scripts/create_module.py $(path)

db-migrate:
	alembic revision --autogenerate -m "$(msg)"

db-upgrade:
	alembic upgrade head

db-downgrade:
	alembic downgrade -1

db-reset:
	alembic downgrade base
