# Database Schema

## Employees Table

| Column Name | Data Type | Description |
| --- | --- | --- |
| id | int | Unique identifier for the employee |
| name | varchar(100) | Employee name |
| designation | varchar(100) | Employee designation |
| department | varchar(100) | Employee department |
| date_of_joining | date | Date of joining |

## Attendance Table

| Column Name | Data Type | Description |
| --- | --- | --- |
| id | int | Unique identifier for the attendance record |
| employee_id | int | Foreign key referencing the Employees table |
| date | date | Date of attendance |
| status | varchar(100) | Attendance status (e.g., present, absent, leave) |