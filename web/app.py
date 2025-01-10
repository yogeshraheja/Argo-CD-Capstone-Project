from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

# Get the API host and port from environment variables, default to localhost
API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = os.getenv("API_PORT", "8000")

@app.route('/')
def index():
    """Main landing page with information about Thinknyx Technologies LLP."""
    thinknyx_info = {
        "company_name": "Thinknyx Technologies LLP",
        "description": (
            "Thinknyx Technologies LLP is a leading technology solutions provider "
            "specializing in software development, consulting, and digital transformation."
        ),
        "linkedin_url": "https://www.linkedin.com/company/thinknyx-technologies",
        "youtube_url": "https://www.youtube.com/@thinknyxtechnologies7446",
        "employees_link": url_for('employees')
    }
    return render_template('index.html', thinknyx_info=thinknyx_info)

@app.route('/employees')
def employees():
    """Fetch and display employee information."""
    url = f'http://{API_HOST}:{API_PORT}/api/employees'
    response = requests.get(url)
    employees = response.json() if response.status_code == 200 else []
    return render_template('employees.html', employees=employees)

@app.route('/add-employee', methods=['GET', 'POST'])
def add_employee():
    """Handle adding a new employee."""
    if request.method == 'POST':
        name = request.form['name']
        date_of_joining = request.form['date_of_joining']
        designation = request.form['designation']

        # Send POST request to the API
        url = f'http://{API_HOST}:{API_PORT}/api/employee'
        response = requests.post(url, json={
            'name': name,
            'date_of_joining': date_of_joining,
            'designation': designation
        })

        if response.status_code == 201:
            return redirect(url_for('employees'))
        else:
            return "Error adding employee", 400

    return render_template('add_employee.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
