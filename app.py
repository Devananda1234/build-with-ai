import streamlit as st
import time
from engine.analyzer import analyze_idea
from ui.components import (
    render_gauge,
    render_investor_analysis,
    render_risk_report,
    render_bias_detection,
    render_timeline,
    render_ai_critic,
    render_improvements,
    render_final_verdict,
)

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="FailSafe AI — Decision Intelligence Engine",
    page_icon="🛑",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# GLOBAL STYLES
# ─────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap" rel="stylesheet">
<style>
    /* Base */
    html, body, .stApp {
        background-color: #060a0f !important;
        color: #E0E0E0 !important;
        font-family: 'Inter', sans-serif !important;
    }

    /* Hide default Streamlit chrome */
    #MainMenu, footer, header { visibility: hidden; }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #0d1117 !important;
        border-right: 1px solid #1e2a3a !important;
    }
    [data-testid="stSidebar"] * { color: #ccc !important; }
    [data-testid="stSidebar"] .stMarkdown p { color: #888 !important; font-size: 0.82rem !important; }

    /* Inputs */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: #0d1117 !important;
        border: 1px solid #2a3a4a !important;
        color: #E0E0E0 !important;
        border-radius: 8px !important;
        font-family: 'Inter', sans-serif !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #FF4B4B !important;
        box-shadow: 0 0 0 3px rgba(255,75,75,0.15) !important;
    }

    /* Primary button */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #FF4B4B, #C0392B) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        letter-spacing: 2px !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
    }
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(255, 75, 75, 0.4) !important;
    }

    /* Labels */
    .stTextInput label, .stTextArea label {
        color: #888 !important;
        font-size: 0.82rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }

    /* Divider */
    hr { border-color: #1e2a3a !important; }

    /* Plotly */
    .js-plotly-plot { border-radius: 10px; }

    /* Spinner */
    .stSpinner > div { border-top-color: #FF4B4B !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:20px 0 10px 0">
        <div style="font-size:2.5rem">🛑</div>
        <h2 style="color:#FF4B4B;margin:6px 0 4px 0;font-size:1.3rem;letter-spacing:2px">FAILSAFE AI</h2>
        <p style="color:#555;font-size:0.75rem;margin:0">Decision Intelligence Engine</p>
    </div>
    <hr style="border-color:#1e2a3a">
    """, unsafe_allow_html=True)

    api_key = st.text_input("🔑 Groq API Key", type="password", placeholder="gsk_...")

    st.markdown("""
    <div style="background:#0a1520;border:1px solid #1e3a5a;border-radius:8px;padding:12px;margin-top:10px">
        <p style="color:#4a9eff;font-size:0.78rem;margin:0 0 6px 0;font-weight:600">📡 GET FREE API KEY</p>
        <p style="color:#666;font-size:0.75rem;margin:0">Visit <span style="color:#4a9eff">console.groq.com/keys</span> — 100% free, no billing needed. Key starts with <code style="color:#aaa">gsk_</code></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="color:#444;font-size:0.72rem;line-height:1.6">
        <p style="margin:0 0 4px 0;color:#555;font-weight:600">WHAT THIS DOES</p>
        <p style="margin:0">🔴 Investor rejection analysis</p>
        <p style="margin:0">🔴 Risk & failure simulation</p>
        <p style="margin:0">🔴 Cognitive bias detection</p>
        <p style="margin:0">🔴 Month-by-month timeline</p>
        <p style="margin:0">🔴 Brutal AI critic verdict</p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HERO HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:3rem 0 2rem 0">
    <div style="display:inline-block;background:linear-gradient(135deg,rgba(255,75,75,0.15),rgba(192,57,43,0.1));
        border:1px solid rgba(255,75,75,0.3);border-radius:50px;padding:6px 20px;margin-bottom:20px">
        <span style="color:#FF4B4B;font-size:0.8rem;font-weight:600;letter-spacing:3px">CRITICAL ANALYSIS ENGINE</span>
    </div>
    <h1 style="font-size:3.2rem;font-weight:900;margin:0 0 12px 0;line-height:1.1">
        <span style="color:#FFFFFF">Your Idea Will </span>
        <span style="background:linear-gradient(135deg,#FF4B4B,#FF8C00);-webkit-background-clip:text;-webkit-text-fill-color:transparent">Fail.</span>
    </h1>
    <p style="color:#666;font-size:1.1rem;max-width:600px;margin:0 auto;line-height:1.6">
        FailSafe AI simulates three independent expert agents — an Investor, a Risk Analyst, and a Psychologist — to ruthlessly expose the weaknesses in your idea before reality does.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# INPUT FORM
# ─────────────────────────────────────────────
st.markdown("""
<p style="color:#888;font-size:0.8rem;text-transform:uppercase;letter-spacing:2px;margin-bottom:1rem">
    📝 INPUT YOUR IDEA
</p>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([3, 2], gap="large")

with col_left:
    idea = st.text_area(
        "Describe your startup / project idea",
        placeholder="e.g. An AI-powered meal planning app that learns your dietary preferences and automatically orders groceries from local stores...",
        height=160,
    )

with col_right:
    domain = st.text_input("Industry / Domain", placeholder="e.g. FoodTech, AI SaaS, FinTech")
    target_audience = st.text_input("Target Audience", placeholder="e.g. Busy urban professionals aged 25-40")
    budget = st.text_input("Budget & Resources", placeholder="e.g. $50K bootstrapped, 2 developers")

st.markdown("<br>", unsafe_allow_html=True)
analyze_clicked = st.button("🛑 PREDICT FAILURE", type="primary", use_container_width=True)

# ─────────────────────────────────────────────
# VALIDATION & ANALYSIS
# ─────────────────────────────────────────────
if analyze_clicked:
    if not api_key:
        st.error("⚠️ Please provide your Groq API Key in the sidebar to run the analysis.")
    elif not idea.strip():
        st.error("⚠️ Please describe your idea before running the analysis.")
    elif not domain.strip():
        st.error("⚠️ Please specify the industry/domain.")
    else:
        progress_messages = [
            "🔍 Activating Investor Agent — scanning ROI potential...",
            "⚠️ Activating Risk Analyst — identifying failure vectors...",
            "🧠 Activating Psychologist — detecting cognitive biases...",
            "⏳ Simulating failure timeline...",
            "🤖 Engaging Brutal Mode — compiling final verdict...",
        ]

        progress_bar = st.progress(0)
        status_box = st.empty()

        for i, msg in enumerate(progress_messages):
            status_box.markdown(f"""
            <div style="background:#0d1117;border:1px solid #1e2a3a;border-radius:8px;padding:12px 16px;color:#888;font-size:0.9rem">
                {msg}
            </div>""", unsafe_allow_html=True)
            progress_bar.progress(int((i + 1) / len(progress_messages) * 60))
            time.sleep(0.6)

        try:
            result = analyze_idea(api_key, idea, target_audience, budget, domain)

            progress_bar.progress(100)
            status_box.empty()
            progress_bar.empty()

            # ── SECTION 1: Failure Probability ──────────────
            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown("""
            <div style="text-align:center;margin:1.5rem 0 1rem 0">
                <h2 style="color:#FF4B4B;font-size:1.6rem;font-weight:800;letter-spacing:3px;margin:0">
                    📊 RISK ASSESSMENT DASHBOARD
                </h2>
            </div>
            """, unsafe_allow_html=True)

            gauge_col1, gauge_col2, confidence_col = st.columns([2, 2, 2])

            with gauge_col1:
                render_gauge(
                    result.failure_probability,
                    "Failure Probability",
                    ["#00CC96", "#FFA15A", "#EF553B"],
                )

            with gauge_col2:
                render_gauge(
                    result.bias_detection.overall_bias_score,
                    "Human Bias Score",
                    ["#00CC96", "#FFA15A", "#AB63FA"],
                )

            with confidence_col:
                risk_color = {"Low": "#4CAF50", "Medium": "#FFA500", "High": "#FF4B4B"}.get(result.risk_level, "#FFA500")
                st.markdown(f"""
                <div style="background:#0d1117;border:1px solid #1e2a3a;border-radius:12px;padding:24px;height:210px;
                    display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
                    <p style="color:#666;font-size:0.75rem;text-transform:uppercase;letter-spacing:2px;margin:0 0 8px 0">Risk Level</p>
                    <div style="background:{risk_color}22;border:2px solid {risk_color};border-radius:8px;
                        padding:8px 24px;margin-bottom:16px">
                        <span style="color:{risk_color};font-size:1.4rem;font-weight:800;letter-spacing:3px">{result.risk_level.upper()}</span>
                    </div>
                    <p style="color:#666;font-size:0.75rem;text-transform:uppercase;letter-spacing:2px;margin:0 0 4px 0">AI Confidence</p>
                    <p style="color:#FFFFFF;font-size:2rem;font-weight:900;margin:0">{result.confidence_score}%</p>
                    <p style="color:#555;font-size:0.75rem;margin:8px 0 0 0;line-height:1.4">{result.confidence_explanation}</p>
                </div>
                """, unsafe_allow_html=True)

            # ── SECTION 2: Investor Analysis ─────────────────
            st.markdown("<hr>", unsafe_allow_html=True)
            render_investor_analysis(result.investor_analysis)

            # ── SECTION 3: Risk Analyst Report ───────────────
            st.markdown("<hr>", unsafe_allow_html=True)
            render_risk_report(result.risk_analyst_report)

            # ── SECTION 4: Bias Detection ─────────────────────
            st.markdown("<hr>", unsafe_allow_html=True)
            render_bias_detection(result.bias_detection)

            # ── SECTION 5: Timeline Simulation ───────────────
            st.markdown("<hr>", unsafe_allow_html=True)
            render_timeline(result.timeline_simulation)

            # ── SECTION 6: AI Critic Brutal Mode ─────────────
            st.markdown("<hr>", unsafe_allow_html=True)
            render_ai_critic(result.ai_critic_brutal)

            # ── SECTION 7 & 8: Improvements + Verdict ────────
            st.markdown("<hr>", unsafe_allow_html=True)
            imp_col, verdict_col = st.columns([1, 1], gap="large")
            with imp_col:
                render_improvements(result.improvement_suggestions)
            with verdict_col:
                render_final_verdict(result.final_verdict, result.final_verdict_justification)

            st.markdown("<br><br>", unsafe_allow_html=True)

        except Exception as e:
            progress_bar.empty()
            status_box.empty()
            st.error(f"❌ Analysis failed: {str(e)}")
            st.markdown("""
            <div style="background:#1a0a0a;border:1px solid #FF4B4B;border-radius:8px;padding:16px;margin-top:8px">
                <p style="color:#FF9999;font-size:0.9rem;margin:0"><strong>Tip:</strong> Make sure your Groq API key is valid (starts with <code>gsk_</code>).
                Get a free key at <a href="https://console.groq.com/keys" style="color:#4a9eff">console.groq.com/keys</a> — no billing required.</p>
            </div>
            """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# EMPTY STATE
# ─────────────────────────────────────────────
else:
    st.markdown("""
    <div style="text-align:center;padding:3rem 2rem;background:#0d1117;border:1px dashed #1e2a3a;
        border-radius:16px;margin-top:1rem">
        <div style="font-size:3rem;margin-bottom:12px">🎯</div>
        <h3 style="color:#333;margin:0 0 8px 0">Ready to destroy your idea?</h3>
        <p style="color:#444;font-size:0.9rem;max-width:400px;margin:0 auto">
            Fill in your idea details above, paste your Groq API key in the sidebar, and hit <strong style="color:#FF4B4B">PREDICT FAILURE</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)
