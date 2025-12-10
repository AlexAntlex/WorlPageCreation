from fastapi import APIRouter

from app.api_v1.views.user import router as user_router
from app.api_v1.views.project import router as project_router

router = APIRouter()
router.include_router(user_router)
router.include_router(project_router)
