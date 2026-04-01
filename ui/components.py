import streamlit as st
import plotly.graph_objects as go
from engine.models import (
    FailurePrediction, InvestorAnalysis, RiskAnalystReport,
    BiasDetection, BiasEntry, TimelineMonth
)


# ─────────────────────────────────────────────
# GAUGE CHART
# ─────────────────────────────────────────────
def render_gauge(value: int, title: str, thresholds: list):
    """Render a Plotly gauge with dark theme."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={"text": title, "font": {"size": 18, "color": "#E0E0E0"}},
        number={"font": {"size": 36, "color": "#FFFFFF"}, "suffix": "%"},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#888", "tickfont": {"color": "#888"}},
            "bar": {"color": "#FF4B4B", "thickness": 0.3},
            "bgcolor": "rgba(30,30,30,0.8)",
            "borderwidth": 0,
            "steps": [
                {"range": [0, 33], "color": "rgba(0, 200, 150, 0.25)"},
                {"range": [33, 66], "color": "rgba(255, 161, 90, 0.25)"},
                {"range": [66, 100], "color": "rgba(239, 85, 59, 0.25)"},
            ],
            "threshold": {
                "line": {"color": thresholds[0] if value < 33 else thresholds[1] if value < 66 else thresholds[2], "width": 5},
                "thickness": 0.8,
                "value": value,
            },
        },
    ))
    fig.update_layout(
        height=230,
        margin=dict(l=20, r=20, t=60, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "#E0E0E0"},
    )
    st.plotly_chart(fig, use_container_width=True)


# ─────────────────────────────────────────────
# SECTION HEADER
# ─────────────────────────────────────────────
def section_header(icon: str, title: str, subtitle: str = ""):
    st.markdown(f"""
    <div style="margin: 2rem 0 1rem 0; display: flex; align-items: center; gap: 12px;">
        <span style="font-size: 2rem;">{icon}</span>
        <div>
            <h2 style="margin:0; color:#FF4B4B; font-size:1.4rem;">{title}</h2>
            {"<p style='margin:0; color:#888; font-size:0.85rem;'>" + subtitle + "</p>" if subtitle else ""}
        </div>
    </div>
    <hr style="border-color: #2a2a2a; margin-bottom: 1rem;">
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# INVESTOR ANALYSIS
# ─────────────────────────────────────────────
def render_investor_analysis(data: InvestorAnalysis):
    section_header("💰", "INVESTOR ANALYSIS", "Why investors will pass on your idea")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**❌ Why Investors Will Reject**")
        for r in data.rejection_reasons:
            st.markdown(f"""<div style="background:#1a1a2e;border-left:3px solid #FF4B4B;padding:8px 12px;margin:4px 0;border-radius:4px;font-size:0.9rem">{r}</div>""", unsafe_allow_html=True)

        st.markdown("<br>**📉 ROI Concerns**", unsafe_allow_html=True)
        for c in data.roi_concerns:
            st.markdown(f"""<div style="background:#1a1a2e;border-left:3px solid #FFA15A;padding:8px 12px;margin:4px 0;border-radius:4px;font-size:0.9rem">{c}</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("**⚙️ Scalability Issues**")
        for s in data.scalability_issues:
            st.markdown(f"""<div style="background:#1a1a2e;border-left:3px solid #AB63FA;padding:8px 12px;margin:4px 0;border-radius:4px;font-size:0.9rem">{s}</div>""", unsafe_allow_html=True)

        st.markdown("<br>**🏆 Competition Analysis**", unsafe_allow_html=True)
        st.markdown(f"""<div style="background:#1a1a2e;border:1px solid #333;padding:14px;border-radius:8px;font-size:0.9rem;line-height:1.6;color:#ccc">{data.competition_analysis}</div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# RISK ANALYST REPORT
# ─────────────────────────────────────────────
def render_risk_report(data: RiskAnalystReport):
    section_header("⚠️", "RISK ANALYST REPORT", "Key failure vectors and operational threats")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🔴 Key Risks**")
        for i, r in enumerate(data.key_risks, 1):
            st.markdown(f"""<div style="background:#1a0a0a;border-left:3px solid #FF4B4B;padding:8px 12px;margin:4px 0;border-radius:4px;font-size:0.9rem"><span style="color:#FF4B4B;font-weight:bold">Risk {i}:</span> {r}</div>""", unsafe_allow_html=True)

        st.markdown("<br>**💥 Failure Triggers**", unsafe_allow_html=True)
        for t in data.failure_triggers:
            st.markdown(f"""<div style="background:#1a0a0a;border-left:3px solid #FF6B6B;padding:8px 12px;margin:4px 0;border-radius:4px;font-size:0.9rem">⚡ {t}</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("**🔧 Feasibility Issues**")
        for f in data.feasibility_issues:
            st.markdown(f"""<div style="background:#0a0a1a;border-left:3px solid #636EFA;padding:8px 12px;margin:4px 0;border-radius:4px;font-size:0.9rem">{f}</div>""", unsafe_allow_html=True)

        st.markdown("<br>**🏗️ Operational Challenges**", unsafe_allow_html=True)
        for o in data.operational_challenges:
            st.markdown(f"""<div style="background:#0a0a1a;border-left:3px solid #19D3F3;padding:8px 12px;margin:4px 0;border-radius:4px;font-size:0.9rem">{o}</div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# BIAS DETECTION
# ─────────────────────────────────────────────
def _bias_card(name: str, icon: str, entry: BiasEntry, color: str):
    detected_label = "✅ DETECTED" if entry.detected else "⬜ Not Found"
    detected_color = "#FF4B4B" if entry.detected else "#4CAF50"
    st.markdown(f"""
    <div style="background:#111827;border:1px solid {color};border-radius:10px;padding:16px;margin:8px 0;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
            <span style="font-size:1rem;font-weight:bold;color:{color}">{icon} {name}</span>
            <span style="color:{detected_color};font-size:0.8rem;font-weight:bold">{detected_label}</span>
        </div>
        <div style="background:#1f293799;border-radius:6px;height:8px;margin-bottom:10px;overflow:hidden">
            <div style="background:{color};width:{entry.score}%;height:100%;border-radius:6px;transition:width 0.5s"></div>
        </div>
        <p style="color:#aaa;font-size:0.85rem;margin:0;line-height:1.5">{entry.explanation}</p>
    </div>
    """, unsafe_allow_html=True)


def render_bias_detection(data: BiasDetection):
    section_header("🧠", "PSYCHOLOGICAL BIAS DETECTION", "Hidden cognitive distortions in your thinking")

    st.markdown(f"""
    <div style="text-align:center;background:linear-gradient(135deg,#1a0a2e,#2a0a1e);border:1px solid #7B2D8B;border-radius:12px;padding:20px;margin-bottom:1.5rem">
        <p style="color:#ccc;font-size:0.9rem;margin:0 0 6px 0">Overall Bias Score</p>
        <h1 style="color:#AB63FA;font-size:3.5rem;margin:0;font-weight:900">{data.overall_bias_score}<span style="font-size:1.5rem">%</span></h1>
        <p style="color:#888;font-size:0.8rem;margin:4px 0 0 0">{"🔴 Highly Biased" if data.overall_bias_score > 66 else "🟡 Moderately Biased" if data.overall_bias_score > 33 else "🟢 Low Bias"}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        _bias_card("Overconfidence Bias", "🎯", data.overconfidence, "#FF4B4B")
        _bias_card("Survivorship Bias", "💀", data.survivorship_bias, "#636EFA")
    with col2:
        _bias_card("Trend-Following Bias", "📈", data.trend_following, "#FFA15A")
        _bias_card("Emotional Reasoning", "❤️", data.emotional_reasoning, "#EF553B")


# ─────────────────────────────────────────────
# TIMELINE SIMULATION
# ─────────────────────────────────────────────
def render_timeline(timeline: list):
    section_header("⏳", "TIMELINE SIMULATION", "Realistic month-by-month failure trajectory")

    colors = ["#636EFA", "#FFA15A", "#EF553B", "#FF0033"]
    icons = ["🚀", "📉", "🆘", "💀"]

    for i, month in enumerate(timeline):
        color = colors[min(i, len(colors) - 1)]
        icon = icons[min(i, len(icons) - 1)]

        st.markdown(f"""
        <div style="background:#0d1117;border:1px solid {color};border-radius:12px;padding:20px;margin:12px 0;position:relative;overflow:hidden">
            <div style="position:absolute;top:0;left:0;width:4px;height:100%;background:{color}"></div>
            <div style="padding-left:12px">
                <h3 style="color:{color};margin:0 0 12px 0">{icon} {month.month}</h3>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
                    <div>
                        <p style="color:#888;font-size:0.75rem;text-transform:uppercase;margin:0 0 4px 0">👥 User Growth</p>
                        <p style="color:#ddd;font-size:0.9rem;margin:0">{month.user_growth}</p>
                    </div>
                    <div>
                        <p style="color:#888;font-size:0.75rem;text-transform:uppercase;margin:0 0 4px 0">🏁 Competition Impact</p>
                        <p style="color:#ddd;font-size:0.9rem;margin:0">{month.competition_impact}</p>
                    </div>
                    <div>
                        <p style="color:#888;font-size:0.75rem;text-transform:uppercase;margin:0 0 4px 0">💰 Financial Condition</p>
                        <p style="color:#ddd;font-size:0.9rem;margin:0">{month.financial_condition}</p>
                    </div>
                    <div>
                        <p style="color:#888;font-size:0.75rem;text-transform:uppercase;margin:0 0 4px 0">🚨 Failure Signals</p>
                        <p style="color:#FF6B6B;font-size:0.9rem;margin:0">{month.failure_signals}</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# AI CRITIC BRUTAL MODE
# ─────────────────────────────────────────────
def render_ai_critic(critic_text: str):
    section_header("🤖", "AI CRITIC — BRUTAL MODE", "Unfiltered decision intelligence assessment")

    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#1a0000,#0d0000);border:2px solid #FF0033;border-radius:12px;padding:24px;position:relative;overflow:hidden">
        <div style="position:absolute;top:-20px;right:-20px;font-size:120px;opacity:0.05">🛑</div>
        <p style="color:#FF9999;font-size:1rem;line-height:1.8;margin:0;font-style:italic">"{critic_text}"</p>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# IMPROVEMENT SUGGESTIONS
# ─────────────────────────────────────────────
def render_improvements(suggestions: list):
    section_header("🛠️", "IMPROVEMENT SUGGESTIONS", "Actionable fixes to reduce failure probability")

    for i, s in enumerate(suggestions, 1):
        st.markdown(f"""
        <div style="background:#0a1a0a;border:1px solid #2a4a2a;border-left:4px solid #4CAF50;border-radius:8px;padding:14px 16px;margin:8px 0;display:flex;gap:12px;align-items:flex-start">
            <span style="color:#4CAF50;font-weight:bold;font-size:1.1rem;min-width:28px">{i}.</span>
            <span style="color:#c8e6c9;font-size:0.92rem;line-height:1.6">{s}</span>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FINAL VERDICT
# ─────────────────────────────────────────────
def render_final_verdict(verdict: str, justification: str):
    section_header("⚖️", "FINAL VERDICT", "The FailSafe AI decision")

    configs = {
        "Reject": {
            "icon": "❌",
            "color": "#FF0033",
            "bg": "linear-gradient(135deg, #2a0000, #1a0000)",
            "border": "#FF0033",
            "label": "REJECT",
        },
        "Risky": {
            "icon": "⚠️",
            "color": "#FFA500",
            "bg": "linear-gradient(135deg, #2a1a00, #1a1000)",
            "border": "#FFA500",
            "label": "RISKY — PROCEED WITH CAUTION",
        },
        "Consider": {
            "icon": "✅",
            "color": "#4CAF50",
            "bg": "linear-gradient(135deg, #001a00, #000d00)",
            "border": "#4CAF50",
            "label": "CONSIDER — WITH MODIFICATIONS",
        },
    }

    cfg = configs.get(verdict, configs["Risky"])

    st.markdown(f"""
    <div style="background:{cfg['bg']};border:2px solid {cfg['border']};border-radius:16px;padding:30px;text-align:center;margin-top:1rem">
        <div style="font-size:4rem;margin-bottom:10px">{cfg['icon']}</div>
        <h1 style="color:{cfg['color']};font-size:2.5rem;margin:0 0 16px 0;letter-spacing:4px">{cfg['label']}</h1>
        <p style="color:#ccc;font-size:1rem;line-height:1.7;max-width:700px;margin:0 auto">{justification}</p>
    </div>
    """, unsafe_allow_html=True)
