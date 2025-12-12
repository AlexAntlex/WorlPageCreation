from fastapi import APIRouter

from app.api_v1.views.user import router as user_router

router = APIRouter()
router.include_router(user_router)
