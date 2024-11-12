from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

# Get the API host and port from environment variables, default to localhost
API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = os.getenv("API_PORT", "8000")

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