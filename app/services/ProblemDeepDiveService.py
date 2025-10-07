import requests
import os

VAPI_API_KEY = os.getenv("VAPI_API_KEY")


'''
Interview Full Flow

DONE 1. Client hits start interview session endpoint with optional problem id

DONE 2. Server creates a new interview session (redis) and returns the session id and problem details 

DONE 3. Server creates a new vapi session and returns the session id

4. User discusses requirements and gets clarifications from the agent until satisfaction

6. User asynchronously hits end_vapi_session endpoint for the clarification/requirements portion and requirements are saved to session state

7. User starts working on the system design diagram & model diagram purely in the frontend. 

8. Once finished diagrams, Client hits deepdive endpoint with current rubric category

9. Create a new vapi session and provides all context needed for the model
    - interview problem
    - current rubric category 
    - system design diagrams & model diagrams
    - previous interview session data

10. Once finished deepdive, vapi judges the deepdive and saves the feedback to session state and scores the deepdive.

11. current vapi session is ended

12. Repeat steps 8-11 for each rubric category until all categories are covered

13. Client hits end interview session endpoint with session id 

'''



def create_vapi_deepdive_session(rubric_category: str, diagrams: dict):
    url = "https://api.vapi.ai/call"
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "assistant": {
            "model": "gpt-4o-mini",  # cheap for dev
            "voice": "alloy",        # pick any TTS voice
            "instructions": f"""
                You are the interviewer.
                Analyze the candidate's design for the rubric category: {rubric_category}.
                Diagrams: {diagrams}.
                Ask probing questions one at a time until the category is covered.
                At the end, summarize strengths/weaknesses and give a score out of 5.
            """
        },
        "session": {
            "mode": "webrtc",   # important: browser audio, not phone
            "type": "outbound" # but we won’t actually dial a number
        }
    }

    resp = requests.post(url, headers=headers, json=payload)
    return resp.json()
