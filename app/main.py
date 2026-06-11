from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


def create_app() -> FastAPI:
    # Setup (need improvemenr)
    app = FastAPI(
        title=settings.APP_NAME,
        description="Doc Digitalization API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Error Handling
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
            headers=exc.headers or {},
        )

    # Error Handling
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={"detail": exc.errors()},
        )

app = create_app()