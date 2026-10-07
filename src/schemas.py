from pydantic import BaseModel, Field
class EvaluationReport(BaseModel):
    match_score: int = Field(description="Match percentage score from 0 to 100 based strictly on technical match.")
    qualification_status: str = Field(description="Ready to Apply, Partially Ready, or Needs Preparation")
    summary: str = Field(description="Constructive summary directly addressing the user about their fit for this role.")
    matched_skills: List[str] = Field(description="List of matching skills found in your CV")
    missing_skills: List[str] = Field(description="List of required job skills missing from your CV")

class RoadmapStep(BaseModel):
    title: str = Field(description="Header title for the time block, e.g., 'Day 1: Introduction to REST APIs' or 'Week 1: Core SQL Mastery'")
    bullet_points: List[str] = Field(description="List of specific, actionable learning tasks or topics to study for this timeframe.")

class LearningRoadmap(BaseModel):
    is_feasible: bool = Field(description="True if the allocated timeframe is realistically sufficient to learn only the basics of all missing skills; False otherwise.")
    feasibility_comment: str = Field(description="Honest assessment advising the user if this timeline is realistic or too tight to cover all missing gaps effectively.")
    steps: List[RoadmapStep] = Field(description="Structured chronological roadmap covering only missing skills over the requested timeframe.")
