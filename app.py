from flask import Flask
import pyodbc

app = Flask(__name__)

# SQL Database connection string - ЕНДІ ДҰРЫС
connection_string = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:zhanyladmin.database.windows.net;"
    "Database=student_database;"
    "Uid=zhanyladmin;"
    "Pwd=admin123;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

@app.route('/')
def hello():
    try:
        # Database-ке қосылу
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        # Students кестесінен деректерді алу
        cursor.execute("SELECT * FROM Students")
        students = cursor.fetchall()
        
        # Нәтижені HTML-ге айналдыру
        result = "<h1>Студенттер тізімі:</h1><ul>"
        for student in students:
            result += f"<li>{student.Name} - {student.Major} - {student.Grade}</li>"
        result += "</ul>"
        
        conn.close()
        return result
        
    except Exception as e:
        return f"<h1>Қате:</h1><p>{str(e)}</p>"

@app.route('/add')
def add_student():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        # Жаңа студент қосу
        cursor.execute(
            "INSERT INTO Students (Name, Major, Grade) VALUES (?, ?, ?)", 
            'Айгүл', 'Computer Science', 95
        )
        conn.commit()
        conn.close()
        
        return "Студент сәтті қосылды!"
        
    except Exception as e:
        return f"Қате: {str(e)}"

if __name__ == '__main__':
    app.run()
