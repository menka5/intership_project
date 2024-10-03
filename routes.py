from flask import render_template

from app import app, db
from models import Employee, Department, Attendance
from datetime import datetime


@app.route("/employees")
def employees():
    employees = Employee.query.all()
    return render_template("employees.html", employees=employees)


@app.route("/departments")
def departments():
    departments = Department.query.all()
    return render_template("departments.html", departments=departments)


@app.route("/attendance")
def attendance():
    attendances = Attendance.query.all()
    return render_template("attendance.html", attendances=attendances)

@app.route("/add_employee", methods=["POST"])
def add_employee():
    data = request.form
    employee = Employee(
        name=data["name"],
        designation=data["designation"],
        department=data["department"],
        date_of_joining=datetime.strptime(data["date_of_joining"], "%Y-%m-%d"),
    )
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for("employees"))


@app.route("/add_department", methods=["POST"])
def add_department():
    data = request.form
    department = Department(name=data["name"])
    db.session.add(department)
    db.session.commit()
    return redirect(url_for("departments"))

@app.route("/mark_attendance", methods=["POST"])
def mark_attendance():
    data = request.form
    attendance = Attendance(
        employee_id=data["employee_id"],
        attendance_status=data["attendance_status"],
    )
    db.session.add(attendance)
    db.session.commit()
    return redirect(url_for("attendance"))

@app.route("/departments", methods=["GET"])
def departments():
    departments = Department.query.all()
    return render_template("departments.html", departments=departments)


@app.route("/add_department", methods=["POST"])
def add_department():
    data = request.form
    department = Department(name=data["name"])
    db.session.add(department)
    db.session.commit()
    return redirect(url_for("departments"))


@app.route("/edit_department/<int:department_id>", methods=["GET", "POST"])
def edit_department(department_id):
    department = Department.query.get_or_404(department_id)
    if request.method == "POST":
        department.name = request.form["name"]
        db.session.commit()
        return redirect(url_for("departments"))
    return render_template("edit_department.html", department=department)

@app.route("/delete_department/<int:department_id>", methods=["POST"])
def delete_department(department_id):
    department = Department.query.get_or_404(department_id)
    db.session.delete(department)
    db.session.commit()
    return redirect(url_for("departments"))

@app.route("/attendance", methods=["GET"])
def attendance():
    attendances = Attendance.query.all()
    return render_template("attendance.html", attendances=attendances)


@app.route("/mark_attendance", methods=["POST"])
def mark_attendance():
    data = request.form
    attendance = Attendance(
        employee_id=data["employee_id"],
        attendance_status=data["attendance_status"],
    )
    db.session.add(attendance)
    db.session.commit()
    return redirect(url_for("attendance"))


@app.route("/edit_attendance/<int:attendance_id>", methods=["GET", "POST"])
def edit_attendance(attendance_id):
    attendance = Attendance.query.get_or_404(attendance_id)
    if request.method == "POST":
        attendance.attendance_status = request.form["attendance_status"]
        db.session.commit()
        return redirect(url_for("attendance"))
    return render_template("edit_attendance.html", attendance=attendance)

    @app.route("/delete_attendance/<int:attendance_id>", methods=["POST"])
    def delete_attendance(attendance_id):
        attendance = Attendance.query.get_or_404(attendance_id)
        db.session.delete(attendance)
        db.session.commit()
        return redirect(url_for("attendance"))

