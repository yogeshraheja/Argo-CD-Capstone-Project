from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection settings
DB_HOST = os.getenv("PGHOST", "localhost")
DB_NAME = os.getenv("PGDATABASE", "postgres")
DB_USER = os.getenv("PGUSER", "postgres")
DB_PASSWORD = os.getenv("PGPASSWORD", "thinknyx")

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

@app.route('/api/employee-info', methods=['GET'])
def employee_info():
    """Endpoint to get employee information."""
    employees = get_employees()
    return jsonify(employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)