#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


pip install fastapi uvicorn


# In[3]:


from fastapi import FastAPI, HTTPException
from datetime import datetime

app = FastAPI()

# Dictionary to store vehicle entry times
parking_data = {}

# Parking fee per hour
PARKING_RATE_PER_HOUR = 500

@app.post("/enter")
async def vehicle_entry(vehicle_number: str):
    entry_time = datetime.now()
    parking_data[vehicle_number] = entry_time
    return {"message": f"Vehicle {vehicle_number} entry recorded at {entry_time}"}

@app.post("/exit")
async def vehicle_exit(vehicle_number: str):
    if vehicle_number in parking_data:
        entry_time = parking_data.pop(vehicle_number)
        exit_time = datetime.now()
        parking_duration = (exit_time - entry_time).total_seconds() / 3600
        parking_fee = int(parking_duration) * PARKING_RATE_PER_HOUR
        return {
            "vehicle_number": vehicle_number,
            "entry_time": str(entry_time),
            "exit_time": str(exit_time),
            "parking_fee": parking_fee,
        }
    else:
        raise HTTPException(status_code=404, detail="Vehicle entry not found")


# In[10]:


from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# In[ ]:





# In[ ]:




