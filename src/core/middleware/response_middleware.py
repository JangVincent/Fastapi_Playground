import http
import json

from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from starlette.middleware.base import BaseHTTPMiddleware


class UnifiedResponseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)

        # 파일 / 스트리밍 응답은 그대로 pass
        if isinstance(response, (FileResponse, StreamingResponse)):
            return response

        content_type = response.headers.get("content-type", "")

        # 기타 바이너리 응답 필터
        if (
            "application/octet-stream" in content_type
            or "application/pdf" in content_type
            or "image/" in content_type
        ):
            return response

        # 기존 Body 읽기
        body = b"".join([chunk async for chunk in response.body_iterator])
        status = response.status_code

        # JSON 파싱
        try:
            data = json.loads(body)
        except Exception:
            data = body.decode("utf-8", errors="ignore")

        # 새 헤더 생성: content-length 제거
        new_headers = {k: v for k, v in response.headers.items() if k.lower() != "content-length"}

        wrapped = {
            "success": status < 400,
            "status": status,
            "message": http.HTTPStatus(status).phrase,
            "optional_message": None,
            "data": data,
        }

        return JSONResponse(
            headers=new_headers,
            status_code=status,
            content=wrapped,
        )
