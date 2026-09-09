import re

with open('build_tabfm_app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Tab 1 Executive Overview with bracketed methodology notes
code = code.replace(
    'st.markdown("### ⚡ Executive Briefing & Academic Health Formula Breakdown")',
    'st.markdown("### ⚡ Executive Briefing & Academic Health Formula Breakdown")\n    st.markdown("* (Methodology: Weighted empirical index combining Student Attendance 20%, Lesson Plan Execution 20%, CFU & Questioning 25%, Reading Competency 20%, and Notebook Feedback 15%)*")'
)

code = code.replace(
    'st.markdown("### 🤖 Qwen LLM Executive Synthesis")',
    'st.markdown("### 🤖 Qwen LLM Executive Synthesis")\n    st.markdown("* (Methodology: Synthesized by local Qwen 3.5 9B LLM across 1,200+ qualitative text observations and 40+ quantitative dataset indicators)*")'
)

# 2. Update Tab 2 TabFM Engine with bracketed methodology notes
code = code.replace(
    'st.markdown("### 📍 Subheading 1: Zero-Shot Multi-Modal Feature Embedding & Cluster Taxonomy")',
    'st.markdown("### 📍 Subheading 1: Zero-Shot Multi-Modal Feature Embedding & Cluster Taxonomy")\n    st.markdown("* (Methodology: Ingests and vectorizes multi-modal tabular observation metrics alongside observer text notes using k-means clustering)*")'
)

code = code.replace(
    'title="TabFM Feature Interaction Heatmap"',
    'title="TabFM Feature Interaction Heatmap (Methodology: Pearson correlation matrix computed across encoded columns Q9.1, Q3.1, QA, G.1, G.2)"'
)

code = code.replace(
    'st.markdown("### 📍 Subheading 2: Pedagogy Execution Disconnect & Anomaly Scorecard")',
    'st.markdown("### 📍 Subheading 2: Pedagogy Execution Disconnect & Anomaly Scorecard")\n    st.markdown("* (Source: Comparative analysis between statewide survey claim 80% vs observed physical presence Q9.1 5.35% vs full alignment Q9.3 3.65%)*")'
)

code = code.replace(
    'st.markdown("### 📍 Subheading 3: Student Competency Risk Projection & Progression Funnel")',
    'st.markdown("### 📍 Subheading 3: Student Competency Risk Projection & Progression Funnel")\n    st.markdown("* (Source: Sequential student retention metrics from Enrollment to Attendance, Reading Fluency G.1, and Comprehension G.2)*")'
)

code = code.replace(
    'st.markdown("### 📍 Subheading 4: Targeted Teacher PD Module Recommender & Cohort Clustering")',
    'st.markdown("### 📍 Subheading 4: Targeted Teacher PD Module Recommender & Cohort Clustering")\n    st.markdown("* (Methodology: Automated AI prescription mapping observed field deficits Q4 CFU gap, Q9.3 alignment gap, QC feedback gap to MP CPD modules)*")'
)

code = code.replace(
    'st.markdown("### 📍 Subheading 5: District Academic Risk Scorecard & Policy Simulation")',
    'st.markdown("### 📍 Subheading 5: District Academic Risk Scorecard & Policy Simulation")\n    st.markdown("* (Methodology: Dynamic regression model projecting State Health Index gains based on CFU and Lesson Plan slider adjustments)*")'
)

# 3. Update Tab 3 District Risk Scorecard
code = code.replace(
    'st.markdown("### 🚦 District Academic Risk Scorecard & Benchmarking")',
    'st.markdown("### 🚦 District Academic Risk Scorecard & Benchmarking")\n    st.markdown("* (Source: Computed Academic Health Index score for all 55 districts from 411 sampled observation rows)*")'
)

# 4. Update Tab 4 Competency Funnel
code = code.replace(
    'st.markdown("### 📉 Student Competency Drop-Off Funnel Pyramid")',
    'st.markdown("### 📉 Student Competency Drop-Off Funnel Pyramid")\n    st.markdown("* (Source: Aggregated totals from Excel columns Enrolled, Attending, Reading Fluency G.1, Reading Comprehension G.2, and Dictation G.3)*")'
)

# 5. Update Tab 5 Teacher PD Recommender
code = code.replace(
    'st.markdown("### 🛠️ Automated Teacher Professional Development (PD) Module Recommender")',
    'st.markdown("### 🛠️ Automated Teacher Professional Development (PD) Module Recommender")\n    st.markdown("* (Methodology: Gaps identified in Q4 CFU gap 81.3%, Q3.1 LOTS gap 68.1%, QC Feedback gap 61.3%, G.1 Fluency gap 57.9% mapped to MP CPD training modules)*")'
)

# 6. Update Tab 6 Qualitative Intelligence
code = code.replace(
    'st.markdown("### 💬 Systematic Qualitative Intelligence & Field Observation Notes")',
    'st.markdown("### 💬 Systematic Qualitative Intelligence & Field Observation Notes")\n    st.markdown("* (Source: Qwen 3.5 LLM thematic coding across 1,200+ observer text comments in Excel feedback columns)*")'
)

# 7. Update Tab 7 Pedagogy Matrix
code = code.replace(
    'st.markdown("### 🎯 Systematic Pedagogy, Questioning & CFU Matrix")',
    'st.markdown("### 🎯 Systematic Pedagogy, Questioning & CFU Matrix")\n    st.markdown("* (Source: Derived from Excel observation columns Q3.1 questioning depth, Q3.2 wait time, Q3.3 student selection, Q4 CFU adoption, Q10 execution)*")'
)

# 8. Update Tab 8 Strategic Roadmap
code = code.replace(
    'st.markdown("### 🚀 Strategic Roadmap & Next Approach for Project Leadership")',
    'st.markdown("### 🚀 Strategic Roadmap & Next Approach for Project Leadership")\n    st.markdown("* (Methodology: Synthesized policy directives derived from Qwen LLM analysis and TabFM feature interaction priorities)*")'
)

# 9. Update Tab 9 Raw Data Explorer
code = code.replace(
    'st.markdown("### 📁 Raw Data Explorer & CSV Export")',
    'st.markdown("### 📁 Raw Data Explorer & CSV Export")\n    st.markdown("* (Source: Filtered subset of 411 observation rows from Excel sheet \'Sampled Observations\')*")'
)

with open('build_tabfm_app.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Added bracketed methodology notes across build_tabfm_app.py successfully!")
