# Directory structure
'''
job_portal/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── jobs.html
│   ├── post_job.html
│   └── apply.html
│
├── app.py
├── models.py
└── requirements.txt
'''

# requirements.txt
flask==2.0.1
flask-sqlalchemy==2.5.1
flask-login==0.5.0
werkzeug==2.0.1
python-dotenv==0.19.0

# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_employer = db.Column(db.Boolean, default=False)
    jobs = db.relationship('Job', backref='author', lazy=True)
    applications = db.relationship('Application', backref='applicant', lazy=True)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    applications = db.relationship('Application', backref='job', lazy=True)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    resume = db.Column(db.String(100), nullable=False)
    cover_letter = db.Column(db.Text)
    date_applied = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')

# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models import db, User, Job, Application
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_portal.db'
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    jobs = Job.query.order_by(Job.date_posted.desc()).limit(10).all()
    return render_template('index.html', jobs=jobs)

@app.route('/jobs')
def jobs():
    query = request.args.get('q', '')
    location = request.args.get('location', '')
    
    jobs_query = Job.query
    if query:
        jobs_query = jobs_query.filter(Job.title.contains(query) | Job.description.contains(query))
    if location:
        jobs_query = jobs_query.filter(Job.location.contains(location))
    
    jobs = jobs_query.order_by(Job.date_posted.desc()).all()
    return render_template('jobs.html', jobs=jobs)

@app.route('/job/<int:job_id>')
def job_detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job_detail.html', job=job)

@app.route('/post-job', methods=['GET', 'POST'])
@login_required
def post_job():
    if request.method == 'POST':
        job = Job(
            title=request.form['title'],
            description=request.form['description'],
            company=request.form['company'],
            location=request.form['location'],
            salary=request.form['salary'],
            user_id=current_user.id
        )
        db.session.add(job)
        db.session.commit()
        flash('Job posted successfully!', 'success')
        return redirect(url_for('jobs'))
    return render_template('post_job.html')

@app.route('/apply/<int:job_id>', methods=['POST'])
@login_required
def apply_job(job_id):
    job = Job.query.get_or_404(job_id)
    
    if request.method == 'POST':
        resume = request.files['resume']
        # Save resume file logic here
        
        application = Application(
            user_id=current_user.id,
            job_id=job_id,
            resume=resume.filename,
            cover_letter=request.form.get('cover_letter', '')
        )
        db.session.add(application)
        db.session.commit()
        flash('Application submitted successfully!', 'success')
        return redirect(url_for('job_detail', job_id=job_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
