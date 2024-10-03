from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    date_of_joining = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"Employee('{self.name}', '{self.designation}', '{self.department}')"


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Department('{self.name}')"

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    attendance_date = db.Column(db.Date, nullable=False, default=db.func.current_date())
    attendance_status = db.Column(db.Boolean, nullable=False)

    employee = db.relationship('Employee', backref=db.backref('attendances', lazy=True))

    def __repr__(self):
        return f"Attendance('{self.employee.name}', '{self.attendance_date}', '{self.attendance_status}')"
