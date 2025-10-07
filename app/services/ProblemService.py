from app.models.models import InterviewProblem
from app.db import session_maker


'''
Service managing all interview problems
'''

def create_interview_problem():

    problem_data = {
        "name": "Design a URL Shortener",
        "problem_number": "1",
        "category": "system_design",
        "difficulty": "medium",
        "details": {
            "description":(
                "Design a URL shortening service that converts long URL's into short links that redirect them to the original URLs."
                "Your solution should consider scalability, reliability, and low latency."
            ),
            "functional_requirements": [
                "Generate short, unique URLs for given long URLs",
                "Service should redirect short URLs to their original targets",
                "Handle very high read traffic efficiently"
            ],
            "non_functional_requirements": [
                "System should be able to handle 100's of millions of requests per day",
                "Scalability to billions of URLs",
                "Low latency (e.g., sub-50ms redirects)",
                "Fault tolerance via replication/failover mechanisms"
            ],
            "assumptions": [
                "Short URL's don't need to be human readable",
                "Deletion is not a core requirement",
                "Links can only contain alphanumeric characters",  
            ],
            "rubric": {
                "functionality": [
                    "Candidate must walk through their high level diagram design and explain how it fulfils the functional requirements",
                    "Solution must design a system to generate short URLs",
                    "The system must be able to redirect short URLs to their original targets"
                    "Candidate should consider and propose a collision handling mechanism",
                    "Supports high read/write ratio traffic",
                ],
                "Scalability": [
                    "Candidate considers scalability of database layer (e.g., sharding, replication, partitioning)",
                    "Candidate considers scaling of application layer (e.g., stateless servers, load balancing)",
                    "Candidate mentions how system scales to hundreds of millions of requests per day"
                ],
                "Performance": [
                    "Candidate considers low latency of redirects",
                ],
                "Tradeoffs": [
                    "Candidate considers tradeoffs between consistency and availability",
                    "Candidate considers tradeoffs between url generation methods (sequential, random, hashing) with pros and cons",
                    "Candidate acknowledges tradeoff between storage simplicity vs flexibility (SQL vs NoSQL)"
                ],
                "Edge Cases": [
                    "Candidate considers extremely long input URLs",
                ],
                "Expansion": [
                    "Candidate considers handling of hot links",
                    "Candidate considers handling of expired links",
                ],
            }
        }
    }


    db_session = session_maker()
    db_session.query(InterviewProblem).delete()
    problem = InterviewProblem(**problem_data)
    db_session.add(problem)
    db_session.commit()
    db_session.refresh(problem)
    return problem


def get_interview_problem(problem_num):
    db_session = session_maker()
    problem = db_session.query(InterviewProblem).filter(InterviewProblem.problem_number == problem_num).first()
    return problem

def __main__():
    create_interview_problem()
    

if __name__ == "__main__":
    __main__()