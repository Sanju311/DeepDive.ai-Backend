from fastapi import APIRouter, Request
from ..services import InterviewSessionService

router = APIRouter(prefix="/interview", tags=["Interview"])

''' INTERVIEW ROUTES '''

@router.post("/start_interview")
async def start_interview(request: Request):
    return await InterviewSessionService.start_interview_session(request)


@router.post("/end_interview")
async def end_interview(request: Request):
    """End the current interview session"""
    return {"message": "Interview session ended successfully"}