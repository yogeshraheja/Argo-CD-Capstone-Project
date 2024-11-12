from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

# Database connection settings
DB_HOST = os.getenv("PGHOST", "localhost")
DB_NAME = os.getenv("PGDATABASE", "postgres")
DB_USER = os.getenv("PGUSER", "postgres")
DB_PASSWORD = os.getenv("PGPASSWORD", "postgres")

def get_employees():
    """Fetch employees from the database."""
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()
        cursor.execute("SELECT employee_id, name, date_of_joining, designation FROM employee;")
        employees = cursor.fetchall()
        return [{"employee_id": emp[0], "name": emp[1], "date_of_joining": emp[2], "designation": emp[3]} for emp in employees]
    except Exception as e:
        print(f"Error fetching employees: {e}")
        return []
    finally:
        if connection:
            cursor.close()
            connection.close()

@app.route('/api/employees', methods=['GET'])
def employee_info():
    """Endpoint to get employee information."""
    employees = get_employees()
    return jsonify(employees)

@app.route('/api/employee', methods=['POST'])
def add_employee():
    """Endpoint to add a new employee."""
    data = request.json
    name = data.get('name')
    date_of_joining = data.get('date_of_joining', None)
    designation = data.get('designation')

    if not name or not designation:
        return jsonify({"error": "Name and designation are required."}), 400

    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO employee (name, date_of_joining, designation) VALUES (%s, %s, %s)",
            (name, date_of_joining, designation)
        )
        connection.commit()
        return jsonify({"message": "Employee added successfully."}), 201
    except Exception as e:
        print(f"Error inserting employee: {e}")
        return jsonify({"error": "Error inserting employee."}), 500
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)