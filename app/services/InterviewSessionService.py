import requests
import uuid
from datetime import datetime
import redis
import json
import os
from fastapi import Request
from .ProblemService import get_interview_problem
from .VapiSessionService import create_vapi_clarification_assistant

'''
Service managing the state of all interview sessions
'''

async def start_interview_session(request: Request):
    """
    Start a new interview session and create Redis session + VAPI session
    Returns both session_id and vapi_session_info
    """

    try: 
 
        problem_id = "1"
        
        # Generate unique session ID
        session_id = str(uuid.uuid4())
        
        # Get problem details (use default if no problem_id provided)
        if problem_id:
            problem = get_interview_problem(problem_id)

        problem_display_data = {
            "name": problem.name,
            "category": problem.category,
            "difficulty": problem.difficulty,
        }
        
        # Create session state data
        session_state = {
            "session_id": session_id,
            "problem_id": problem_id,
            "problem_display_data": problem_display_data,
            "problem_details": problem.details,
            "start_time": datetime.now().isoformat(),
            "stage": "clarification",
        }
        # Redis connection
        redis_client = redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)

        # Store session in Redis with key pattern: interview:session:{session_id}
        redis_key = f"interview:session:{session_id}"
        redis_client.setex(redis_key, 3600, json.dumps(session_state))  # 1 hour TTL
        
        # Create VAPI assistant first
        assistant_id = create_vapi_clarification_assistant(problem)
        
        if not assistant_id:
            print("Failed to create VAPI assistant")
            return None

        
        # Prepare response data
        response_data = {
            "session_id": session_id,
            "problem_display_data": problem_display_data,
            "vapi_clarification_assistant": assistant_id,
        }
        
        print(f"Created interview session: {session_id}")
        
        return response_data

    except Exception as e:
        print(f"Error creating interview session: {e}")
        return {"success": False, "error": f"{e}"}



# def update_session_data(session_id: str, updates: dict):
#     """Update session data in Redis"""
#     try: 
#         redis_key = f"interview:session:{session_id}"
#         current_data = get_session_data(session_id)
        
#         if current_data:
#             current_data.update(updates)
#             redis_client.setex(redis_key, 3600, json.dumps(current_data))  # 1 hour TTL
#             return True
#         else:
#             print(f"No session data found for session_id: {session_id}")
#             return False
    
#     except Exception as e:
#         print(f"Error updating session data: {e}")
#         return False



# def end_interview_session(session_id: str):
#     """End an interview session"""
#     redis_key = f"interview:session:{session_id}"
#     current_data = redis_service.get(redis_key)
    
#     if current_data:
#         current_data.update({
#             "status": "completed",
#             "end_time": datetime.now().isoformat()
#         })
#         redis_service.set(redis_key, current_data, expire=7200)
#         return True
#     return False



