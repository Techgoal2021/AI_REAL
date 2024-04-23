from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# Sample reminders list
reminders = [
    {"type": "Birthday", "date": datetime.date(2024, 5, 15), "recurring": True},
    {"type": "Anniversary", "date": datetime.date(2024, 7, 20), "recurring": False},
    {"type": "Appointment", "date": datetime.date(2024, 4, 30), "recurring": False},
    {"type": "Deadline", "date": datetime.date(2024, 6, 15), "recurring": False}
]

# Function to check for upcoming reminders
def check_upcoming_reminders():
    today = datetime.date.today()
    upcoming_reminders = [reminder for reminder in reminders if reminder['date'] >= today]
    upcoming_reminders.sort(key=lambda x: x['date'])
    return upcoming_reminders

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_reminder', methods=['POST'])
def add_reminder():
    event_type = request.form['event_type']
    year = int(request.form['year'])
    month = int(request.form['month'])
    day = int(request.form['day'])
    event_date = datetime.date(year, month, day)
    recurring = request.form['recurring'].lower() == 'yes'
    reminders.append({"type": event_type, "date": event_date, "recurring": recurring})
    return render_template('index.html', reminders=reminders)


@app.route('/check_upcoming_reminders')
def upcoming_reminders():
    upcoming = check_upcoming_reminders()
    return render_template('index.html', upcoming_reminders=upcoming)

if __name__ == '__main__':
    app.run(debug=True)
