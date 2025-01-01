# Online-job-portal

## Overview
The Job Portal Project is a web-based application designed to connect job seekers and employers. The application allows job seekers to search and apply for jobs, while employers can post and manage job listings. The platform is built using Python (Flask) for the backend, with JavaScript, HTML, and CSS for the frontend.

## Features
- **For Job Seekers**:
  - User registration and login.
  - Search and browse job listings.
  - Apply for jobs.
  - Profile management.

- **For Employers**:
  - User registration and login.
  - Post job listings.
  - Manage job applications.

- **Admin Panel**:
  - Manage users (job seekers and employers).
  - Moderate job listings.

## Technologies Used
- **Backend**: Python (Flask framework), SQLite (or PostgreSQL/MySQL).
- **Frontend**: HTML, CSS (Bootstrap for responsiveness), JavaScript.
- **Deployment**: Heroku (or AWS).

## Installation
### Prerequisites
- Python 3.x
- Node.js (for JavaScript package management, if required)
- Git (optional, for version control)

### Steps
1. Clone the repository:
   ```
   git clone <repository-url>
   cd job-portal
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```
4. Run the application:
   ```
   flask run
   ```
   The application will be available at `http://127.0.0.1:5000`.

## Usage
1. Open the application in a browser.
2. Register as a job seeker or employer.
3. Use the respective dashboards to search for jobs or post job listings.
4. Admins can log in to manage users and moderate content.

## Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```
   git commit -m "Description of changes"
   ```
4. Push to your fork and submit a pull request.

## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.
