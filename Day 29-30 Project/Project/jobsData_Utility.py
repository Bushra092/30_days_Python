import json, os


def load_jobs(file_path=None):
    if not file_path:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "jobs_dataset.json")

    with open(file_path, "r") as f:
        return json.load(f)
    
def save_jobs(jobs, file_path=None):
    if not file_path:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "jobs_dataset.json")

    with open(file_path, 'w') as f:
        json.dump(jobs, f, indent=4)    

# Extract unique fiel ds for filters
def get_unique_fields(jobs):
    unique_titles = set()
    unique_skills = set()
    unique_experience_levels = set()
    unique_location_types = set()

    for job in jobs:
        unique_titles.add(job.get('title'))
        unique_experience_levels.add(job.get('experience_level'))
        unique_location_types.add(job.get('location_type'))

        for skill in job.get('skills', []):
            unique_skills.add(skill)

    return (
        sorted(unique_titles),
        sorted(unique_skills),
        sorted(unique_experience_levels),
        sorted(unique_location_types)
    )

# Filter jobs based on user input
def filter_jobs(jobs, skills=None, experience_level='', location_type='', title=''):
    skills = skills or []
    results = []

    for job in jobs:
        if title and job.get('title') != title:
            continue
        if experience_level and job.get('experience_level') != experience_level:
            continue
        if location_type and job.get('location_type') != location_type:
            continue
        if skills and not set(skills).intersection(set(job.get('skills', []))):
            continue
        results.append(job)

    return results
