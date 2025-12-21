from fastapi import APIRouter

from .views.project import router as project_views
from .views.post import router as post_views
from .views.comment import router as comment_views

router = APIRouter()
router.include_router(project_views)
router.include_router(post_views)
router.include_router(comment_views)
