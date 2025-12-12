from fastapi import APIRouter

from .views.project import router as project_views

router = APIRouter()
router.include_router(project_views, prefix="/project")
