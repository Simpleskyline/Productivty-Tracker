from .models import db, Activity, Goal, Reminder, Session, Report

# --------- Activities ----------
def create_activity(data):
    activity = Activity(**data)
    db.session.add(activity)
    db.session.commit()
    return activity

def get_activities():
    return Activity.query.all()

# --------- Goals ----------
def create_goal(data):
    goal = Goal(**data)
    db.session.add(goal)
    db.session.commit()
    return goal

def get_goals():
    return Goal.query.all()

# --------- Reminders ----------
def create_reminder(data):
    reminder = Reminder(**data)
    db.session.add(reminder)
    db.session.commit()
    return reminder

def get_reminders():
    return Reminder.query.all()

# --------- Sessions ----------
def create_session(data):
    session = Session(**data)
    db.session.add(session)
    db.session.commit()
    return session

def get_sessions():
    return Session.query.all()

# --------- Reports ----------
def create_report(data):
    report = Report(**data)
    db.session.add(report)
    db.session.commit()
    return report

def get_reports():
    return Report.query.all()
