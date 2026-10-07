# 🚀 [Tips Hindawi](https://www.tipshindawi.com/) Internship (August–October) 2026

> 🎓 This project was built during the [ **Tips Hindawi** ](https://www.tipshindawi.com/) **Internship (August–October) 2026**.

## 👤 Participant

| Field            | Value                                |
| ---------------- | ------------------------------------ |
| Full Name        |          Hadear Mohamed Reda         |
| Project Name     |              QualifAI Me             |
| GitHub Username  |                Ha-dear               |
| Internship Batch | August–October 2026                  |
| Training Program | Large Language Models (LLMs) Program |
| Organization     | [**Edrak for Ai**](https://edrak4ai.com/en)                         |

---

# 📖 Project Overview
**QualifAI Me** 🎯 is a modularized, AI-powered career assistant designed to evaluate candidate CVs against target job descriptions, bridge technical skill gaps with personalized learning roadmaps, and prepare candidates through realistic, interactive mock interviews.

By combining structured outputs, dynamic prompt orchestration, and high-performance LLM inference, QualifAI Me delivers a seamless, three-step career readiness journey.
---

# ✨ Features

* **📄 CV Evaluation & Gap Analysis:** Analyzes uploaded PDF resumes against job requirements to produce a match percentage score, key strengths, missing skills, and an executive evaluation summary using Pydantic structured outputs.
* **🗺️ Targeted Learning Roadmap:** Automatically generates a structured, step-by-step learning path tailored specifically to bridge identified technical skill gaps for the target job role.
* **🎙️ Interactive Mock Interview:** Conducts a dynamic, 5-stage conversational mock interview with custom temperature settings (`0.7`) for realistic interaction and tailored response evaluation.
* **🎨 Custom Aesthetic UI:** Built with a modern, streamlined Streamlit layout using a custom "Dark red / Grey" theme and robust session state management.

---

# 🛠️ Technologies Used

* **Deployment & Hosting:** Streamlit Community Cloud (Live Cloud Hosting)
* **Streamlit:** Interactive UI and multi-page navigation state management.
* **LangChain & LangChain-Groq:** LLM orchestration and high-speed API execution (`Qwen-27b`).
* **Pydantic:** Schema validation and structured output parsing for evaluation reports and roadmaps.
* **PyPDF:** Resume text parsing and extraction.
---

# ⚙️ Installation

### 🌐 Live Web Application
You can access and test the live application directly without any local installation:
👉 **[QualifAI Me Live App](https://finalprojecttipshindawi-g5c8daxj57ya3dewfq4vym.streamlit.app/)** 

---

### 💻 Local Setup & Execution

If you prefer to run the project locally, follow these steps:

1. **Clone the Repository:**
```bash
   git clone [https://github.com/Ha-dear/Final_Project_Tips_Hindawi.git]
   cd Final_Project_Tips_Hindawi

---
2. **Create & Activate Virtual Environment:**
    Bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
   
3. **Install Required Packages:**
    Bash
    pip install -r requirements.txt

4. **Run the Streamlit App:**
    Bash
    streamlit run app.py
       


# 🚀 Usage

Using **QualifAI Me** is straightforward and follows a simple 3-step workflow:

### 1️⃣ Setup & Credentials
* Open the application in your browser.
* Enter your **Groq API Key** in the sidebar.
* Upload your CV in **PDF format**.
* Enter the **Target Job Title** and paste the **Job Description / Requirements**.

### 2️⃣ CV Analysis & Skill Gap Identification
* Click the **"Evalute My CV"** button.
* Review your personalized dashboard:
  * **Match Score:** A percentage showing how well your CV aligns with the job.
  * **Matched Skills:** Areas where your background excels.
  * **Skill Gaps:** Missing technical skills or requirements.
  * **Learning Roadmap:** A structured, step-by-step guide to bridge the identified gaps.

### 3️⃣ Interactive Mock Interview
* Navigate to the **Mock Interview** section.
* Click **"Start Mock Interview"** to begin a multi-stage interactive practice session.
* Answer the interviewer's technical and situational questions.
* Receive real-time evaluation and feedback on your answers.

---

# 📸 Demo

Add screenshots, GIFs, or a demo video.

---

# 📈 Results

The development and deployment of **QualifAI Me** yielded the following key outcomes and technical achievements:

* **⚡ High-Precision CV Evaluation:** Successfully integrated Pydantic structured outputs with LLM orchestration, enabling deterministic schema parsing for Match Scores, Matched Skills , and Skill Gaps.
* **🎯 Tailored Learning Roadmaps:** Automated the extraction of missing technical competencies and generated actionable, step-by-step career development roadmaps tailored to specific job requirements.
* **💬 Dynamic Interactive Mock Interviews:** Implemented a multi-turn conversational interface with optimized temperature parameters (`0.7`), offering candidates real-time feedback and structured evaluations during practice sessions.
* **🌐 Live Cloud Accessibility:** Successfully deployed on **Streamlit Community Cloud**, making the career assistant publicly accessible to candidates with zero local installation overhead.
---

# 🔮 Future Improvements

* **📚 RAG Integration (Retrieval-Augmented Generation):** Integrate a vector database (e.g., FAISS or ChromaDB) to ground resume analysis and interview prep on real-world industry benchmarks, company-specific frameworks, and verified learning resources.
* **🌐 Multilingual Support (Arabic Language Integration):** Expand the UI and LLM prompting logic to fully support Arabic, enabling seamless resume parsing, gap analysis, and mock interviews for Arabic-speaking users.
* **📊 CV Profile Viewer Page:** Add a dedicated dashboard/page to display structured, extracted details from the uploaded CV (e.g., contact info, work history, skills breakdown, education) for easy review and quick edits.
* **✏️ AI-Powered Resume Tailoring & PDF Export:** Implement an intelligent resume builder that automatically tailors the CV to match specific job requirements and allows candidates to export the optimized, job-ready resume directly as a PDF.
---

# 📚 About the Internship

This project was developed as part of the [**Tips Hindawi**](https://www.tipshindawi.com/) **Internship (August–October) 2026**, and it will be showcased on the official [Tips Hindawi](https://www.tipshindawi.com/) website.

[Tips Hindawi](https://www.tipshindawi.com/) is the internships department of [**Edrak for Ai**](https://edrak4ai.com/en), and the internship encourages participants to build real-world projects, apply practical skills, and showcase their work through GitHub.

For more information about the internship, training programs, and upcoming batches, visit the official [Tips Hindawi](https://www.tipshindawi.com/) website.

---

# 📄 License

This project is shared for educational and portfolio purposes.
