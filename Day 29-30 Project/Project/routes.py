from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from jobsData_Utility import load_jobs, save_jobs


app = FastAPI()

class jobPost(BaseModel):
   job_id: int
   title: str
   description: str
   skills: List[str]
   experience_level: str
   location_type: str

@app.get('/')
def job_list_len():
    job = load_jobs()
    return{'No of jobs are:':len(job)}

 
@app.post("/items/")
def create_item(item: jobPost):
    
    jobs = load_jobs()

    # Check for existing job_id
    for job in jobs:
        if job['job_id'] == item.job_id:
            raise HTTPException(status_code=400, detail="Job ID already exists. Use update instead.")

    # If not found, add the job
    jobs.append(item.dict())
    save_jobs(jobs)

    return {"message": "Job added successfully", "data": item}


@app.put("/items/{job_id}")
def update_item(job_id: int, updated_job: jobPost):
    jobs = load_jobs()
    for i, job in enumerate(jobs):
        if job['job_id'] == job_id:
            jobs[i] = updated_job.dict()
            save_jobs(jobs)
            return {"message": "Job updated successfully", "data": updated_job}
    
    raise HTTPException(status_code=404, detail="Job ID not found for update.")


@app.delete("/items/{job_id}")
def delete_item(job_id: int):
    jobs = load_jobs()
    for i, job in enumerate(jobs):
        if job['job_id'] == job_id:
            deleted_job = jobs.pop(i)
            save_jobs(jobs)
            return {"message": "Job deleted successfully", "data": deleted_job}
    
    raise HTTPException(status_code=404, detail="Job ID not found for deletion.")
