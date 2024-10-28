from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Get the API host from environment variable, default to localhost
API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = os.getenv("API_PORT", "8000")

@app.route('/employees')
def employee():
    """Fetch and display employee information."""
    url = f'http://{API_HOST}:{API_PORT}/api/employee-info'
    response = requests.get(url)
    employees = response.json() if response.status_code == 200 else []
    return render_template('employees.html', employees=employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)