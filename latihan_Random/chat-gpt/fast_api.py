import gspread
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

app = FastAPI()

# SETUP GOOGEL SHEETS CLIEnt
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Data KM PDAM").sheet1

class KMinput(BaseModel):
    km_value: float

@app.post("/submit-km")
def submit_km(km: KMinput):
    try:
        today = datetime.today().strftime('%Y-%m-%d')
        sheet.append_row([today, data.km_value])
