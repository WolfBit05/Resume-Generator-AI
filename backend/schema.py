from pydantic import BaseModel
from typing import List, Optional


class SkillGroup(BaseModel):
    skill_type: str
    skills: List[str]

class Experience(BaseModel):
    role: str
    organization: str
    responsibilities: List[str]

class Project(BaseModel):
    title: str
    description: str
    technologies: Optional[List[str]] = []

class Education(BaseModel):
    degree: str
    institution: str
    year: int
    score: Optional[str] = None

class Certificate(BaseModel):
    name: str
    issuer: Optional[str] = None
    year: Optional[int] = None

class PersonalInfo(BaseModel):
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None

class ResumeAIInput(BaseModel):
    personal_info: Optional[PersonalInfo] = None
    objective: Optional[str] = None
    skills: Optional[List[SkillGroup]] = []
    experience: Optional[List[Experience]] = []
    projects: Optional[List[Project]] = []
    education: Optional[List[Education]] = []
    certificates: Optional[List[Certificate]] = []

class ResumeRequest(BaseModel):
    role_target: str
    constraints: dict
    user_data: ResumeAIInput
