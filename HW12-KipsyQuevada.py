"""
Kipsy Quevada
SSW-810-WS: Special Topics in SSW
Summer 2018 | Professor Jim Rowland
Homework 12: Flask
"""

from flask import Flask, render_template
import sqlite3

app = Flask (__name__)

@app.route('/students')
def students_summary():
    students = [ # partial list of students
    {'cwid': '11658', 'name': 'Kelly, P', 'major': 'SYEN', 'taken': ['SSW 540'], 'remain': ['SYS 612', 'SYS 671', 'SYS 672', 'SYS 673', 'SYS 674', 'SYS 800']},
    {'cwid': '11714', 'name': 'Morton, A', 'major': 'SYEN', 'taken': ['SYS 611', 'SYS 645'], 'remain': ['SYS 612', 'SYS 671', 'SYS 672', 'SYS 673', 'SYS 674', 'SYS 800']}
    ]

    return render_template('students_table.html', title='Stevens Repository', table_title='Student Summary', students=students)

@app.route('/student_courses')
def student_courses():
    DB_FILE = "/Users/Class2018/Desktop/ssw810/HW11.db"
    query = """ select i.CWID, i.Name, i.Dept, g.Course, count(g.Course) as student_count
                from instructors i
                    left join grades g on i.CWID = g.Instructor_CWID
                group by i.CWID, i.Name, i.Dept, g.Course; """
    db = sqlite3.connect(DB_FILE)
    results = db.execute(query)

    #convert the query results into a list of dictionaries to pass to the template
    data = [{'cwid': cwid, 'name': name, 'department': department, 'courses': courses, 'students': students}
            for cwid, name, department, courses, students in results]
    
    return render_template('students_table.html', title='Stevens Repository', table_title="Number of students by course and instructor", students=data)

    db.close()
    
app.run(debug=True)