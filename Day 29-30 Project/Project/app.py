import streamlit as st

from jobsData_Utility import  load_jobs, get_unique_fields, filter_jobs

st.set_page_config(page_title="Job Search App", page_icon="🧑‍💻")

st.title("Welcome to Job Search App 🧑‍💻")

jobs = load_jobs()

job_titles, skill_options, experience_levels, location_types = get_unique_fields(jobs)

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    selected_title = st.selectbox("Job Title", ["Job Title"] + job_titles)

with col2:
    selected_skills = st.multiselect("Skills", skill_options)

with col3:
    selected_experience = st.selectbox("Experience", ["Experience"] + experience_levels)

with col4:
    selected_location = st.selectbox("Location Type", ["Location Type"] + location_types)


Filtered = False
 


if st.button("🔍 Show Matching Jobs"):
    
    Filtered = True
    st.markdown("---")
    st.write("### Matching Jobs")


    filtered_jobs = filter_jobs(
    jobs,
    skills=selected_skills,
    experience_level=selected_experience,
    location_type=selected_location,
    title=selected_title
    )

    if not filtered_jobs:
        st.warning("No matching jobs found. Try changing filters.")
    else:
        for job in filtered_jobs:
            st.markdown(f"**🧑‍💼 {job['title']}**")
            st.markdown(f"📍 *{job['location_type']}* | 🧪 *{job['experience_level']}*")
            st.markdown(f"🛠️ Skills: {', '.join(job['skills'])}")
            st.markdown(f"📄 {job['description']}")
            st.markdown("---")


if Filtered == False:    
    st.markdown("---")
    st.write("### All Jobs")
    for job in jobs:
        st.markdown(f"**🧑‍💼 {job['title']}**")
        st.markdown(f"📍 *{job['location_type']}* | 🧪 *{job['experience_level']}*")
        st.markdown(f"🛠️ Skills: {', '.join(job['skills'])}")
        st.markdown(f"📄 {job['description']}")
        st.markdown("---")