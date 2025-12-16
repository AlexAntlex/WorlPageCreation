from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api_v1.crud import profiles as c_profiles
from app.api_v1.schemas.profile_schema import (
    ProfileResponse,
    ProfileUpdate,
    ProfileBase,
    ProfileCreate,
)
from app.core import db_helper
from app.api_v1.crud import profiles
from app.api_v1.dependecies import profile_by_id
from app.structure.models.profile_model import Profile

router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.get("/", response_model=list[ProfileResponse])
async def get_profiles(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await profiles.get_profiles(session=session)


@router.post(
    "/add_profile/", response_model=ProfileCreate, status_code=status.HTTP_201_CREATED
)
async def create_profile(
    profile_create: ProfileCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await profiles.create_profile(session=session, profile_create=profile_create)


@router.get("/{profile_id}/", response_model=ProfileBase)
async def get_one_profile(
    profile: Profile = Depends(profile_by_id),
):
    return profile


@router.patch("/update/{profile_id}/")
async def update_profile(
    profile_update: ProfileUpdate,
    profile: Profile = Depends(profile_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await c_profiles.update_profile(
        session=session,
        profile=profile,
        profile_update=profile_update,
    )


@router.delete("/delete/{profile_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(
    profile: Profile = Depends(profile_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    return await c_profiles.delete_profile(session=session, profile=profile)
