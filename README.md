🚀 Productivty Tracker

📖 Overview

This is a modern full-stack web application that helps users track and manage their activities.

It allows manual logging of activities, goal setting, reminders, and notifications. Data is stored locally using SQLite, ensuring privacy and offline accessibility.

✨ Features

✅ Manual logging of activities

✅ Local storage in SQLite database

✅ Notifications & reminders for activities

✅ Goal setting and progress tracking

✅ Modern full-stack architecture

✅ Private use — only for the owner

📌 Usage

Log activities manually through the dashboard

Set daily, weekly, or monthly goals

Get reminders via notifications

Track your progress visually

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Flask (Python)

Database: SQLite

📂 Project Structure
productivity-tracker/
│── frontend/          
│── backend/          
│── database/          
│── static/              
│── templates/       
│── requirements.txt  
│── README.md           

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/username/activity-tracker.git
cd activity-tracker

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Initialize Database
flask shell
>>> from backend.models import db
>>> db.create_all()
>>> exit()

5. Run the App
python app.py


The app will start on:
👉 http://127.0.0.1:5000/
