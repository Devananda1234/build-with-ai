from pydantic import BaseModel, Field
from typing import List, Literal


class InvestorAnalysis(BaseModel):
    rejection_reasons: List[str] = Field(..., description="Why an investor would reject this idea")
    roi_concerns: List[str] = Field(..., description="Return on investment concerns")
    scalability_issues: List[str] = Field(..., description="Scalability bottlenecks and issues")
    competition_analysis: str = Field(..., description="Market competition analysis")


class RiskAnalystReport(BaseModel):
    key_risks: List[str] = Field(..., description="Key operational and strategic risks")
    failure_triggers: List[str] = Field(..., description="Specific events that would trigger failure")
    feasibility_issues: List[str] = Field(..., description="Technical and operational feasibility problems")
    operational_challenges: List[str] = Field(..., description="Day-to-day operational challenges")


class BiasEntry(BaseModel):
    detected: bool = Field(..., description="Whether this bias is detected")
    score: int = Field(..., description="Bias intensity score 0-100")
    explanation: str = Field(..., description="Why this specific bias was detected and its impact")


class BiasDetection(BaseModel):
    overall_bias_score: int = Field(..., description="Overall human bias score 0-100")
    overconfidence: BiasEntry
    trend_following: BiasEntry
    emotional_reasoning: BiasEntry
    survivorship_bias: BiasEntry


class TimelineMonth(BaseModel):
    month: str = Field(..., description="Time label e.g. Month 1, Month 3")
    user_growth: str = Field(..., description="User growth situation at this point")
    competition_impact: str = Field(..., description="Competition impact at this point")
    financial_condition: str = Field(..., description="Financial health at this point")
    failure_signals: str = Field(..., description="Warning signs and failure signals")


class FailurePrediction(BaseModel):
    # Section 1
    failure_probability: int = Field(..., description="Failure probability 0-100")
    risk_level: Literal["Low", "Medium", "High"] = Field(..., description="Overall risk level")
    confidence_score: int = Field(..., description="AI confidence in its prediction 0-100")
    confidence_explanation: str = Field(..., description="Why the AI is this confident in its prediction")

    # Section 2
    investor_analysis: InvestorAnalysis

    # Section 3
    risk_analyst_report: RiskAnalystReport

    # Section 4
    bias_detection: BiasDetection

    # Section 5
    timeline_simulation: List[TimelineMonth] = Field(..., description="Month-by-month failure timeline")

    # Section 6
    ai_critic_brutal: str = Field(..., description="Brutal AI critic review - why this will fail, what was ignored")

    # Section 7
    improvement_suggestions: List[str] = Field(..., description="Actionable fixes and alternative strategies")

    # Section 8
    final_verdict: Literal["Reject", "Risky", "Consider"] = Field(..., description="Final decision verdict")
    final_verdict_justification: str = Field(..., description="Clear justification for the final verdict")
