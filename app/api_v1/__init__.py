from fastapi import APIRouter

from .views.project import router as project_views
from .views.profile import router as profile_router

router = APIRouter()
router.include_router(project_views, prefix="/project")
