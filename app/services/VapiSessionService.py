import requests
from datetime import datetime
import os
import json

'''
Service managing the VAPI session for requirements clarification
'''

# VAPI Configuration
VAPI_API_KEY = os.getenv("VAPI_API_KEY")
VAPI_BASE_URL = "https://api.vapi.ai"

def create_vapi_clarification_assistant(problem):
    """
    Create a VAPI assistant for requirements clarification
    Returns assistant information with ID
    """
    url = f"{VAPI_BASE_URL}/assistant"
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    problem_details = problem.details
    
    # Extract problem information for the AI
    problem_name = problem.name
    problem_description = problem_details.get("description")
    functional_requirements = problem_details.get("functional_requirements")
    non_functional_requirements = problem_details.get("non_functional_requirements")
    assumptions = problem_details.get("assumptions")
    
    payload = {
        "model": {
            "provider": "openai",
            "model": "gpt-4o-mini",
            "temperature": 0.7,
            "maxTokens": 1000,
            "messages": [
                {
                    "role": "assistant",
                    "content": f"""
                        You are an experienced software engineer conducting the Clarification Phase of a technical system design interview.
                        
                        The problem to be solved is: {problem_name}
                        The problem description is: {problem_description}
                        The functional requirements are: {functional_requirements}
                        The non-functional requirements are: {non_functional_requirements}
                        The assumptions the user can make are: {assumptions}. Don't give these to the candidate unless they ask for them.
                        
                        Your role is to help the candidate clarify requirements and understand the problem thoroughly before moving on to system design.
   
                        Guidelines:
                        1. Start by reading out the problem description, functional requirements, non-functional requirements.
                        2. Ask the candidate to clarify requirements, problem scope, constraints and assumptions using the provided context. When appropriate, assist with rough quantitative estimates (e.g., throughput, storage, latency) related to non-functional requirements.
                        3. Stay strictly on requirement clarification; do not discuss design, technology, or implementation details. Keep explanations abstract and tied only to requirements. If the candidate mentions a solution, acknowledge it briefly and redirect back to the underlying requirement it addresses.
                        4. Keep responses concise and focused. Answer only what’s asked—no extra hints or implementation details unless requested.
                        5. Assert responses confidently to clarification questions, using standard engineering assumptions and domain knowledge. Avoid seeking approval or confirmation from the user.
                        6. When a question has multiple reasonable answers not specified in context, briefly mention both options without explaining trade-offs and note that each is valid depending on design priorities. Do **not** ask the user to choose.
                        7. Avoid repeating the candidate’s question. If multiple interpretations/answers exist, acknowledge them briefly and recommend the most practical option based on typical design principles.
                        8. Maintain a professional and conversational tone. Be supportive but let the candidate drive the depth of discussion.
                    

                    """
                },
                {
                    "role": "user",
                    "content": f"""
                        You are a software engineering candidate participating in a technical system design interview.

                        Their goal during this clarification phase is to ensure you have a complete and accurate understanding of the problem before proposing a solution.

                        They will:
                        1. Carefully listen to the problem description, functional requirements, non-functional requirements, provided by the interviewer.
                        2. Drive the conversation by asking clarifying questions about requirements, assumptions you can make, edge cases, constraints, and any ambiguities in the problem statement.
                        3. Seek confirmation about what is in scope and out of scope for your solution.
                        4. Don't seek tutoring or or validation from the interviewer.
                        5. When appropriate, attempt rough calculations or estimations (e.g., throughput, storage capacity, data volume, latency) to validate the non-functional requirements and reason about system scale.
                        6. Restate your understanding of the problem in your own words to verify alignment.
                        7. Avoid discussing or proposing design solutions at this stage—focus entirely on requirement gathering and problem comprehension.

                        By the end of this phase, your objective is to confirm that all functional and non-functional requirements are fully understood and validated before moving on to system design.
                    """
                    }

            ]
        }
    }
    
    try:
        resp = requests.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        assistant_response = resp.json()
        assistant_id = assistant_response.get("id")
        
        print(f"Created VAPI assistant: {assistant_response.get('id')}")
        return assistant_id
        
    except requests.exceptions.RequestException as e:
        print(f"VAPI Assistant Creation Error: {e}")
        return None


def create_vapi_clarification_session(assistant_id: str):
    """
    Create a VAPI call using an existing assistant
    Returns VAPI call information
    """
    url = f"{VAPI_BASE_URL}/call"
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "assistantId": assistant_id,
        "session": {
            "mode": "webrtc",   # important: browser audio, not phone
            "type": "outbound"  # but we won't actually dial a number
        }
    }
    
    try:
        resp = requests.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        vapi_response = resp.json()

        print(f"Created VAPI call: {vapi_response.get('id')}")
        return vapi_response
        
    except requests.exceptions.RequestException as e:
        print(f"VAPI Call Creation Error: {e}")
        return None


def end_vapi_clarification_session(vapi_session_id: str):
    """
    End the VAPI clarification session and save requirements to session state
    This corresponds to step 6 in the flow
    """


    if not vapi_session_id:
        return False
    
    
    # End the VAPI session
    try:
        url = f"{VAPI_BASE_URL}/call/{vapi_session_id}/end"
        headers = {
            "Authorization": f"Bearer {VAPI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        resp = requests.post(url, headers=headers)
        resp.raise_for_status()
        
        # Note: Session updates are handled by the calling service
        
        print(f"Ended VAPI clarification session: {vapi_session_id}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Error ending VAPI session: {e}")
        return False