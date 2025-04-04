import base64
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class Base64Middleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        # Read original response body
        body = b""
        async for chunk in response.body_iterator:
            body += chunk

        # Encode body with Base64
        encoded_body = base64.b64encode(body).decode("utf-8")

        # Clean up headers to avoid conflict with body length
        headers = dict(response.headers)
        headers.pop("content-length", None)  # Remove Content-Length if present

        # Return a new response with the Base64-encoded body
        return Response(
            content=encoded_body,
            status_code=response.status_code,
            headers=headers,
            media_type="text/plain",  # Changed to plain text for encoded string
        )
