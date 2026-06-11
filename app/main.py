from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware


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

app = create_app()