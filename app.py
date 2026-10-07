
import streamlit as st
from src.schemas import EvaluationReport, LearningRoadmap
from src.backend import extract_text_from_pdf, analyze_cv, generate_roadmap, generate_interview_response

st.set_page_config(page_title="QualifAI Me - AI Career Readiness Toolkit", page_icon="🎯", layout="wide")

if "page" not in st.session_state:
    st.session_state["page"] = "input_page"
if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = []

def set_page(page_name):
    st.session_state["page"] = page_name

def render_circular_progress(score: int):
    if score >= 75:
        color = "#580B14"
    elif score >= 50:
        color = "#801320"
    else:
        color = "#9B1B2B"

    html_code = f"""
    <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
        <div style="
            width: 150px; height: 150px; border-radius: 50%;
            background: conic-gradient({color} {score}%, #D1D5DB {score}% 100%);
            display: flex; justify-content: center; align-items: center;
            box-shadow: 0 4px 10px rgba(88,11,20,0.15);
        ">
            <div style="
                width: 120px; height: 120px; border-radius: 50%;
                background-color: #F4F5F7; display: flex; flex-direction: column;
                justify-content: center; align-items: center;
            ">
                <span style="font-size: 28px; font-weight: bold; color: #22252A;">{score}%</span>
                <span style="font-size: 11px; color: #580B14; font-weight: 700; letter-spacing: 0.5px;">MATCH SCORE</span>
            </div>
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

def render_accordion_roadmap(roadmap_data: LearningRoadmap, timeframe_str: str):
    st.markdown(f"#### 📅 Your Targeted {timeframe_str} Interactive Roadmap")
    if roadmap_data.is_feasible:
        st.success(f"💡 **Feasibility Assessment:** {roadmap_data.feasibility_comment}")
    else:
        st.warning(f"⚠️ **Feasibility Assessment:** {roadmap_data.feasibility_comment}")
        
    for idx, step in enumerate(roadmap_data.steps, 1):
        with st.expander(f"📌 {step.title}", expanded=(idx == 1)):
            for point in step.bullet_points:
                st.markdown(f"• {point}")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration & Navigation")
    groq_api_key = st.text_input("Enter Groq API Key:", type="password")
    st.markdown("[🔑 Get Free Groq API Key](https://console.groq.com/keys)")
    st.markdown("---")
    
    st.subheader("📌 Navigation")
    nav_choice = st.radio(
        "Go to page:",
        ["1. Input Form & Upload", "2. Your Report", "3. Mock Interview Chat"],
        index=0 if st.session_state["page"] == "input_page" else (1 if st.session_state["page"] == "results_page" else 2)
    )
    
    if nav_choice == "1. Input Form & Upload" and st.session_state["page"] != "input_page":
        set_page("input_page")
        st.rerun()
    elif nav_choice == "2. Your Report" and st.session_state["page"] != "results_page":
        if "analysis_result" in st.session_state:
            set_page("results_page")
            st.rerun()
        else:
            st.warning("Please analyze a CV first!")
    elif nav_choice == "3. Mock Interview Chat" and st.session_state["page"] != "interview_page":
        set_page("interview_page")
        st.rerun()

# =========================================================
if st.session_state["page"] == "input_page":
    st.title("🎯 QualifAI Me")
    st.caption("Qualify yourself for your dream job with AI-powered resume analysis, custom roadmaps, and realistic mock interviews.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Target Job Details")
        job_title = st.text_input("Job Title", placeholder="Junior Python Developer")
        requirements = st.text_area("Requirements & Tech Stack", height=120, placeholder="Python, REST APIs, Git, SQL, LangChain")
        responsibilities = st.text_area("Responsibilities", height=120, placeholder="Build automation pipelines, integrate APIs")

    with col2:
        st.subheader("2. Upload Your CV")
        uploaded_file = st.file_uploader("Upload PDF CV", type=["pdf"])

    st.markdown("---")
    if st.button("Evaluate My CV", type="primary", use_container_width=True):
        if not groq_api_key:
            st.error("Please enter your Groq API Key in the sidebar.")
        elif not uploaded_file:
            st.error("Please upload your PDF CV.")
        else:
            with st.spinner("Analyzing your CV..."):
                try:
                    full_cv_text = extract_text_from_pdf(uploaded_file)
                    
                    st.session_state["full_cv_text"] = full_cv_text
                    st.session_state["job_title"] = job_title
                    st.session_state["requirements"] = requirements
                    st.session_state["responsibilities"] = responsibilities
                    st.session_state["chat_messages"] = []
                    
                    if "roadmap_result" in st.session_state:
                        del st.session_state["roadmap_result"]

                    eval_output = analyze_cv(job_title, requirements, responsibilities, full_cv_text, groq_api_key)
                    st.session_state["analysis_result"] = eval_output
                    set_page("results_page")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error during execution: {e}")

# =========================================================
# 📊 الصفحة الثانية: عرض النتائج
# =========================================================
elif st.session_state["page"] == "results_page":
    st.title("📊 Your Report")
    
    if "analysis_result" in st.session_state:
        result: EvaluationReport = st.session_state["analysis_result"]
        
        col_status, col_ring = st.columns([1, 1])
        with col_status:
            st.write("")
            st.write("")
            st.metric("Readiness Status", result.qualification_status)
        with col_ring:
            render_circular_progress(result.match_score)
        
        st.markdown("---")
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📌 Personal Advice", "✅ Matched Skills", "⚠️ Skill Gaps", "🚀 Learning Roadmap", "🎙️ Interview Prep"
        ])
        
        with tab1:
            st.markdown("### Your Career Evaluation")
            st.info(result.summary)
            
        with tab2:
            st.markdown("### Skills You Already Have for This Job")
            if result.matched_skills:
                for skill in result.matched_skills:
                    st.success(f"✔ {skill}")
            else:
                st.write("No matching skills found in your CV for this specific Job.")
                
        with tab3:
            st.markdown("### Technical Skills You Need to Acquire")
            if result.missing_skills:
                for gap in result.missing_skills:
                    st.warning(f"❌ {gap}")
            else:
                st.write("Awesome! You meet all key requirements!")

        with tab4:
            st.markdown("### 🎯 Targeted Skill Preparation Plan")
            if not result.missing_skills:
                st.success("🎉 You already match all required skills for this job! No gap-bridging roadmap needed.")
            else:
                col_duration, col_unit = st.columns([1, 1])
                with col_duration:
                    time_value = st.number_input("Target Duration:", min_value=1, max_value=60, value=2, step=1)
                with col_unit:
                    time_unit = st.selectbox("Time Unit:", ["Months","Weeks", "Days"])
                
                timeframe_str = f"{time_value} {time_unit}"
                st.markdown("---")
                
                if st.button("🚀 Generate Learning Roadmap", type="primary"):
                    if not groq_api_key:
                        st.error("Groq API Key is missing. Please enter it in the sidebar.")
                    else:
                        with st.spinner(f"Evaluating Possibility and building roadmap..."):
                            try:
                                roadmap_output = generate_roadmap(
                                    st.session_state.get("job_title", ""),
                                    result.missing_skills,
                                    timeframe_str,
                                    groq_api_key
                                )
                                st.session_state["roadmap_result"] = roadmap_output
                                st.session_state["roadmap_timeframe"] = timeframe_str
                                st.rerun()
                            except Exception as ex:
                                st.error(f"Failed to generate roadmap: {ex}")

                if "roadmap_result" in st.session_state and st.session_state["roadmap_result"]:
                    st.markdown("---")
                    render_accordion_roadmap(st.session_state["roadmap_result"], st.session_state.get("roadmap_timeframe", timeframe_str))

        with tab5:
            st.markdown("### 🎙️ Professional AI Mock Interview")
            st.caption("Click below to start your structured session (5 Questions Flow).")
            if st.button("🚀 Start Mock Interview", type="primary"):
                st.session_state["chat_messages"] = []
                set_page("interview_page")
                st.rerun()

        st.markdown("---")
        st.button("⬅️ Test Another Job / CV", on_click=lambda: set_page("input_page"))

# =========================================================
# 🎙️ الصفحة الثالثة: الشات والانترفيو
# =========================================================
elif st.session_state["page"] == "interview_page":
    st.title("🎙️ Professional Mock Interview")
    job_title_active = st.session_state.get("job_title", "Target Position")
    st.caption(f"Role: {job_title_active}")

    if not groq_api_key:
        st.error("Please enter your Groq API Key in the sidebar to start the interview.")
    else:
        if not st.session_state["chat_messages"]:
            welcome_msg = (
                f"Welcome to your technical interview for the **{job_title_active}** position! "
                f"I will guide you through a realistic 5-part interview process.\n\n"
                f"**Question 1 (Background & Intro):** Could you brief me on your technical background, "
                f"and highlight 1-2 major projects you have worked on?"
            )
            st.session_state["chat_messages"].append({"role": "assistant", "content": welcome_msg})

        for message in st.session_state["chat_messages"]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if user_input := st.chat_input("Type your interview response here..."):
            st.session_state["chat_messages"].append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            with st.chat_message("assistant"):
                with st.spinner("Interviewer is evaluating..."):
                    try:
                        cv_text = st.session_state.get("full_cv_text", "")
                        job_reqs = st.session_state.get("requirements", "")
                        
                        response_text = generate_interview_response(
                            job_title_active, job_reqs, cv_text, st.session_state["chat_messages"], groq_api_key
                        )
                        st.markdown(response_text)
                        st.session_state["chat_messages"].append({"role": "assistant", "content": response_text})
                    except Exception as err:
                        st.error(f"Error during interview execution: {err}")
