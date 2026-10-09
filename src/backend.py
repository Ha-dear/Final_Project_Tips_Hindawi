from pypdf import PdfReader
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from src.schemas import EvaluationReport, LearningRoadmap

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)
    return " ".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
def analyze_cv(job_title: str, requirements: str, responsibilities: str, cv_text: str, api_key: str, model_name: str = "qwen/qwen3.8-27b") -> EvaluationReport:
    prompt = ChatPromptTemplate.from_template("""
    You are an expert AI Career Coach and Personal Resume Analyst.
    Your task is to analyze the user's CV against their target job posting to help them evaluate their readiness before applying.

    CRITICAL SCORING & TONE RULES:
    - Address the user directly (e.g., "Your background...", "You have strong experience in...").
    - Do NOT talk as an HR recruiter making a hiring decision. Talk as a supportive, honest mentor.
    - Strict Match Score: If NONE of the required technical skills appear in the CV, match_score MUST BE 0%. Do not give points for unrelated experience.
    - All text output MUST be strictly in standard Intermedate English.

    Target Position: {job_title}
    Requirements: {requirements}
    Responsibilities: {responsibilities}

    User's CV Text:
    {context}
    """)
    
    llm = ChatGroq(model=model_name, groq_api_key=api_key, temperature=0.1)
    structured_llm = llm.with_structured_output(EvaluationReport)
    chain = prompt | structured_llm
    
    return chain.invoke({
        "job_title": job_title,
        "requirements": requirements,
        "responsibilities": responsibilities,
        "context": cv_text
    })

def generate_roadmap(job_title: str, missing_skills: list, timeframe_str: str, api_key: str, model_name: str = "qwen/qwen3.8-27b"):
    roadmap_prompt = ChatPromptTemplate.from_template("""
    You are an expert Technical Mentor.
    The candidate is preparing for the position: {job_title}.

    CRITICAL INSTRUCTIONS:
    1. Evaluate if the timeframe '{timeframe}' is realistic/feasible to learn only the basic of ALL these missing skills: {missing_skills}.
    2. Provide a clear 'feasibility_comment' addressing whether this duration is enough or if a longer/different pace is recommended.
    3. Target ONLY the missing technical skills: {missing_skills}.
    4. Break down the timeline strictly into time blocks matching the requested unit (e.g. 'Day 1: [Topic]', 'Day 2: [Topic]' or 'Week 1: [Topic]').
    5. Generate 3-5 specific bullet_points per time step for practical learning.
    6. Output strictly in standard Intermedate English.
    """)
    
    llm = ChatGroq(model=model_name, groq_api_key=api_key, temperature=0.3)
    structured_llm = llm.with_structured_output(LearningRoadmap)
    chain = roadmap_prompt | structured_llm
    
    return chain.invoke({
        "job_title": job_title,
        "missing_skills": ", ".join(missing_skills),
        "timeframe": timeframe_str
    })


def generate_interview_response(job_title: str, job_reqs: str, cv_text: str, chat_history: list, api_key: str, model_name: str = "qwen/qwen3.8-27b") -> str:
    stage_prompt = f"""
You are a Professional Interviewer conducting a structured interview for the position of {job_title}.
Job Requirements: {job_reqs}
Candidate CV Summary: {cv_text[:15000]}

STRUCTURED INTERVIEW FLOW INSTRUCTIONS:
- You must advance the interview structurally and naturally.
- In your response:
  1. Give brief (1-2 sentences) constructive feedback or acknowledge their previous answer.
  2. Move directly to the NEXT logical interview stage based on the guide below.

STAGES GUIDE:
- Stage 1 (Intro Done): You just asked Intro/Background. Next, ask a CORE DOMAIN QUESTION (Stage 2) testing essential skills or knowledge required for {job_title}.
- Stage 2: You just asked Core Domain. Next, ask a SCENARIO-BASED PROBLEM-SOLVING QUESTION (Stage 3) relevant to real challenges in this role.
- Stage 3: You just asked Scenario/Problem-solving. Next, ask a BEHAVIORAL/SITUATIONAL QUESTION (Stage 4) e.g., handling tight deadlines, teamwork, or conflict.
- Stage 4: You just asked Behavioral. Next, provide a FINAL COMPREHENSIVE PERFORMANCE EVALUATION (Stage 5) scoring their overall performance out of 10 with key strengths and improvement areas, then conclude the interview.

Always keep responses concise, encouraging, and candidate-focused in standard Intermediate English.
"""

    conversation_transcript = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in chat_history])
    full_prompt = f"{stage_prompt}\n\nInterview Transcript So Far:\n{conversation_transcript}\nInterviewer:"
    
    llm = ChatGroq(model=model_name, groq_api_key=api_key, temperature=0.7)
    response = llm.invoke(full_prompt)
    return response.content
