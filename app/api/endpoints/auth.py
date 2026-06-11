from fastapi import APIRouter, Depends

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register():
    # Register
    return 1

@router.post("/login")
async def login():
    # Login
    return 1


@router.post("/refresh")
async def refresh():
    # Referesher
    return 1


@router.get("/me")
async def me():
    return 1